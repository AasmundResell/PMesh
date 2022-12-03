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
SketchLine_1 = Sketch_1.addLine(0, 0, 0.7583546962660087, 0)
SketchLine_1.setName("baseAxialLine_0")
SketchLine_1.result().setName("baseAxialLine_0")

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(0.7583546962660087, 0, 0.7583546962660087, 0.127)
SketchLine_2.setName("baseAxialLine_0")
SketchLine_2.result().setName("baseRadialLine_0")
Sketch_1.setHorizontal(SketchLine_1.result())
Sketch_1.setVertical(SketchLine_2.result())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(0.002540000000000001, 0, 0.001928375483948882, 0.002465261740944608, 0, 0, False)
Sketch_1.setCoincident(SketchArc_1.endPoint(), SketchLine_1.result())

### Create SketchArc
SketchArc_2 = Sketch_1.addArc(1.156675461788461, -4.651948905162474, 0.001928375483948882, 0.002465261740944608, 0.7583546962660087, 0.127, True)
Sketch_1.setCoincident(SketchLine_2.result(), SketchArc_2.endPoint())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(0.7583546962660087, 0, 1.266354696266009, 0)
SketchLine_3.setName("baseAxialLine_1")
SketchLine_3.result().setName("baseAxialLine_1")

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(1.266354696266009, 0, 1.266354696266009, 0.127)
SketchLine_4.setName("baseAxialLine_1")
SketchLine_4.result().setName("baseRadialLine_1")
Sketch_1.setHorizontal(SketchLine_3.result())
Sketch_1.setVertical(SketchLine_4.result())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(0.7583546962660087, 0.127, 1.266354696266009, 0.127)
SketchLine_5.setName("upperContourLine_1")
SketchLine_5.result().setName("upperContourLine_1")
Sketch_1.setHorizontal(SketchLine_5.result())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.endPoint())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(1.266354696266009, 0, 1.516036696266009, 0)
SketchLine_6.setName("baseAxialLine_2")
SketchLine_6.result().setName("baseAxialLine_2")

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(1.516036696266009, 0, 1.516036696266009, 0.096342905358)
SketchLine_7.setName("baseAxialLine_2")
SketchLine_7.result().setName("baseRadialLine_2")
Sketch_1.setHorizontal(SketchLine_6.result())
Sketch_1.setVertical(SketchLine_7.result())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_7.startPoint())

### Create SketchLine
SketchLine_8 = Sketch_1.addLine(1.266354696266009, 0.127, 1.516036696266009, 0.096342905358)
SketchLine_8.setName("upperContourLine_2")
SketchLine_8.result().setName("upperContourLine_2")
Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_8.endPoint())
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchPoint_1.result())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_5.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_8.startPoint())
model.do()

### Create Revolution
Revolution_1 = model.addRevolution(Part_1_doc, [model.selection("EDGE", "Sketch_1/SketchArc_1_2"), model.selection("EDGE", "Sketch_1/SketchArc_2_2")], model.selection("EDGE", "Sketch_1/baseAxialLine_0"), 360, 0)

### Create Revolution
Revolution_2 = model.addRevolution(Part_1_doc, [model.selection("EDGE", "Sketch_1/upperContourLine_1")], model.selection("EDGE", "Sketch_1/baseAxialLine_1"), 360, 0)

### Create Revolution
Revolution_3 = model.addRevolution(Part_1_doc, [model.selection("EDGE", "Sketch_1/upperContourLine_2"), model.selection("EDGE", "Sketch_1/baseRadialLine_2")], model.selection("EDGE", "Sketch_1/baseAxialLine_2"), 360, 0)

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, '/tmp/shaper_start_0.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')

### Create Export
Export_2 = model.exportToXAO(Part_1_doc, '/tmp/shaper_SecantOgiveNose.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')

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
(imported, Revolution_1_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_SecantOgiveNose.xao")
(imported, Revolution_2_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_middle_1.xao")
(imported, Revolution_3_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_middle_2.xao")
(imported, Revolution_3_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_rear_2.xao")
start_0 = geompy.CreateGroup(Revolution_1_1, geompy.ShapeType["FACE"])
geompy.UnionList(start_0, [Revolution_1_1])
SecantOgiveNose = geompy.CreateGroup(Revolution_1_2, geompy.ShapeType["FACE"])
geompy.UnionList(SecantOgiveNose, [Revolution_1_2])
middle_1 = geompy.CreateGroup(Revolution_2_1, geompy.ShapeType["FACE"])
geompy.UnionList(middle_1, [Revolution_2_1])
middle_2 = geompy.CreateGroup(Revolution_3_1, geompy.ShapeType["FACE"])
geompy.UnionList(middle_2, [Revolution_3_1])
rear_2 = geompy.CreateGroup(Revolution_3_2, geompy.ShapeType["FACE"])
geompy.UnionList(rear_2, [Revolution_3_2])
ShellProjectile = geompy.MakeShell([Revolution_1_1, Revolution_1_2, Revolution_2_1, Revolution_3_1, Revolution_3_2])
Projectile = geompy.MakeSolid([ShellProjectile])
VertexCylinder = geompy.MakeVertex(-30.48, 0, 0)
[geomObj_1] = geompy.SubShapeAll(VertexCylinder, geompy.ShapeType["VERTEX"])
geomObj_2 = geompy.MakeVectorDXDYDZ(1, 0, 0)
Cylinder = geompy.MakeCylinder(VertexCylinder, geomObj_2, 30.48, 62.47603669626601)
[geomObj_3,geomObj_4] = geompy.SubShapeAll(Cylinder, geompy.ShapeType["VERTEX"])
[geomObj_5,geomObj_6,geomObj_7] = geompy.SubShapeAll(Cylinder, geompy.ShapeType["FACE"])
[geomObj_8,geomObj_9,geomObj_10] = geompy.SubShapeAll(Cylinder, geompy.ShapeType["FACE"])
Domain = geompy.MakeCutList(Cylinder, [Projectile], True)
geomObj_11 = geompy.CreateGroup(Domain, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_11, [3, 10, 12])
geomObj_12 = geompy.CreateGroup(Domain, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_12, [15, 22, 27, 32])
geomObj_13 = geompy.GetInPlace(Domain, Cylinder, True)
[geomObj_14,geomObj_15,geomObj_16,geomObj_17,geomObj_18,geomObj_19,geomObj_20] = geompy.SubShapeAll(geomObj_13, geompy.ShapeType["VERTEX"])
Farfield = geompy.CreateGroup(Domain, geompy.ShapeType["FACE"])
geompy.UnionIDs(Farfield, [3, 10, 12])
Projectile_1 = geompy.CreateGroup(Domain, geompy.ShapeType["FACE"])
geompy.UnionIDs(Projectile_1, [15, 22, 27, 32, 37])
geompy.addToStudy( Revolution_1_1, 'Revolution_1_1' )
geompy.addToStudy( Revolution_1_2, 'Revolution_1_2' )
geompy.addToStudy( Revolution_2_1, 'Revolution_2_1' )
geompy.addToStudy( Revolution_3_1, 'Revolution_3_1' )
geompy.addToStudy( Revolution_3_2, 'Revolution_3_2' )
geompy.addToStudyInFather( Revolution_1_1, start_0, 'start_0' )
geompy.addToStudyInFather( Revolution_1_2, SecantOgiveNose, 'SecantOgiveNose' )
geompy.addToStudyInFather( Revolution_2_1, middle_1, 'middle_1' )
geompy.addToStudyInFather( Revolution_3_1, middle_2, 'middle_2' )
geompy.addToStudyInFather( Revolution_3_2, rear_2, 'rear_2' )
geompy.addToStudy( ShellProjectile, 'ShellProjectile' )
geompy.addToStudy( Projectile, 'Projectile' )
geompy.addToStudy( VertexCylinder, 'VertexCylinder' )
geompy.addToStudy( Cylinder, 'Cylinder' )
geompy.addToStudy( Domain, 'Domain' )
geompy.addToStudyInFather( Domain, Farfield, 'Farfield' )
geompy.addToStudyInFather( Domain, Projectile_1, 'Projectile' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
