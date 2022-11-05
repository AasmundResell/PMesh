#!/usr/bin/env python

import sys
from tkinter import E
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'bajs')


###
### SHAPER component
###

from SketchAPI import *

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Sketch
Sketch_side = model.addSketch(partSet, model.defaultPlane("XOY"))

### Create SketchLine
SketchLine_1 = Sketch_side.addLine(0, 0, 7.39, 0)

### Create SketchProjection
SketchProjection_1 = Sketch_side.addProjection(model.selection("VERTEX", "Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_side.setCoincident(SketchLine_1.startPoint(), SketchPoint_1.result())
Sketch_side.setHorizontal(SketchLine_1.result())

### Create SketchLine
SketchLine_2 = Sketch_side.addLine(7.39, 0, 7.39, 0.8100000000000001)
Sketch_side.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_side.setVertical(SketchLine_2.result())

### Create SketchLine
SketchLine_3 = Sketch_side.addLine(0, 0.1099999999999999, 0, 0)
SketchLine_3.setName("mmm_6")
SketchLine_3.result().setName("mmm_6")
Sketch_side.setCoincident(SketchLine_1.startPoint(), SketchLine_3.endPoint())
Sketch_side.setVertical(SketchLine_3.result())
Sketch_side.setLength(SketchLine_2.result(), 0.8100000000000001)
Sketch_side.setVerticalDistance(SketchLine_3.startPoint(), SketchAPI_Point(SketchPoint_1).coordinates(), 0.11)

### Create SketchPoint
SketchPoint_2 = Sketch_side.addPoint(7.39, 0.8100000000000001)
Sketch_side.setCoincident(SketchLine_2.endPoint(), SketchPoint_2.coordinates())

### Create SketchPoint
SketchPoint_3 = Sketch_side.addPoint(7.39, 0.8100000000000001)
Sketch_side.setCoincident(SketchLine_2.endPoint(), SketchPoint_3.coordinates())

### Create SketchPoint
SketchPoint_4 = Sketch_side.addPoint(0, 0.1099999999999999)
Sketch_side.setCoincident(SketchLine_3.startPoint(), SketchPoint_4.coordinates())

### Create SketchLine
SketchLine_4 = Sketch_side.addLine(7.39, 0, 7.59, 0)
SketchLine_4.setName("SketchLine_7")
SketchLine_4.result().setName("SketchLine_7")
Sketch_side.setCoincident(SketchLine_1.endPoint(), SketchLine_4.startPoint())
Sketch_side.setHorizontal(SketchLine_4.result())

### Create SketchLine
SketchLine_5 = Sketch_side.addLine(7.59, 0, 7.59, 0.6100000000000001)
SketchLine_5.setName("SketchLine_8")
SketchLine_5.result().setName("SketchLine_8")
Sketch_side.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())
Sketch_side.setVertical(SketchLine_5.result())

### Create SketchLine
SketchLine_6 = Sketch_side.addLine(7.59, 0.6100000000000001, 7.39, 0.8100000000000001)
SketchLine_6.setName("SketchLine_9")
SketchLine_6.result().setName("SketchLine_9")
Sketch_side.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())
Sketch_side.setCoincident(SketchLine_2.endPoint(), SketchLine_6.endPoint())

### Create SketchPoint
SketchPoint_5 = Sketch_side.addPoint(4.12, 0)
SketchPoint_5.setName("SketchPoint_6")
SketchPoint_5.result().setName("SketchPoint_6")
Sketch_side.setCoincident(SketchPoint_5.coordinates(), SketchLine_1.result())
Sketch_side.setHorizontalDistance(SketchAPI_Point(SketchPoint_1).coordinates(), SketchPoint_5.coordinates(), 4.12)

### Create SketchLine
SketchLine_7 = Sketch_side.addLine(4.12, 0, 4.12, 0.8099999999999999)
SketchLine_7.setName("SketchLine_10")
SketchLine_7.result().setName("SketchLine_10")
Sketch_side.setCoincident(SketchPoint_5.coordinates(), SketchLine_7.startPoint())
Sketch_side.setVertical(SketchLine_7.result())

### Create SketchLine
SketchLine_8 = Sketch_side.addLine(4.12, 0.8099999999999999, 7.39, 0.8100000000000001)
SketchLine_8.setName("SketchLine_11")
SketchLine_8.result().setName("SketchLine_11")
Sketch_side.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
Sketch_side.setCoincident(SketchLine_2.endPoint(), SketchLine_8.endPoint())
Sketch_side.setHorizontal(SketchLine_8.result())

### Create SketchLine
SketchLine_9 = Sketch_side.addLine(4.12, 0.8099999999999999, 0, 0.1099999999999999)
SketchLine_9.setName("SketchLine_12")
SketchLine_9.result().setName("SketchLine_12")
Sketch_side.setCoincident(SketchLine_7.endPoint(), SketchLine_9.startPoint())
Sketch_side.setCoincident(SketchLine_3.startPoint(), SketchLine_9.endPoint())
Sketch_side.setHorizontalDistance(SketchPoint_5.coordinates(), SketchLine_1.endPoint(), 3.27)
Sketch_side.setHorizontalDistance(SketchLine_1.endPoint(), SketchLine_4.endPoint(), 0.2)

### Create SketchConstraintAngle
Sketch_side.setAngle(SketchLine_6.result(), SketchLine_8.result(), 45, type = "Supplementary")
model.do()
Sketch_side.changeFacesOrder([[SketchLine_4.result(), SketchLine_5.result(), SketchLine_6.result(), SketchLine_2.result()],
                           [SketchLine_1.result(), SketchLine_2.result(), SketchLine_8.result(), SketchLine_7.result()],
                           [SketchLine_1.result(), SketchLine_7.result(), SketchLine_9.result(), SketchLine_3.result()]
                          ])
model.do()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Revolution
Revolution_1_objects = [model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_7f-SketchLine_8f-SketchLine_9f-SketchLine_2r"),
                        model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_11r-SketchLine_10r"),
                        model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_1r-SketchLine_10f-SketchLine_12f-mmm_6f")]
Revolution_1 = model.addRevolution(Part_1_doc, Revolution_1_objects, model.selection("EDGE", "PartSet/Sketch_1/SketchLine_1"), 360, 0)

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, '/tmp/shaper_vtyojslp.xao', model.selection("COMPSOLID", "Revolution_1_1"), 'XAO')

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "Revolution_1_1_3/Generated_Face&PartSet/Sketch_1/mmm_6"))

### Create SketchProjection
SketchProjection_2 = Sketch_2.addProjection(model.selection("VERTEX", "[Revolution_1_1_3/Generated_Face&PartSet/Sketch_1/SketchLine_12][Revolution_1_1_3/Generated_Face&PartSet/Sketch_1/mmm_6]__cc"), False)
SketchPoint_6 = SketchProjection_2.createdFeature()

### Create SketchCircle
SketchCircle_1 = Sketch_2.addCircle(0, 0, 116.332)
Sketch_2.setCoincident(SketchPoint_6.result(), SketchCircle_1.center())
Sketch_2.setRadius(SketchCircle_1.results()[1], 116.332)
model.do()

### Create Extrusion
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchCircle_1_2f")], model.selection(), 62.738, 101.092, "Faces|Wires")

### Create Export
Export_2 = model.exportToXAO(Part_1_doc, '/tmp/shaper_9e355s3c.xao', model.selection("COMPSOLID", "Revolution_1_1"), 'XAO')

### Create Export
Export_3 = model.exportToXAO(Part_1_doc, '/tmp/shaper_3h3es3jg.xao', model.selection("SOLID", "Extrusion_1_1"), 'XAO')

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Revolution_1_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1))
Extrusion_1_1, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_1))
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

(imported, geomObj_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_vtyojslp.xao")
(imported, Revolution_1_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_9e355s3c.xao")
(imported, Extrusion_1_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_3h3es3jg.xao")
Cut_1 = geompy.MakeCutList(Extrusion_1_1, [Revolution_1_1], True)
Farfield = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Farfield, [3, 12, 10])
Rocket = geompy.CreateGroup(Revolution_1_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Rocket, [22, 4, 17, 26, 8, 13, 31])
[geomObj_2,geomObj_3,geomObj_4,geomObj_5] = geompy.SubShapeAll(Rocket, geompy.ShapeType["VERTEX"])
geomObj_6 = geompy.GetInPlace(Cut_1, Rocket, True)
[geomObj_7,geomObj_8,geomObj_9,geomObj_10] = geompy.SubShapeAll(geomObj_6, geompy.ShapeType["VERTEX"])
[geomObj_11,geomObj_12,geomObj_13,geomObj_14,geomObj_15] = geompy.SubShapeAll(geomObj_6, geompy.ShapeType["FACE"])
[geomObj_16,geomObj_17,geomObj_18,geomObj_19,geomObj_20] = geompy.SubShapeAll(geomObj_6, geompy.ShapeType["FACE"])
Rocket_1 = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Rocket_1, [15, 19, 24, 29, 34])
[Farfield, geomObj_6, Rocket_1] = geompy.GetExistingSubObjects(Cut_1, False)
[Farfield, geomObj_6, Rocket_1] = geompy.GetExistingSubObjects(Cut_1, False)
geompy.addToStudy( Revolution_1_1, 'Revolution_1_1' )
geompy.addToStudy( Extrusion_1_1, 'Extrusion_1_1' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudyInFather( Cut_1, Farfield, 'Farfield' )
geompy.addToStudyInFather( Revolution_1_1, Rocket, 'Rocket' )
geompy.addToStudyInFather( Cut_1, Rocket_1, 'Rocket' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

SubsonicMesh = smesh.Mesh(Cut_1,'SubsonicMesh')
NETGEN_1D_2D = SubsonicMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_3D = SubsonicMesh.Tetrahedron()
NETGEN_3D_Parameters_1 = NETGEN_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 30 )
NETGEN_3D_Parameters_1.SetMinSize( 0.0265181 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 2 )
NETGEN_3D_Parameters_1.SetElemSizeWeight( 4.63894e-310 )
NETGEN_3D_Parameters_1.SetCheckOverlapping( 2 )
NETGEN_3D_Parameters_1.SetCheckChartBoundary( 3 )
Farfield_1 = SubsonicMesh.GroupOnGeom(Farfield,'Farfield',SMESH.FACE)

Rocket_2 = SubsonicMesh.GroupOnGeom(Rocket_1,'Rocket',SMESH.FACE)
isDone = SubsonicMesh.Compute()
[ Farfield_1, Rocket_2 ] = SubsonicMesh.GetGroups()

Viscous_Layers_1 = NETGEN_3D.ViscousLayers(0.44,20,1.25,[ 15, 19, 24, 29, 34 ],0,smeshBuilder.SURF_OFFSET_SMOOTH)
isDone = SubsonicMesh.Compute()
[ Farfield_1, Rocket_2 ] = SubsonicMesh.GetGroups()
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 36.7567 )
NETGEN_2D_Parameters_1.SetMinSize( 0.0197206 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 3 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 21861 )
NETGEN_2D_Parameters_1.SetUseDelauney( 224 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 3 )
status = SubsonicMesh.RemoveHypothesis(NETGEN_3D_Parameters_1)
NETGEN_3D_Parameters_2 = NETGEN_3D.Parameters()
NETGEN_3D_Parameters_2.SetMaxSize( 36.7567 )
NETGEN_3D_Parameters_2.SetMinSize( 0.0197206 )
NETGEN_3D_Parameters_2.SetOptimize( 1 )
NETGEN_3D_Parameters_2.SetFineness( 4 )
NETGEN_3D_Parameters_2.SetElemSizeWeight( 4.63894e-310 )
NETGEN_3D_Parameters_2.SetCheckOverlapping( 2 )
NETGEN_3D_Parameters_2.SetCheckChartBoundary( 3 )
isDone = SubsonicMesh.Compute()
[ Farfield_1, Rocket_2 ] = SubsonicMesh.GetGroups()
Body_Fitting_Parameters_1 = smesh.CreateHypothesis('CartesianParameters3D')
Body_Fitting_Parameters_1.SetSizeThreshold( 4 )
Body_Fitting_Parameters_1.SetToAddEdges( 0 )
Body_Fitting_Parameters_1.SetGridSpacing( [ '36.7567' ], [ 0, 1 ], 0 )
Body_Fitting_Parameters_1.SetGridSpacing( [ '36.7567' ], [ 0, 1 ], 1 )
Body_Fitting_Parameters_1.SetGridSpacing( [ '36.7567' ], [ 0, 1 ], 2 )
Cartesian_3D = smesh.CreateHypothesis('Cartesian_3D')
#hyp_16.SetLength( 36.7567 ) ### not created Object
NETGEN_2D_Parameters_2 = smesh.CreateHypothesisByAverageLength( 'NETGEN_Parameters_2D', 'NETGENEngine', 36.7567, 1 )
NETGEN_1D_2D_1 = smesh.CreateHypothesis( "NETGEN_2D" )


## Set names of Mesh objects
smesh.SetName(Body_Fitting_Parameters_1, 'Body Fitting Parameters_1')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(NETGEN_2D_Parameters_2, 'NETGEN 2D Parameters_2')
smesh.SetName(Rocket_2, 'Rocket')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(Farfield_1, 'Farfield')
smesh.SetName(NETGEN_3D_Parameters_2, 'NETGEN 3D Parameters_2')
smesh.SetName(Viscous_Layers_1, 'Viscous Layers_1')
smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
smesh.SetName(Cartesian_3D, 'Cartesian_3D')
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(SubsonicMesh.GetMesh(), 'SubsonicMesh')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()


from cfdmsh import ExportSU2File

ExportSU2File(mesh=SubsonicMesh,file="subsonic")