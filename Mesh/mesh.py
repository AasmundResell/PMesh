import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder
    

def generateMesh(geomDomain):    
    
    ###
    ### SMESH component
    ###


    smesh = smeshBuilder.New()
    #smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                     # multiples meshes built in parallel, complex and numerous mesh edition (performance)
    
    NETGEN_3D_Parameters_2 = smesh.CreateHypothesis('NETGEN_Parameters_3D', 'libNETGENEngine.so')
    NETGEN_3D_Parameters_2.SetOptimize( 1 )
    NETGEN_3D_Parameters_2.SetMaxSize( 20 )
    NETGEN_3D_Parameters_2.SetMinSize( 0.1 )
    NETGEN_3D_Parameters_2.SetFineness( 3 )
    NETGEN_3D_Parameters_2.SetElemSizeWeight( 4.63916e-310 )
    Viscous_Layers_2 = smesh.CreateHypothesis('ViscousLayers')
    Viscous_Layers_2.SetTotalThickness( 1 )
    Viscous_Layers_2.SetNumberLayers( 20 )
    Viscous_Layers_2.SetStretchFactor( 1.2 )
    Viscous_Layers_2.SetFaces( [], 1 )
    Viscous_Layers_2.SetMethod( smeshBuilder.SURF_OFFSET_SMOOTH )
    Mesh = smesh.Mesh(geomDomain.domain,'Mesh')
    NETGEN_1D_2D = Mesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
    NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
    NETGEN_2D_Parameters_1.SetMaxSize( 41.2311 )
    NETGEN_2D_Parameters_1.SetMinSize( 0.160716 )
    NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
    NETGEN_2D_Parameters_1.SetOptimize( 1 )
    NETGEN_2D_Parameters_1.SetFineness( 2 )
    NETGEN_2D_Parameters_1.SetChordalError( -1 )
    NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
    NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
    NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
    NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
    NETGEN_2D_Parameters_1.SetWorstElemMeasure( 22031 )
    Viscous_Layers_2D_1 = NETGEN_1D_2D.ViscousLayers2D(1,20,1.2,[],0)
    NETGEN_3D = Mesh.Tetrahedron()
    NETGEN_3D_Parameters_1 = NETGEN_3D.Parameters()
    NETGEN_3D_Parameters_1.SetMaxSize( 29 )
    NETGEN_3D_Parameters_1.SetMinSize( 0.160716 )
    NETGEN_3D_Parameters_1.SetOptimize( 1 )
    NETGEN_3D_Parameters_1.SetFineness( 2 )
    NETGEN_3D_Parameters_1.SetElemSizeWeight( 4.63916e-310 )
    Viscous_Layers_1 = NETGEN_3D.ViscousLayers(1,20,1,[ 3 ],1,smeshBuilder.SURF_OFFSET_SMOOTH)
    status = Mesh.RemoveHypothesis(Viscous_Layers_2D_1)
    status = Mesh.RemoveHypothesis(Viscous_Layers_1)
    status = Mesh.RemoveHypothesis(NETGEN_2D_Parameters_1)
    NETGEN_2D_Parameters_2 = NETGEN_1D_2D.Parameters()
    NETGEN_2D_Parameters_2.SetMaxSize( 77.5177 )
    NETGEN_2D_Parameters_2.SetMinSize( 3.11868 )
    NETGEN_2D_Parameters_2.SetSecondOrder( 0 )
    NETGEN_2D_Parameters_2.SetOptimize( 1 )
    NETGEN_2D_Parameters_2.SetFineness( 3 )
    NETGEN_2D_Parameters_2.SetChordalError( -1 )
    NETGEN_2D_Parameters_2.SetChordalErrorEnabled( 0 )
    NETGEN_2D_Parameters_2.SetUseSurfaceCurvature( 1 )
    NETGEN_2D_Parameters_2.SetFuseEdges( 1 )
    NETGEN_2D_Parameters_2.SetUseDelauney( 0 )
    NETGEN_2D_Parameters_2.SetQuadAllowed( 0 )
    NETGEN_2D_Parameters_2.SetWorstElemMeasure( 21911 )
    NETGEN_2D_Parameters_2.SetCheckChartBoundary( 3 )
    status = Mesh.RemoveHypothesis(NETGEN_3D_Parameters_1)
    NETGEN_3D_Parameters_3 = NETGEN_3D.Parameters()
    NETGEN_3D_Parameters_3.SetMaxSize( 77.5177 )
    NETGEN_3D_Parameters_3.SetMinSize( 3.11868 )
    NETGEN_3D_Parameters_3.SetOptimize( 1 )
    NETGEN_3D_Parameters_3.SetFineness( 3 )
    NETGEN_3D_Parameters_3.SetElemSizeWeight( 4.64966e-310 )
    NETGEN_3D_Parameters_3.SetCheckOverlapping( 5 )
    NETGEN_3D_Parameters_3.SetCheckChartBoundary( 3 )
    isDone = Mesh.Compute()


    ## Set names of Mesh objects
    smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
    smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
    smesh.SetName(Mesh.GetMesh(), 'Mesh')
    smesh.SetName(Viscous_Layers_2D_1, 'Viscous Layers 2D_1')
    smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
    smesh.SetName(Viscous_Layers_1, 'Viscous Layers_1')
    smesh.SetName(NETGEN_3D_Parameters_3, 'NETGEN 3D Parameters_3')
    smesh.SetName(NETGEN_3D_Parameters_2, 'NETGEN 3D Parameters_2')
    smesh.SetName(Viscous_Layers_2, 'Viscous Layers_2')
    smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
    smesh.SetName(NETGEN_2D_Parameters_2, 'NETGEN 2D Parameters_2')

    return Mesh