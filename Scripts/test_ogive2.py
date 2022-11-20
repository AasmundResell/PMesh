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

from SketchAPI import *

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 0, 10.3, 0)

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchPoint_1.result())
Sketch_1.setHorizontal(SketchLine_1.result())

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(10.3, 0, 10.3, 1.1)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setVertical(SketchLine_2.result())

### Create SketchPoint
SketchPoint_2 = Sketch_1.addPoint(10.3, 1.1)
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchPoint_2.coordinates())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(0, 0, 2.5, 0)
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_3.startPoint())
Sketch_1.setHorizontal(SketchLine_3.result())
Sketch_1.setHorizontalDistance(SketchAPI_Point(SketchPoint_1).coordinates(), SketchLine_1.endPoint(), 10.3)
Sketch_1.setHorizontalDistance(SketchLine_3.endPoint(), SketchAPI_Point(SketchPoint_1).coordinates(), 2.5)
Sketch_1.setVerticalDistance(SketchLine_2.endPoint(), SketchLine_1.endPoint(), 1.1)

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(2.5, 0, 2.5, 0.4723)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setVertical(SketchLine_4.result())
Sketch_1.setVerticalDistance(SketchLine_3.endPoint(), SketchLine_4.endPoint(), 0.4723)

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(2.5, 0, 6.4, 0)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_5.startPoint())
Sketch_1.setHorizontal(SketchLine_5.result())
Sketch_1.setHorizontalDistance(SketchLine_3.endPoint(), SketchLine_5.endPoint(), 3.9)

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(6.4, 0, 6.4, 0.9428)
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())
Sketch_1.setVertical(SketchLine_6.result())
Sketch_1.setVerticalDistance(SketchLine_5.endPoint(), SketchLine_6.endPoint(), 0.9428)

### Create SketchPoint
SketchPoint_3 = Sketch_1.addPoint(2.5, 0.4723)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchPoint_3.coordinates())

### Create SketchPoint
SketchPoint_4 = Sketch_1.addPoint(6.4, 0.9428)
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchPoint_4.coordinates())

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(10.3, -47.6723, 2.5, 0.4723, 10.3, 1.1, True)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchArc_1.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchArc_1.endPoint())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchArc_1.results()[1])
model.do()

### Create Revolution
Revolution_1_objects = [model.selection("EDGE", "Sketch_1/SketchLine_4"),
                        model.selection("EDGE", "Sketch_1/SketchArc_1_2"),
                        model.selection("EDGE", "Sketch_1/SketchLine_2")]
Revolution_1 = model.addRevolution(Part_1_doc, Revolution_1_objects, model.selection("EDGE", "Sketch_1/SketchLine_1"), 360, 0)

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Revolution_1_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1))
Revolution_1_2, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1, 1))
Revolution_1_3, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1, 2))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
