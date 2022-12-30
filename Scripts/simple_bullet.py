#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.9.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/asmund/dev/PMesh/Scripts')

###
### SHAPER component
###

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 0, 41.2, 0)
SketchLine_1.setName("baseAxialLine_0")
SketchLine_1.result().setName("baseAxialLine_0")

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(41.2, 0, 41.2, 8.1)
SketchLine_2.setName("baseAxialLine_0")
SketchLine_2.result().setName("baseRadialLine_0")
Sketch_1.setHorizontal(SketchLine_1.result())
Sketch_1.setVertical(SketchLine_2.result())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(41.2, 8.1, 0, 1.1)
SketchLine_3.setName("noseConicLine")
SketchLine_3.result().setName("noseConicLine")
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(0, 0, 0, 1.1)
SketchLine_4.setName("noseFrontLine")
SketchLine_4.result().setName("noseFrontLine")
Sketch_1.setVertical(SketchLine_4.result())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_3.endPoint())
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_4.startPoint())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(41.2, 0, 73.90000000000001, 0)
SketchLine_5.setName("baseAxialLine_1")
SketchLine_5.result().setName("baseAxialLine_1")

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(73.90000000000001, 0, 73.90000000000001, 8.1)
SketchLine_6.setName("baseAxialLine_1")
SketchLine_6.result().setName("baseRadialLine_1")
Sketch_1.setHorizontal(SketchLine_5.result())
Sketch_1.setVertical(SketchLine_6.result())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(41.2, 8.1, 73.90000000000001, 8.1)
SketchLine_7.setName("upperContourLine_1")
SketchLine_7.result().setName("upperContourLine_1")
Sketch_1.setHorizontal(SketchLine_7.result())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_7.endPoint())

### Create SketchLine
SketchLine_8 = Sketch_1.addLine(73.90000000000001, 0, 75.90000000000001, 0)
SketchLine_8.setName("baseAxialLine_2")
SketchLine_8.result().setName("baseAxialLine_2")

### Create SketchLine
SketchLine_9 = Sketch_1.addLine(75.90000000000001, 0, 75.90000000000001, 6.1)
SketchLine_9.setName("baseAxialLine_2")
SketchLine_9.result().setName("baseRadialLine_2")
Sketch_1.setHorizontal(SketchLine_8.result())
Sketch_1.setVertical(SketchLine_9.result())
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())

### Create SketchLine
SketchLine_10 = Sketch_1.addLine(73.90000000000001, 8.1, 75.90000000000001, 6.1)
SketchLine_10.setName("upperContourLine_2")
SketchLine_10.result().setName("upperContourLine_2")
Sketch_1.setCoincident(SketchLine_9.endPoint(), SketchLine_10.endPoint())
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchPoint_1.result())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_5.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_7.startPoint())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_8.startPoint())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_10.startPoint())
model.do()

### Create Revolution
Revolution_1 = model.addRevolution(Part_1_doc, [model.selection("EDGE", "Sketch_1/noseFrontLine"), model.selection("EDGE", "Sketch_1/noseConicLine")], model.selection("EDGE", "Sketch_1/baseAxialLine_0"), 360, 0)

### Create Revolution
Revolution_2 = model.addRevolution(Part_1_doc, [model.selection("EDGE", "Sketch_1/upperContourLine_1")], model.selection("EDGE", "Sketch_1/baseAxialLine_1"), 360, 0)

### Create Revolution
Revolution_3 = model.addRevolution(Part_1_doc, [model.selection("EDGE", "Sketch_1/upperContourLine_2"), model.selection("EDGE", "Sketch_1/baseRadialLine_2")], model.selection("EDGE", "Sketch_1/baseAxialLine_2"), 360, 0)

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, '/tmp/shaper_start_0.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')

### Create Export
Export_2 = model.exportToXAO(Part_1_doc, '/tmp/shaper_ConicNose.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')

### Create Export
Export_3 = model.exportToXAO(Part_1_doc, '/tmp/shaper_middle_1.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')

### Create Export
Export_4 = model.exportToXAO(Part_1_doc, '/tmp/shaper_middle_2.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')

### Create Export
Export_5 = model.exportToXAO(Part_1_doc, '/tmp/shaper_rear_2.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Revolution_1_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1))
Revolution_1_2, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1, 1))
Revolution_2_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_2))
Revolution_3_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_3))
Revolution_3_2, = SHAPERSTUDY.shape(model.featureStringId(Revolution_3, 1))
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

(imported, Revolution_1_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_start_0.xao")
(imported, Revolution_1_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_ConicNose.xao")
(imported, Revolution_2_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_middle_1.xao")
(imported, Revolution_3_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_middle_2.xao")
(imported, Revolution_3_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_rear_2.xao")
start_0 = geompy.CreateGroup(Revolution_1_1, geompy.ShapeType["FACE"])
geompy.UnionList(start_0, [Revolution_1_1])
ConicNose = geompy.CreateGroup(Revolution_1_2, geompy.ShapeType["FACE"])
geompy.UnionList(ConicNose, [Revolution_1_2])
middle_1 = geompy.CreateGroup(Revolution_2_1, geompy.ShapeType["FACE"])
geompy.UnionList(middle_1, [Revolution_2_1])
middle_2 = geompy.CreateGroup(Revolution_3_1, geompy.ShapeType["FACE"])
geompy.UnionList(middle_2, [Revolution_3_1])
rear_2 = geompy.CreateGroup(Revolution_3_2, geompy.ShapeType["FACE"])
geompy.UnionList(rear_2, [Revolution_3_2])
ShellProjectile = geompy.MakeShell([Revolution_1_1, Revolution_1_2, Revolution_2_1, Revolution_3_1, Revolution_3_2])
Projectile = geompy.MakeSolid([ShellProjectile])
VertexCylinder = geompy.MakeVertex(-644, 0, 0)
geomObj_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
Outer_domain = geompy.MakeCylinder(VertexCylinder, geomObj_1, 741, 919.9)
geomObj_2 = geompy.MakeVertex(-25.3, 0, 0)
geomObj_3 = geompy.MakeVectorDXDYDZ(1, 0, 0)
innerCylinder = geompy.MakeCylinder(geomObj_2, geomObj_3, 24.3, 139.15)
innerDomain = geompy.MakeCutList(innerCylinder, [Projectile], True)
Vector_1 = geompy.MakeVectorDXDYDZ(0, 0, 1)
Plane_1 = geompy.MakePlane(VertexCylinder, Vector_1, 2000)
Partition_1 = geompy.MakePartitionNonSelfIntersectedShape([Outer_domain, innerDomain], [Plane_1], [], [], geompy.ShapeType["SOLID"], 0, [], 1, True)
[Solid_1,Solid_2,Solid_3,Solid_4,Solid_5,Solid_6] = geompy.ExtractShapes(Partition_1, geompy.ShapeType["SOLID"], True)
projectile = geompy.CreateGroup(Solid_3, geompy.ShapeType["FACE"])
geompy.UnionIDs(projectile, [42, 38, 44, 47, 50])
farfield = geompy.CreateGroup(Solid_1, geompy.ShapeType["FACE"])

faceIDs = geompy.SubShapeAllIDs(Solid_1, geompy.ShapeType["FACE"])
print(faceIDs)

faceIDs = geompy.GetFreeFacesIDs(Solid_1)
print(faceIDs)
faceIDs = geompy.SubShapeAllIDs(Solid_3, geompy.ShapeType["FACE"])
print(faceIDs)
faceIDs = geompy.SubShapeAllIDs(Solid_5, geompy.ShapeType["FACE"])
print(faceIDs)
shared = geompy.GetSharedShapes(Solid_1,Solid_3,geompy.ShapeType["FACE"])

print("shared:", shared)

geompy.UnionIDs(farfield, [13, 3, 28])
geompy.addToStudy( Revolution_1_1, 'Revolution_1_1' )
geompy.addToStudy( Revolution_1_2, 'Revolution_1_2' )
geompy.addToStudy( Revolution_2_1, 'Revolution_2_1' )
geompy.addToStudy( Revolution_3_1, 'Revolution_3_1' )
geompy.addToStudy( Revolution_3_2, 'Revolution_3_2' )
geompy.addToStudyInFather( Revolution_1_1, start_0, 'start_0' )
geompy.addToStudyInFather( Revolution_1_2, ConicNose, 'ConicNose' )
geompy.addToStudyInFather( Revolution_2_1, middle_1, 'middle_1' )
geompy.addToStudyInFather( Revolution_3_1, middle_2, 'middle_2' )
geompy.addToStudyInFather( Revolution_3_2, rear_2, 'rear_2' )
geompy.addToStudy( ShellProjectile, 'ShellProjectile' )
geompy.addToStudy( Projectile, 'Projectile' )
geompy.addToStudy( VertexCylinder, 'VertexCylinder' )
geompy.addToStudy( Outer_domain, 'Outer_domain' )
geompy.addToStudy( innerCylinder, 'innerCylinder' )
geompy.addToStudy( innerDomain, 'innerDomain' )
geompy.addToStudy( Vector_1, 'Vector_1' )
geompy.addToStudy( Plane_1, 'Plane_1' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, Solid_1, 'Solid_1' )
geompy.addToStudyInFather( Partition_1, Solid_2, 'Solid_2' )
geompy.addToStudyInFather( Partition_1, Solid_3, 'Solid_3' )
geompy.addToStudyInFather( Partition_1, Solid_4, 'Solid_4' )
geompy.addToStudyInFather( Partition_1, Solid_5, 'Solid_5' )
geompy.addToStudyInFather( Partition_1, Solid_6, 'Solid_6' )
geompy.addToStudyInFather( Solid_3, projectile, 'projectile' )
geompy.addToStudyInFather( Solid_1, farfield, 'farfield' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
