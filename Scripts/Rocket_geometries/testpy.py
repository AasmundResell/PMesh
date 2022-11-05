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
Extrusion_2 = model.addExtrusion(Part_1_doc, [model.selection("COMPOUND", "Sketch_2")], model.selection(), 300, 500, "Faces|Wires")

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, '/tmp/shaper_clnfrcq6.xao', model.selection("COMPSOLID", "Fuse_4_1"), 'XAO')

### Create Export
Export_2 = model.exportToXAO(Part_1_doc, '/tmp/shaper_0_etlge0.xao', model.selection("SOLID", "Extrusion_2_1"), 'XAO')

### Create Export
Export_3 = model.exportToXAO(Part_1_doc, '/tmp/shaper_leuddro7.xao', model.selection("COMPSOLID", "Fuse_4_1"), 'XAO')

### Create Export
Export_4 = model.exportToXAO(Part_1_doc, '/tmp/shaper_q_r8mmy3.xao', model.selection("SOLID", "Extrusion_2_1"), 'XAO')

### Create Export
Export_5 = model.exportToXAO(Part_1_doc, '/tmp/shaper_8yf1a66n.xao', model.selection("COMPSOLID", "Fuse_4_1"), 'XAO')

### Create Export
Export_6 = model.exportToXAO(Part_1_doc, '/tmp/shaper_jdinnwgb.xao', model.selection("SOLID", "Extrusion_2_1"), 'XAO')

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Fuse_4_1, = SHAPERSTUDY.shape(model.featureStringId(Fuse_4))
# This shape does not exist among the SHAPER results; if it is referenced by SMESH, this may cause an error
# Shell_1_1, = SHAPERSTUDY.shape("dead02_8:79")
# This shape does not exist among the SHAPER results; if it is referenced by SMESH, this may cause an error
# Extrusion_2_1, = SHAPERSTUDY.shape("dead03_8:78")
# This shape does not exist among the SHAPER results; if it is referenced by SMESH, this may cause an error
# Solid_1_1, = SHAPERSTUDY.shape("dead04_8:80")
Extrusion_2_1_1, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_2))
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
(imported, Fuse_4_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_clnfrcq6.xao")
[geomObj_1,geomObj_2,geomObj_3,geomObj_4,geomObj_5,geomObj_6,geomObj_7,geomObj_8,geomObj_9,geomObj_10,geomObj_11,geomObj_12,geomObj_13,geomObj_14,geomObj_15,geomObj_16,geomObj_17,geomObj_18,geomObj_19,geomObj_20,geomObj_21,geomObj_22,geomObj_23,geomObj_24,geomObj_25,geomObj_26,geomObj_27,geomObj_28,geomObj_29,geomObj_30,geomObj_31,geomObj_32,geomObj_33,geomObj_34,geomObj_35,geomObj_36,geomObj_37,geomObj_38,geomObj_39,geomObj_40,geomObj_41,geomObj_42,geomObj_43,geomObj_44,geomObj_45,geomObj_46,geomObj_47,geomObj_48,geomObj_49,geomObj_50,geomObj_51,geomObj_52,geomObj_53,geomObj_54,geomObj_55,geomObj_56,geomObj_57,geomObj_58,geomObj_59,geomObj_60,geomObj_61,geomObj_62,geomObj_63,geomObj_64,geomObj_65,geomObj_66,geomObj_67,geomObj_68,geomObj_69,geomObj_70,geomObj_71,geomObj_72,geomObj_73,geomObj_74,geomObj_75,geomObj_76,geomObj_77,geomObj_78,geomObj_79,geomObj_80,geomObj_81,geomObj_82,geomObj_83,geomObj_84,geomObj_85,geomObj_86,geomObj_87,geomObj_88,geomObj_89,geomObj_90,geomObj_91,geomObj_92,geomObj_93,geomObj_94,geomObj_95,geomObj_96,geomObj_97,geomObj_98,geomObj_99] = geompy.SubShapeAll(Fuse_4_1, geompy.ShapeType["VERTEX"])
(imported, Extrusion_2_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_0_etlge0.xao")
(imported, geomObj_100, [], [], []) = geompy.ImportXAO("/tmp/shaper_leuddro7.xao")
(imported, geomObj_101, [], [], []) = geompy.ImportXAO("/tmp/shaper_q_r8mmy3.xao")
(imported, geomObj_102, [], [], []) = geompy.ImportXAO("/tmp/shaper_8yf1a66n.xao")
(imported, geomObj_103, [], [], []) = geompy.ImportXAO("/tmp/shaper_jdinnwgb.xao")
Farfield = geompy.CreateGroup(Extrusion_2_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Farfield, [12, 3, 10])
Rocket = geompy.CreateGroup(Fuse_4_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Rocket, [140, 498, 347, 80, 135, 226, 463, 256, 220, 170, 161, 187, 214, 293, 247, 310, 177, 240, 393, 277, 199, 232, 335, 398, 437, 361, 340, 501, 466, 485, 406, 488, 449, 352, 382, 305, 495, 316, 4, 14, 21, 26, 31, 34, 45, 54, 63, 70, 75, 84, 91, 96, 101, 106, 113, 120, 125, 130, 147, 154, 180, 194, 204, 209, 223, 235, 259, 264, 267, 269, 272, 283, 290, 300, 313, 325, 327, 332, 355, 358, 372, 377, 390, 403, 411, 414, 416, 419, 427, 434, 444, 452, 455, 458, 469, 474, 477, 479, 482])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Fuse_4_1, 'Fuse_4_1' )
geompy.addToStudy( Extrusion_2_1, 'Extrusion_2_1' )
geompy.addToStudyInFather( Extrusion_2_1, Farfield, 'Farfield' )
geompy.addToStudyInFather( Fuse_4_1, Rocket, 'Rocket' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
