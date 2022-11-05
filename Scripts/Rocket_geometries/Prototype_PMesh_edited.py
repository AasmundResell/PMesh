#!/usr/bin/env python

###
# This file is generated automatically by SALOME v9.9.0 with dump python functionality
###

import SALOMEDS
import math
from salome.geom import geomBuilder
import GEOM
import SHAPERSTUDY
from salome.shaper import model
from SketchAPI import *
import salome_notebook  
import sys
import salome

salome.salome_init()
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/asmund/dev/PMesh/Scripts/Rocket_geometries')

###
# SHAPER component
###


model.begin()
partSet = model.moduleDocument()

# Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
model.addParameter(Part_1_doc, "l", '30')
model.addParameter(Part_1_doc, "r", '20')
model.addParameter(Part_1_doc, "l_b", '110')

l = 30
r = 20
l_b = 110

# Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

# Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(
    model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()

# Create SketchLine
SketchLine_1 = Sketch_1.addLine(l, 0, l, r)
SketchLine_1.setName("hehehei2")
SketchLine_1.result().setName("hehehei2")
Sketch_1.setVertical(SketchLine_1.result())

# Create SketchLine
SketchLine_2 = Sketch_1.addLine(l, r, 0, 0)
SketchLine_2.setName("SketchLine_3")
SketchLine_2.result().setName("SketchLine_3")
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())

# Create SketchLine
SketchLine_3 = Sketch_1.addLine(l, r, l_b + l, r)
SketchLine_3.setName("SketchLine_4")
SketchLine_3.result().setName("SketchLine_4")
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_3.startPoint())
Sketch_1.setHorizontal(SketchLine_3.result())

# Create SketchLine
SketchLine_4 = Sketch_1.addLine(l_b + l, r, l_b + l, 0)
SketchLine_4.setName("SketchLine_5")
SketchLine_4.result().setName("SketchLine_5")
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setVertical(SketchLine_4.result())

# Create SketchLine
SketchLine_5 = Sketch_1.addLine(l, 0, 0, 0)
SketchLine_5.setName("SketchLine_8")
SketchLine_5.result().setName("SketchLine_8")
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_5.startPoint())
Sketch_1.setCoincident(SketchAPI_Point(
    SketchPoint_1).coordinates(), SketchLine_5.endPoint())
Sketch_1.setHorizontal(SketchLine_5.result())
Sketch_1.setHorizontalDistance(SketchAPI_Point(
    SketchPoint_1).coordinates(), SketchLine_5.startPoint(), "l")
Sketch_1.setVerticalDistance(
    SketchLine_5.startPoint(), SketchLine_2.startPoint(), "r")
Sketch_1.setHorizontalDistance(
    SketchLine_2.startPoint(), SketchLine_3.endPoint(), "l_b")

# Create SketchLine
SketchLine_6 = Sketch_1.addLine(l_b + l, 0, l, 0)
SketchLine_6.setName("SketchLine_6")
SketchLine_6.result().setName("SketchLine_6")
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_6.endPoint())
Sketch_1.setHorizontal(SketchLine_6.result())
model.do()

# Create Revolution
Revolution_1 = model.addRevolution(Part_1_doc, [model.selection(
    "FACE", "Sketch_1/Face-hehehei2f-SketchLine_3f-SketchLine_8r")], model.selection("EDGE", "Sketch_1/SketchLine_8"), 360, 0)

# Create Revolution
Revolution_2 = model.addRevolution(Part_1_doc, [model.selection(
    "FACE", "Sketch_1/Face-SketchLine_6r-SketchLine_5r-SketchLine_4r-hehehei2r")], model.selection("EDGE", "PartSet/OX"), 360, 0)

# Create Fuse
Fuse_1 = model.addFuse(Part_1_doc, [model.selection(
    "SOLID", "Revolution_1_1"), model.selection("SOLID", "Revolution_2_1")], keepSubResults=True)

# Create Export
Export_1 = model.exportToXAO(
    Part_1_doc, '/tmp/shaper_dltfnwem.xao', model.selection("SOLID", "Fuse_1_1"), 'XAO')

model.end()

###
# SHAPERSTUDY component
###

model.publishToShaperStudy()
# This shape does not exist among the SHAPER results; if it is referenced by SMESH, this may cause an error
# Revolution_1_1, = SHAPERSTUDY.shape("dead01_8:55")
# This shape does not exist among the SHAPER results; if it is referenced by SMESH, this may cause an error
# Revolution_2_1, = SHAPERSTUDY.shape("dead02_8:56")
Fuse_1_1, = SHAPERSTUDY.shape(model.featureStringId(Fuse_1))
###
# GEOM component
###


geompy = geomBuilder.New()

(imported, Fuse_1_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_dltfnwem.xao")
Rocket = geompy.CreateGroup(Fuse_1_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Rocket, [12, 3, 7])
geompy.addToStudy(Fuse_1_1, 'Fuse_1_1')
geompy.addToStudyInFather(Fuse_1_1, Rocket, 'Rocket')


if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()
