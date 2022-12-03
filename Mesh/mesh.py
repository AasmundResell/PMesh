import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder
from Mesh.meshTools import *

class MeshGenerator():

    def __init__(self,name,geomDomain,**meshParams):
        self.smesh = smeshBuilder.New()

        self.geomDomain = geomDomain
        self.meshParams = meshParams
        

        self.readMeshCommands()

        self.definePhysicalQuantities()
        self.defineVolumeAlgorithm()

        self.name = name

    def readMeshCommands(self):

        self.inflationLayers = self.meshParams.get("inflationLayers")

        if self.inflationLayers:
            
            self.yPlusTarget = self.meshParams.get("yPlussValue")

            if self.meshParams.get("growthRate"):
                self.growthRate = self.meshParams.get("growth_rate")
            else:
                self.growthRate = 1.2
                Warning("BL Growth rate is not specified, default value is 1.2")
        
            if self.meshParams.get("totalBLCells"):
                self.numBLcells = self.meshParams.get("totalBLCells")
            else:
                self.numBLcells = 20
                Warning("Number of BL cells is not specified, default value is 20")
        

        
        if self.meshParams.get("fineness"):
            self.fineness = self.meshParams.get("fineness")

            if type(self.fineness) is not int and self.fineness >= 0  and self.fineness <= 4:
                RuntimeError("Mesh fineness must be specified as an integer in the range: 0 (very coarse) - 4 (very fine) ")

        else: #Very fine by default
            self.fineness = 4
            Warning("Mesh fineness set to very fine by default")

        
        

    def definePhysicalQuantities(self):

        if "physicalQuantities" in self.meshParams:
            values = {k.lower():v for k,v in self.meshParams["physicalQuantities"].items()} #make keys case insensitive

            if values.get("u"):
                self.U = values.get("u")
            elif values.get("m"): #Mach number
                if values.get("u"):
                    Warning("Specified mach number is overridden by the velocity U")
                else:
                    self.M = values["m"]
                    if values.get("c"): #Speed of sound
                        self.c = values.get("c")
                    else: #TODO Consider alternative of calculating c from formula    
                        self.c = 343.0    
                        Warning("Speed of sound set to 343 m/s")
                    self.U = self.M*self.c
            else:
                RuntimeError("Velocity must be specified for the mesh generation!")

            if values.get("rho"):
                self.rho = values.get("rho")
            else: 
                self.rho = 1.225 
                Warning("Standard atmospheric conditions is used for the air density")

            if values.get("mu"):
                self.mu = values.get("mu")
            else: 
                self.mu = 1.8*10**(-5) 
                Warning("Standard atmospheric conditions is used for the air dynamic viscosity")

            self.L = self.geomDomain.projectile.totalLength/1000 #Converted to standard SI units
            print("Total length of the projectile: {} mm".format(self.L*1000))

            self.Re_L = Re(self.U,self.L,self.rho,self.mu)
            self.BL_thickness_experimental = BLThicknessFromTheory(self.Re_L,self.L)*1000    

            if self.inflationLayers:
                
                y_init = YPlus(self.yPlusTarget, self.U, self.L, self.rho, self.mu, skinFrictionMethod="Schlichting")
                self.totalBLHeight = BLThicknessFromCellHeight(y_init,self.numBLcells,self.growthRate)*1000

        else:
            RuntimeError("Physical quantities must be specified for the mesh to be generated!")

    def defineVolumeAlgorithm(self):
        """
        Defines the algorithms for the volume mesh
        """
        #TODO
        
        return None
    

    def generateMesh(self):

        if self.inflationLayers:
            return self.generateMeshWithBL()
        elif not self.inflationLayers:
            return self.generateMeshNoBL()
        else:
            ValueError("Inflation layer not specified") 

    def generateMeshWithBL(self):    
        
        
        self.mesh = self.smesh.Mesh(self.geomDomain.domain,self.name)
        
        NETGEN_1D_2D_3D = self.mesh.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
        NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
        NETGEN_3D_Parameters_1.SetMaxSize( 73.9243 )
        NETGEN_3D_Parameters_1.SetMinSize( 0.265181 )
        NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
        NETGEN_3D_Parameters_1.SetOptimize( 1 )
        NETGEN_3D_Parameters_1.SetFineness( self.fineness )
        NETGEN_3D_Parameters_1.SetChordalError( -1 )
        NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 0 )
        NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
        NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
        NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
        NETGEN_3D_Parameters_1.UnsetLocalSizeOnEntry("Projectile_1")
        for pface in self.geomDomain.projectileGroups:
            NETGEN_3D_Parameters_1.SetLocalSizeOnShape(pface, 4)
       
        NETGEN_3D_Parameters_1.UnsetLocalSizeOnEntry("Projectile_1")
        Farfield_1 = self.mesh.GroupOnGeom(self.geomDomain.Farfield,'Farfield',SMESH.FACE)
        Projectile_1 = self.mesh.GroupOnGeom(self.geomDomain.Projectile,'Projectile',SMESH.FACE)
       
        #isDone = self.mesh.Compute()
        #[ Farfield_1, Projectile_1 ] = self.mesh.GetGroups()
        Viscous_Layers_1 = NETGEN_1D_2D_3D.ViscousLayers(self.totalBLHeight,self.numBLcells,
            self.growthRate,self.geomDomain.domainIDs,1,smeshBuilder.SURF_OFFSET_SMOOTH)
        isDone = self.mesh.Compute()
        [ Farfield_1, Projectile_1 ] = self.mesh.GetGroups()


        ## Set names of Mesh objects
        self.smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
        self.smesh.SetName(self.mesh.GetMesh(), self.name)
        self.smesh.SetName(Farfield_1, 'Farfield')
        self.smesh.SetName(Projectile_1, 'Projectile')
        self.smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
        self.smesh.SetName(Viscous_Layers_1, 'Viscous Layers_1')

        #self.printMeshInfo()

        return self.mesh

    def generateMeshNoBL(self):  

        self.mesh = self.smesh.Mesh(self.geomDomain.domain,self.name)
        
        NETGEN_1D_2D_3D = self.mesh.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
        NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
        NETGEN_3D_Parameters_1.SetMaxSize( 73.9243 )
        NETGEN_3D_Parameters_1.SetMinSize( 0.265181 )
        NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
        NETGEN_3D_Parameters_1.SetOptimize( 1 )
        NETGEN_3D_Parameters_1.SetFineness( self.fineness )
        NETGEN_3D_Parameters_1.SetChordalError( -1 )
        NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 0 )
        NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
        NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
        NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
        NETGEN_3D_Parameters_1.UnsetLocalSizeOnEntry("Projectile_1")
        for pface in self.geomDomain.projectileGroups:
            NETGEN_3D_Parameters_1.SetLocalSizeOnShape(pface, 4)
       
        NETGEN_3D_Parameters_1.SetCheckChartBoundary( 3 )
        NETGEN_3D_Parameters_1.UnsetLocalSizeOnEntry("Projectile_1")
        Farfield_1 = self.mesh.GroupOnGeom(self.geomDomain.Farfield,'Farfield',SMESH.FACE)
        Projectile_1 = self.mesh.GroupOnGeom(self.geomDomain.Projectile,'Projectile',SMESH.FACE)
       
        
        isDone = self.mesh.Compute()
        [ Farfield_1, Projectile_1 ] = self.mesh.GetGroups()


        ## Set names of Mesh objects
        self.smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
        self.smesh.SetName(self.mesh.GetMesh(), self.name)
        self.smesh.SetName(Farfield_1, 'Farfield')
        self.smesh.SetName(Projectile_1, 'Projectile')
        self.smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')

        #self.printMeshInfo()
        
        return self.mesh

    def printMeshInfo(self):
        info = self.mesh.GetMeshInfo()
        print(type(info))
        num_tetras = info.get("Entity_Tetra") + info.get("Entity_Quad_Tetra")
        num_hex = info["Entity_Hexa"] + info["Entity_Quad_Hexa"] + info["Entity_TriQuad_Hexa"]
        num_prism_layers = info["Entity_Hexagonal_Prism"]

        print("Total number of tethedrons: ",num_tetras)
        print("Total number of hexahedrons: ",num_hex)
        print("Total number of prism layers: ",num_prism_layers)
        
        print("\nTotal number of cells: ",  num_hex + num_prism_layers + num_tetras )
        print("\nTotal number of nodes: ",info["Entity_Node"])

    def checkMeshQuality(self):
        #TODO
        return None