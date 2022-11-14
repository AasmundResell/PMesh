import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder
    
class MeshGenerator():

    def __init__(self,name,**meshParams):
        self.smesh = smeshBuilder.New()

        self.meshParams = meshParams

        self.defineSurfaceAlg()
        self.defineVolumeAlg()
        self.name = name
    def defineVolumeAlg(self):
        """
        Defines the algorithms for the volume mesh
        """
        #TODO
        print("TEMP")

    def defineSurfaceAlg(self):
        """
        Defines the algorithms for the surface mesh
        """
        #TODO
        print("TEMP")

    def generateMesh(self,geomDomain):    
    
        self.mesh = self.smesh.Mesh(geomDomain.domain,self.name)
        NETGEN_1D_2D = self.mesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)

        NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
        NETGEN_2D_Parameters_1.SetMaxSize( 30 )
        NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
        NETGEN_2D_Parameters_1.SetOptimize( 1 )
        NETGEN_2D_Parameters_1.SetFineness( 4 )
        NETGEN_2D_Parameters_1.SetChordalError( -1 )
        NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
        NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
        NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
        NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
        
        for pface in geomDomain.projectileGroups:
            NETGEN_2D_Parameters_1.SetLocalSizeOnShape(pface, 4)
       
        
        NETGEN_2D_Parameters_1.SetMinSize( 0.1 )
        NETGEN_2D_Parameters_1.SetWorstElemMeasure( 22050 )
        
        NETGEN_3D = self.mesh.Tetrahedron()
        NETGEN_3D_Parameters_1 = NETGEN_3D.Parameters()
        NETGEN_3D_Parameters_1.SetMaxSize( 30 )
        NETGEN_3D_Parameters_1.SetOptimize( 1 )
        NETGEN_3D_Parameters_1.SetFineness( 4 )
        NETGEN_3D_Parameters_1.SetNbVolOptSteps( 4 )

        for pface in geomDomain.projectileGroups:
            NETGEN_3D_Parameters_1.SetLocalSizeOnShape(pface, 4)

        NETGEN_3D_Parameters_1.SetMinSize( 0.1 )
        NETGEN_3D_Parameters_1.SetElemSizeWeight( 4.67919e-310 )


        Farfield_1 = self.mesh.GroupOnGeom(geomDomain.Farfield,'Farfield',SMESH.FACE)
        Rocket_2 = self.mesh.GroupOnGeom(geomDomain.Projectile,'Projectile',SMESH.FACE)
        
        isDone = self.mesh.Compute()
        [ Farfield_1, Rocket_2 ] = self.mesh.GetGroups()
        Viscous_Layers_1 = NETGEN_3D.ViscousLayers(1.5,20,1.2,geomDomain.domainIDs,1,smeshBuilder.SURF_OFFSET_SMOOTH)
        isDone = self.mesh.Compute()
        [ Farfield_1, Rocket_2 ] = self.mesh.GetGroups()
        
        ## Set names of Mesh objects
        self.smesh.SetName(Rocket_2, 'Rocket')
        self.smesh.SetName(Farfield_1, 'Farfield')
        self.smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
        self.smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
        self.smesh.SetName(self.mesh.GetMesh(), self.name)
        self.smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
        self.smesh.SetName(Viscous_Layers_1, 'Viscous Layers_1')
        self.smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')

        return self.mesh

    def checkMeshQuality(self):
        #TODO
        print("TEMP")