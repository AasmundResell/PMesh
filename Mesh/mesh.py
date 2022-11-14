import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder
    
class MeshGenerator():

    def __init__(self):
        self.smesh = smeshBuilder.New()


    def generateMesh(self,geomDomain):    
    
        Mesh_1 = self.smesh.Mesh(geomDomain.domain,'Mesh_1')
        NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)

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
        
        NETGEN_3D = Mesh_1.Tetrahedron()
        NETGEN_3D_Parameters_1 = NETGEN_3D.Parameters()
        NETGEN_3D_Parameters_1.SetMaxSize( 30 )
        NETGEN_3D_Parameters_1.SetOptimize( 1 )
        NETGEN_3D_Parameters_1.SetFineness( 4 )
        NETGEN_3D_Parameters_1.SetNbVolOptSteps( 4 )

        for pface in geomDomain.projectileGroups:
            NETGEN_3D_Parameters_1.SetLocalSizeOnShape(pface, 4)

        NETGEN_3D_Parameters_1.SetMinSize( 0.1 )
        NETGEN_3D_Parameters_1.SetElemSizeWeight( 4.67919e-310 )


        Farfield_1 = Mesh_1.GroupOnGeom(geomDomain.Farfield,'Farfield',SMESH.FACE)
        Rocket_2 = Mesh_1.GroupOnGeom(geomDomain.Projectile,'Projectile',SMESH.FACE)
        
        isDone = Mesh_1.Compute()
        [ Farfield_1, Rocket_2 ] = Mesh_1.GetGroups()
        Viscous_Layers_1 = NETGEN_3D.ViscousLayers(1.5,20,1.2,geomDomain.domainIDs,1,smeshBuilder.SURF_OFFSET_SMOOTH)
        isDone = Mesh_1.Compute()
        [ Farfield_1, Rocket_2 ] = Mesh_1.GetGroups()
        
        ## Set names of Mesh objects
        self.smesh.SetName(Rocket_2, 'Rocket')
        self.smesh.SetName(Farfield_1, 'Farfield')
        self.smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
        self.smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
        self.smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
        self.smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
        self.smesh.SetName(Viscous_Layers_1, 'Viscous Layers_1')
        self.smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')

        return Mesh_1