from salome.geom import geomBuilder

from CFDMSH import *

import salome

def generateAirfoilGeometry(points):

    # Get the GEOM module
    geompy = geomBuilder.New()
    # Loop over the lines and create a point for each set of coordinates
    geom_points = [geompy.MakeVertex(x,y, 0.0) for x,y in points]

    for i,point in enumerate(geom_points):
        geompy.addToStudy(point, "Point_{}".format(i))

    #Create compound for compatability with CFDMSH
    compound = geompy.MakeCompound(geom_points)
    
    AddToStudy(compound,"Compound")


    foil_wire = MakeFoilFromUnsortedVertexes(compound,coef=2.5,poly=True)

    GetBoundaryVertexes(foil_wire)