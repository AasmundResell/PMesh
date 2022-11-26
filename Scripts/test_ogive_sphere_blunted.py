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
offset = 2.573850226823641
### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 0, 12-offset, 0)


### Create SketchLine
SketchLine_2 = Sketch_1.addLine(12-offset, 0, 12-offset, 2)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setHorizontal(SketchLine_1.result())
Sketch_1.setVertical(SketchLine_2.result())
Sketch_1.setVerticalDistance(SketchLine_1.endPoint(), SketchLine_2.endPoint(), 2)

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(3.339790510902075-offset, 0, 3.339790510902075-offset, 0.9722222222222222)
SketchLine_3.setName("SketchLine_5")
SketchLine_3.result().setName("SketchLine_5")
Sketch_1.setVertical(SketchLine_3.result())

### Create SketchPoint
SketchPoint_2 = Sketch_1.addPoint(3.339790510902075-offset, 0.9722222222222222)
SketchPoint_2.setName("SketchPoint_4")
SketchPoint_2.result().setName("SketchPoint_4")
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchPoint_2.coordinates())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(12-offset, 0, 12-offset, -35)
SketchLine_4.setName("SketchLine_6")
SketchLine_4.result().setName("SketchLine_6")
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_4.startPoint())
Sketch_1.setVertical(SketchLine_4.result())
Sketch_1.setVerticalDistance(SketchLine_4.startPoint(), SketchLine_4.endPoint(), 35)

### Create SketchPoint
SketchPoint_4 = Sketch_1.addPoint(3.339790510902075-offset, 0)
SketchPoint_4.setName("SketchPoint_6")
SketchPoint_4.result().setName("SketchPoint_6")
Sketch_1.setCoincident(SketchLine_3.startPoint(), SketchPoint_4.coordinates())

### Create SketchPoint
SketchPoint_5 = Sketch_1.addPoint(12-offset, 2)
SketchPoint_5.setName("SketchPoint_8")
SketchPoint_5.result().setName("SketchPoint_8")
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchPoint_5.coordinates())
Sketch_1.setVerticalDistance(SketchPoint_4.coordinates(), SketchLine_3.endPoint(), 0.9722222222222222)

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(12-offset, -35, 3.339790510902075-offset, 0.9722222222222222, 12-offset, 2, True)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchArc_1.center())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchArc_1.startPoint())
Sketch_1.setCoincident(SketchLine_2.result(), SketchArc_1.endPoint())

### Create SketchArc
SketchArc_2 = Sketch_1.addArc(3.573850226823641-offset, 0, 3.339790510902075-offset, 0.9722222222222222, 0, 0, False)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchArc_2.startPoint())
Sketch_1.setCoincident(SketchArc_2.endPoint(), SketchLine_1.result())
model.do()

### Create Revolution
Revolution_1_objects = [model.selection("EDGE", "Sketch_1/SketchArc_2_2"),
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
