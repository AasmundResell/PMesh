#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.9.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/asmund/dev/Trajectory-CFD/Salome_scripts/Rocket_geometries')

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
model.addParameter(Part_1_doc, "R", '7.5')
model.addParameter(Part_1_doc, "L", '98.6')
model.addParameter(Part_1_doc, "rho", '(R**2+L**2)/(2*R)', 'radius ogive angle')

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("YOZ"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 0, 98.59999999999999, 0)

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchPoint_1.result())
Sketch_1.setHorizontal(SketchLine_1.result())

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(0, 0, -22.4, 0)
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_2.startPoint())
Sketch_1.setHorizontal(SketchLine_2.result())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(-22.4, 0, -22.4, 5.5)
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setVertical(SketchLine_3.result())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(-12.1, 5.5, -22.4, 5.5)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.endPoint())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(-22.4, 5.5, -22.4, 12.5)

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(-22.4, 12.5, -12.1, 12.5)

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(-12.1, 12.5, -12.1, 5.5)
Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_4.startPoint())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_7.startPoint())
Sketch_1.setHorizontal(SketchLine_4.result())
Sketch_1.setVertical(SketchLine_5.result())
Sketch_1.setHorizontal(SketchLine_6.result())
Sketch_1.setVertical(SketchLine_7.result())

### Create SketchLine
SketchLine_8 = Sketch_1.addLine(0, 0, 0, 7.5)
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_8.startPoint())
Sketch_1.setVertical(SketchLine_8.result())
Sketch_1.setVerticalDistance(SketchLine_3.endPoint(), SketchLine_3.startPoint(), 5.5)
Sketch_1.setVerticalDistance(SketchLine_8.endPoint(), SketchAPI_Point(SketchPoint_1).coordinates(), 7.5)
Sketch_1.setVerticalDistance(SketchLine_5.endPoint(), SketchLine_3.endPoint(), 7)
Sketch_1.setLength(SketchLine_6.result(), 10.3)
Sketch_1.setLength(SketchLine_2.result(), 22.4)
Sketch_1.setLength(SketchLine_1.result(), 98.59999999999999)

### Create SketchLine
SketchLine_9 = Sketch_1.addLine(0, 7.5, -22.4, 5.5)
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_9.endPoint())

### Create SketchLine
SketchLine_10 = Sketch_1.addLine(-12.1, 12.5, 0, 7.5)
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_10.startPoint())
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_10.endPoint())

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(8.957935423574729e-15, -644.3806666666666, 0, 7.5, 98.59999999999999, 0, True)
SketchArc_1.setName("SketchArc_2")
SketchArc_1.result().setName("SketchArc_2")
SketchArc_1.results()[1].setName("SketchArc_2_2")
Sketch_1.setRadius(SketchArc_1.results()[1], "rho")
Sketch_1.setCoincident(SketchArc_1.endPoint(), SketchLine_1.endPoint())
Sketch_1.setCoincident(SketchArc_1.startPoint(), SketchLine_8.endPoint())

### Create SketchLine
SketchLine_11 = Sketch_1.addLine(-12.1, 5.5, 0, 7.5)
Sketch_1.setCoincident(SketchLine_4.startPoint(), SketchLine_11.startPoint())
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_11.endPoint())

### Create SketchLine
SketchLine_12 = Sketch_1.addLine(-18.06320850883445, 5.5, -22.4, 5.5)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_12.endPoint())

### Create SketchLine
SketchLine_13 = Sketch_1.addLine(-22.4, 5.5, -22.4, 4.510130104409561)

### Create SketchLine
SketchLine_14 = Sketch_1.addLine(-22.4, 4.510130104409561, -18.06320850883445, 4.510130104409561)

### Create SketchLine
SketchLine_15 = Sketch_1.addLine(-18.06320850883445, 4.510130104409561, -18.06320850883445, 5.5)
Sketch_1.setCoincident(SketchLine_15.endPoint(), SketchLine_12.startPoint())
Sketch_1.setCoincident(SketchLine_12.endPoint(), SketchLine_13.startPoint())
Sketch_1.setCoincident(SketchLine_13.endPoint(), SketchLine_14.startPoint())
Sketch_1.setCoincident(SketchLine_14.endPoint(), SketchLine_15.startPoint())
Sketch_1.setHorizontal(SketchLine_12.result())
Sketch_1.setVertical(SketchLine_13.result())
Sketch_1.setHorizontal(SketchLine_14.result())
Sketch_1.setVertical(SketchLine_15.result())
model.do()
Sketch_1.changeFacesOrder([[SketchLine_8.result(), SketchLine_11.result(), SketchLine_4.result(), SketchLine_15.result(), SketchLine_14.result(), SketchLine_3.result(), SketchLine_2.result()],
                           [SketchLine_1.result(), SketchArc_1.results()[1], SketchLine_8.result()],
                           [SketchLine_14.result(), SketchLine_15.result(), SketchLine_4.result(), SketchLine_3.result()],
                           [SketchLine_4.result(), SketchLine_7.result(), SketchLine_9.result(), SketchLine_4.result()],
                           [SketchLine_7.result(), SketchLine_9.result(), SketchLine_10.result()],
                           [SketchLine_9.result(), SketchLine_7.result(), SketchLine_6.result(), SketchLine_5.result()],
                           [SketchLine_7.result(), SketchLine_11.result(), SketchLine_9.result()]
                          ])
model.do()

### Create Revolution
Revolution_1_objects = [model.selection("FACE", "Sketch_1/Face-SketchLine_1r-SketchArc_2_2f-SketchLine_8r"),
                        model.selection("FACE", "Sketch_1/Face-SketchLine_8f-SketchLine_11r-SketchLine_4f-SketchLine_15r-SketchLine_14r-SketchLine_3r-SketchLine_2r"),
                        model.selection("FACE", "Sketch_1/Face-SketchLine_14f-SketchLine_15f-SketchLine_4f-SketchLine_3r"),
                        model.selection("FACE", "Sketch_1/Face-SketchLine_4r-SketchLine_7r-SketchLine_9f-SketchLine_4r"),
                        model.selection("FACE", "Sketch_1/Face-SketchLine_7f-SketchLine_11f-SketchLine_9f")]
Revolution_1 = model.addRevolution(Part_1_doc, Revolution_1_objects, model.selection("EDGE", "Sketch_1/SketchLine_1"), 360, 0)

### Create Extrusion
Extrusion_1_objects = [model.selection("FACE", "Sketch_1/Face-SketchLine_9r-SketchLine_7r-SketchLine_6r-SketchLine_5r"),
                       model.selection("FACE", "Sketch_1/Face-SketchLine_7f-SketchLine_9r-SketchLine_10r"),
                       model.selection("FACE", "Sketch_1/Face-SketchLine_7f-SketchLine_11f-SketchLine_9f"),
                       model.selection("WIRE", "Sketch_1/Face-SketchLine_4r-SketchLine_7r-SketchLine_9f-SketchLine_4r_wire"),
                       model.selection("FACE", "Sketch_1/Face-SketchLine_14f-SketchLine_15f-SketchLine_4f-SketchLine_3r")]
Extrusion_1 = model.addExtrusion(Part_1_doc, Extrusion_1_objects, model.selection(), 0.51, 0.51, "Faces|Wires")

### Create Fuse
Fuse_1_objects_1 = [model.selection("SOLID", "Extrusion_1_1_1"),
                    model.selection("SOLID", "Extrusion_1_1_4"),
                    model.selection("SOLID", "Extrusion_1_1_5")]
Fuse_1 = model.addFuse(Part_1_doc, Fuse_1_objects_1, keepSubResults = True)

### Create Fuse
Fuse_2_objects_1 = [model.selection("SOLID", "Fuse_1_1_3"),
                    model.selection("SOLID", "Fuse_1_1_1"),
                    model.selection("SOLID", "Fuse_1_1_2")]
Fuse_2 = model.addFuse(Part_1_doc, Fuse_2_objects_1, keepSubResults = True)

### Create AngularCopy
AngularCopy_1 = model.addMultiRotation(Part_1_doc, [model.selection("SOLID", "Fuse_2_1")], model.selection("EDGE", "Sketch_1/SketchLine_1"), 4, keepSubResults = True)

### Create Fuse
Fuse_3_objects_1 = [model.selection("SOLID", "Revolution_1_1_4"),
                    model.selection("SOLID", "Revolution_1_1_5"),
                    model.selection("SOLID", "AngularCopy_1_1_1"),
                    model.selection("SOLID", "AngularCopy_1_1_4"),
                    model.selection("SOLID", "AngularCopy_1_1_2"),
                    model.selection("SOLID", "AngularCopy_1_1_3")]
Fuse_3 = model.addFuse(Part_1_doc, Fuse_3_objects_1, keepSubResults = True)

### Create Fuse
Fuse_4 = model.addFuse(Part_1_doc, [model.selection("SOLID", "Fuse_3_1_4"), model.selection("SOLID", "Fuse_3_1_1")], keepSubResults = True)

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.standardPlane("XOZ"))

### Create SketchProjection
SketchProjection_2 = Sketch_2.addProjection(model.selection("VERTEX", "[Fuse_3_1_2/Modified_Face&Sketch_1/SketchLine_8][Fuse_3_1_2/Modified_Face&Sketch_1/SketchLine_11&new_weak_name_1]__cc"), False)
SketchPoint_2 = SketchProjection_2.createdFeature()

### Create SketchCircle
SketchCircle_1 = Sketch_2.addCircle(0, 0, 400)
Sketch_2.setCoincident(SketchPoint_2.result(), SketchCircle_1.center())
Sketch_2.setRadius(SketchCircle_1.results()[1], 400)
model.do()

### Create Extrusion
Extrusion_2 = model.addExtrusion(Part_1_doc, [model.selection("COMPOUND", "Sketch_2")], model.selection(), 300, 300, "Faces|Wires")

### Create Shell
Shell_1 = model.addShell(Part_1_doc, [model.selection("FACE", "Extrusion_2_1/Generated_Face&Sketch_2/SketchCircle_1_2")])
Shell_1.result().setTransparency(0.72)

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
# This shape does not exist among the SHAPER results; if it is referenced by SMESH, this may cause an error
# Revolution_1_1, = SHAPERSTUDY.shape("dead01_8:64")
# This shape does not exist among the SHAPER results; if it is referenced by SMESH, this may cause an error
# AngularCopy_1_1, = SHAPERSTUDY.shape("dead02_8:68")
Fuse_4_1, = SHAPERSTUDY.shape(model.featureStringId(Fuse_4))
Shell_1_1, = SHAPERSTUDY.shape(model.featureStringId(Shell_1))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
