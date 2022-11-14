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

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 0, 30, 0)

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchPoint_1.result())
Sketch_1.setHorizontal(SketchLine_1.result())

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(30, 0, 30, 20)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setVertical(SketchLine_2.result())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(30, 20, 0, 0)
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_3.endPoint())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(30, 0, 80, 0)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_4.startPoint())
Sketch_1.setHorizontal(SketchLine_4.result())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(80, 0, 80, 20)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())
Sketch_1.setVertical(SketchLine_5.result())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(30, 20, 80, 20)
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.endPoint())
Sketch_1.setHorizontal(SketchLine_6.result())

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(80, 0, 110, 0)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_7.startPoint())
Sketch_1.setHorizontal(SketchLine_7.result())

### Create SketchLine
SketchLine_8 = Sketch_1.addLine(110, 0, 110, 30)
Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
Sketch_1.setVertical(SketchLine_8.result())

### Create SketchLine
SketchLine_9 = Sketch_1.addLine(110, 30, 80, 20)
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_9.endPoint())
model.do()

### Create Revolution
Revolution_1 = model.addRevolution(Part_1_doc, [model.selection("EDGE", "Sketch_1/SketchLine_3"), model.selection("EDGE", "Sketch_1/SketchLine_2")], model.selection("EDGE", "Sketch_1/SketchLine_1"), 360, 0)

### Create Revolution
Revolution_2_objects = [model.selection("EDGE", "Sketch_1/SketchLine_2"),
                        model.selection("EDGE", "Sketch_1/SketchLine_6"),
                        model.selection("EDGE", "Sketch_1/SketchLine_5")]
Revolution_2 = model.addRevolution(Part_1_doc, Revolution_2_objects, model.selection("EDGE", "Sketch_1/SketchLine_4"), 360, 0)

### Create Revolution
Revolution_3_objects = [model.selection("EDGE", "Sketch_1/SketchLine_5"),
                        model.selection("EDGE", "Sketch_1/SketchLine_9"),
                        model.selection("EDGE", "Sketch_1/SketchLine_8")]
Revolution_3 = model.addRevolution(Part_1_doc, Revolution_3_objects, model.selection("EDGE", "Sketch_1/SketchLine_7"), 360, 0)

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, '/tmp/shaper_Nose_0.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')

### Create Export
Export_2 = model.exportToXAO(Part_1_doc, '/tmp/shaper_end_0.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')

### Create Export
Export_3 = model.exportToXAO(Part_1_doc, '/tmp/shaper_gqux2zkv.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')

### Create Export
Export_4 = model.exportToXAO(Part_1_doc, '/tmp/shaper_qx0sbcii.xao', model.selection("FACE", "Revolution_2_2"), 'XAO')

### Create Export
Export_5 = model.exportToXAO(Part_1_doc, '/tmp/shaper_tpx9inko.xao', model.selection("FACE", "Revolution_2_3"), 'XAO')

### Create Export
Export_6 = model.exportToXAO(Part_1_doc, '/tmp/shaper_3ax5zd26.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')

### Create Export
Export_7 = model.exportToXAO(Part_1_doc, '/tmp/shaper_izc5tcxm.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')

### Create Export
Export_8 = model.exportToXAO(Part_1_doc, '/tmp/shaper_8bnql_4p.xao', model.selection("FACE", "Revolution_3_3"), 'XAO')

### Create Export
Export_9 = model.exportToXAO(Part_1_doc, '/tmp/shaper_v0aajww7.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')

### Create Export
Export_10 = model.exportToXAO(Part_1_doc, '/tmp/shaper_783ep9h9.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')

### Create Export
Export_11 = model.exportToXAO(Part_1_doc, '/tmp/shaper_viudf5nu.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')

### Create Export
Export_12 = model.exportToXAO(Part_1_doc, '/tmp/shaper__smva8a_.xao', model.selection("FACE", "Revolution_2_2"), 'XAO')

### Create Export
Export_13 = model.exportToXAO(Part_1_doc, '/tmp/shaper_kf23e2vv.xao', model.selection("FACE", "Revolution_2_3"), 'XAO')

### Create Export
Export_14 = model.exportToXAO(Part_1_doc, '/tmp/shaper_dsa4ng_i.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')

### Create Export
Export_15 = model.exportToXAO(Part_1_doc, '/tmp/shaper_k0mj7iks.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')

### Create Export
Export_16 = model.exportToXAO(Part_1_doc, '/tmp/shaper_owcdhei40.xao', model.selection("FACE", "Revolution_3_3"), 'XAO')

### Create Export
Export_17 = model.exportToXAO(Part_1_doc, '/tmp/shaper_7h2jxb7u.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')

### Create Export
Export_18 = model.exportToXAO(Part_1_doc, '/tmp/shaper_tnogw0ii.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')

### Create Export
Export_19 = model.exportToXAO(Part_1_doc, '/tmp/shaper_ics86ksd.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')

### Create Export
Export_20 = model.exportToXAO(Part_1_doc, '/tmp/shaper_eulypudq.xao', model.selection("FACE", "Revolution_2_2"), 'XAO')

### Create Export
Export_21 = model.exportToXAO(Part_1_doc, '/tmp/shaper_h0kmr3z4.xao', model.selection("FACE", "Revolution_2_3"), 'XAO')

### Create Export
Export_22 = model.exportToXAO(Part_1_doc, '/tmp/shaper_ab3bkn1g.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')

### Create Export
Export_23 = model.exportToXAO(Part_1_doc, '/tmp/shaper_4lcc4u40.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')

### Create Export
Export_24 = model.exportToXAO(Part_1_doc, '/tmp/shaper_2rkeu0_3.xao', model.selection("FACE", "Revolution_3_3"), 'XAO')

model.do()


### Create Part
Part_2 = model.addPart(partSet)
Part_2_doc = Part_2.document()

### Create Sketch
Sketch_2 = model.addSketch(Part_2_doc, model.defaultPlane("XOY"))

### Create SketchLine
SketchLine_10 = Sketch_2.addLine(0, 0, 30, 0)

### Create SketchProjection
SketchProjection_2 = Sketch_2.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_2 = SketchProjection_2.createdFeature()
Sketch_2.setCoincident(SketchLine_10.startPoint(), SketchPoint_2.result())
Sketch_2.setHorizontal(SketchLine_10.result())

### Create SketchLine
SketchLine_11 = Sketch_2.addLine(30, 0, 30, 20)
Sketch_2.setCoincident(SketchLine_10.endPoint(), SketchLine_11.startPoint())
Sketch_2.setVertical(SketchLine_11.result())

### Create SketchLine
SketchLine_12 = Sketch_2.addLine(30, 20, 0, 0)
Sketch_2.setCoincident(SketchLine_11.endPoint(), SketchLine_12.startPoint())
Sketch_2.setCoincident(SketchLine_10.startPoint(), SketchLine_12.endPoint())

### Create SketchLine
SketchLine_13 = Sketch_2.addLine(30, 0, 80, 0)
Sketch_2.setCoincident(SketchLine_10.endPoint(), SketchLine_13.startPoint())
Sketch_2.setHorizontal(SketchLine_13.result())

### Create SketchLine
SketchLine_14 = Sketch_2.addLine(80, 0, 80, 20)
Sketch_2.setCoincident(SketchLine_13.endPoint(), SketchLine_14.startPoint())
Sketch_2.setVertical(SketchLine_14.result())

### Create SketchLine
SketchLine_15 = Sketch_2.addLine(30, 20, 80, 20)
Sketch_2.setCoincident(SketchLine_11.endPoint(), SketchLine_15.startPoint())
Sketch_2.setCoincident(SketchLine_14.endPoint(), SketchLine_15.endPoint())
Sketch_2.setHorizontal(SketchLine_15.result())

### Create SketchLine
SketchLine_16 = Sketch_2.addLine(80, 0, 110, 0)
Sketch_2.setCoincident(SketchLine_13.endPoint(), SketchLine_16.startPoint())
Sketch_2.setHorizontal(SketchLine_16.result())

### Create SketchLine
SketchLine_17 = Sketch_2.addLine(110, 0, 110, 30)
Sketch_2.setCoincident(SketchLine_16.endPoint(), SketchLine_17.startPoint())
Sketch_2.setVertical(SketchLine_17.result())

### Create SketchLine
SketchLine_18 = Sketch_2.addLine(110, 30, 80, 20)
Sketch_2.setCoincident(SketchLine_17.endPoint(), SketchLine_18.startPoint())
Sketch_2.setCoincident(SketchLine_14.endPoint(), SketchLine_18.endPoint())
model.do()

### Create Revolution
Revolution_4 = model.addRevolution(Part_2_doc, [model.selection("EDGE", "Sketch_1/SketchLine_3"), model.selection("EDGE", "Sketch_1/SketchLine_2")], model.selection("EDGE", "Sketch_1/SketchLine_1"), 360, 0)

### Create Revolution
Revolution_5_objects = [model.selection("EDGE", "Sketch_1/SketchLine_2"),
                        model.selection("EDGE", "Sketch_1/SketchLine_6"),
                        model.selection("EDGE", "Sketch_1/SketchLine_5")]
Revolution_5 = model.addRevolution(Part_2_doc, Revolution_5_objects, model.selection("EDGE", "Sketch_1/SketchLine_4"), 360, 0)

### Create Revolution
Revolution_6_objects = [model.selection("EDGE", "Sketch_1/SketchLine_5"),
                        model.selection("EDGE", "Sketch_1/SketchLine_9"),
                        model.selection("EDGE", "Sketch_1/SketchLine_8")]
Revolution_6 = model.addRevolution(Part_2_doc, Revolution_6_objects, model.selection("EDGE", "Sketch_1/SketchLine_7"), 360, 0)

### Create Export
Export_25 = model.exportToXAO(Part_2_doc, '/tmp/shaper_Nose_0.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')

### Create Export
Export_26 = model.exportToXAO(Part_2_doc, '/tmp/shaper_end_0.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')

### Create Export
Export_27 = model.exportToXAO(Part_2_doc, '/tmp/shaper_gqux2zkv.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')

### Create Export
Export_28 = model.exportToXAO(Part_2_doc, '/tmp/shaper_qx0sbcii.xao', model.selection("FACE", "Revolution_2_2"), 'XAO')

### Create Export
Export_29 = model.exportToXAO(Part_2_doc, '/tmp/shaper_tpx9inko.xao', model.selection("FACE", "Revolution_2_3"), 'XAO')

### Create Export
Export_30 = model.exportToXAO(Part_2_doc, '/tmp/shaper_3ax5zd26.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')

### Create Export
Export_31 = model.exportToXAO(Part_2_doc, '/tmp/shaper_izc5tcxm.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')

### Create Export
Export_32 = model.exportToXAO(Part_2_doc, '/tmp/shaper_8bnql_4p.xao', model.selection("FACE", "Revolution_3_3"), 'XAO')

### Create Export
Export_33 = model.exportToXAO(Part_2_doc, '/tmp/shaper_v0aajww7.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')

### Create Export
Export_34 = model.exportToXAO(Part_2_doc, '/tmp/shaper_783ep9h9.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')

### Create Export
Export_35 = model.exportToXAO(Part_2_doc, '/tmp/shaper_viudf5nu.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')

### Create Export
Export_36 = model.exportToXAO(Part_2_doc, '/tmp/shaper__smva8a_.xao', model.selection("FACE", "Revolution_2_2"), 'XAO')

### Create Export
Export_37 = model.exportToXAO(Part_2_doc, '/tmp/shaper_kf23e2vv.xao', model.selection("FACE", "Revolution_2_3"), 'XAO')

### Create Export
Export_38 = model.exportToXAO(Part_2_doc, '/tmp/shaper_dsa4ng_i.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')

### Create Export
Export_39 = model.exportToXAO(Part_2_doc, '/tmp/shaper_k0mj7iks.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')

### Create Export
Export_40 = model.exportToXAO(Part_2_doc, '/tmp/shaper_owcdhei40.xao', model.selection("FACE", "Revolution_3_3"), 'XAO')

### Create Export
Export_41 = model.exportToXAO(Part_2_doc, '/tmp/shaper_7h2jxb7u.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')

### Create Export
Export_42 = model.exportToXAO(Part_2_doc, '/tmp/shaper_tnogw0ii.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')

### Create Export
Export_43 = model.exportToXAO(Part_2_doc, '/tmp/shaper_ics86ksd.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')

### Create Export
Export_44 = model.exportToXAO(Part_2_doc, '/tmp/shaper_eulypudq.xao', model.selection("FACE", "Revolution_2_2"), 'XAO')

### Create Export
Export_45 = model.exportToXAO(Part_2_doc, '/tmp/shaper_h0kmr3z4.xao', model.selection("FACE", "Revolution_2_3"), 'XAO')

### Create Export
Export_46 = model.exportToXAO(Part_2_doc, '/tmp/shaper_ab3bkn1g.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')

### Create Export
Export_47 = model.exportToXAO(Part_2_doc, '/tmp/shaper_4lcc4u40.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')

### Create Export
Export_48 = model.exportToXAO(Part_2_doc, '/tmp/shaper_2rkeu0_3.xao', model.selection("FACE", "Revolution_3_3"), 'XAO')

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Revolution_1_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1))
Revolution_1_2, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1, 1))
Revolution_2_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_2))
Revolution_2_2, = SHAPERSTUDY.shape(model.featureStringId(Revolution_2, 1))
Revolution_2_3, = SHAPERSTUDY.shape(model.featureStringId(Revolution_2, 2))
Revolution_3_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_3))
Revolution_3_2, = SHAPERSTUDY.shape(model.featureStringId(Revolution_3, 1))
Revolution_3_3, = SHAPERSTUDY.shape(model.featureStringId(Revolution_3, 2))
Revolution_1_1_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_4))
Revolution_1_2_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_4, 1))
Revolution_2_1_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_5))
Revolution_2_2_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_5, 1))
Revolution_2_3_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_5, 2))
Revolution_3_1_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_6))
Revolution_3_2_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_6, 1))
Revolution_3_3_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_6, 2))
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
(imported, geomObj_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_Nose_0.xao")
(imported, geomObj_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_end_0.xao")
(imported, geomObj_3, [], [], []) = geompy.ImportXAO("/tmp/shaper_gqux2zkv.xao")
(imported, geomObj_4, [], [], []) = geompy.ImportXAO("/tmp/shaper_qx0sbcii.xao")
(imported, geomObj_5, [], [], []) = geompy.ImportXAO("/tmp/shaper_tpx9inko.xao")
(imported, geomObj_6, [], [], []) = geompy.ImportXAO("/tmp/shaper_3ax5zd26.xao")
(imported, geomObj_7, [], [], []) = geompy.ImportXAO("/tmp/shaper_izc5tcxm.xao")
(imported, geomObj_8, [], [], []) = geompy.ImportXAO("/tmp/shaper_8bnql_4p.xao")
geomObj_9 = geompy.CreateGroup(geomObj_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_9, [1])
geomObj_10 = geompy.CreateGroup(geomObj_4, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_10, [1])
geomObj_11 = geompy.CreateGroup(geomObj_7, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_11, [1])
geomObj_12 = geompy.CreateGroup(geomObj_8, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_12, [1])
geomObj_13 = geompy.MakeFuseList([geomObj_9, geomObj_10, geomObj_12, geomObj_11], True, True)
geomObj_14 = geompy.MakeSolid([geomObj_13])
[geomObj_15,geomObj_16,geomObj_17,geomObj_18] = geompy.SubShapeAll(geomObj_14, geompy.ShapeType["VERTEX"])
[geomObj_19,geomObj_20,geomObj_21,geomObj_22] = geompy.SubShapeAll(geomObj_14, geompy.ShapeType["FACE"])
[geomObj_23,geomObj_24,geomObj_25,geomObj_26] = geompy.SubShapeAll(geomObj_14, geompy.ShapeType["FACE"])
geomObj_27 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_28 = geompy.MakeVertex(-200, 0, 0)
geomObj_29 = geompy.MakeCylinder(geomObj_28, geomObj_27, 200, 400)
[geomObj_30,geomObj_31,geomObj_32] = geompy.SubShapeAll(geomObj_29, geompy.ShapeType["FACE"])
[geomObj_33,geomObj_34,geomObj_35] = geompy.SubShapeAll(geomObj_29, geompy.ShapeType["FACE"])
geomObj_36 = geompy.MakeCutList(geomObj_29, [geomObj_14], True)
geomObj_37 = geompy.CreateGroup(geomObj_36, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_37, [3, 10, 12])
geomObj_38 = geompy.CreateGroup(geomObj_36, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_38, [15, 22, 27, 32])
(imported, Revolution_1_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_Nose_0.xao")
(imported, Revolution_1_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_end_0.xao")
(imported, Revolution_2_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_gqux2zkv.xao")
(imported, Revolution_2_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_qx0sbcii.xao")
(imported, Revolution_2_3, [], [], []) = geompy.ImportXAO("/tmp/shaper_tpx9inko.xao")
(imported, Revolution_3_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_3ax5zd26.xao")
(imported, Revolution_3_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_izc5tcxm.xao")
(imported, Revolution_3_3, [], [], []) = geompy.ImportXAO("/tmp/shaper_8bnql_4p.xao")
Nose = geompy.CreateGroup(Revolution_1_1, geompy.ShapeType["FACE"])
geompy.UnionList(Nose, [Revolution_1_1])
section_1 = geompy.CreateGroup(Revolution_2_2, geompy.ShapeType["FACE"])
geompy.UnionIDs(section_1, [1])
section_2 = geompy.CreateGroup(Revolution_3_2, geompy.ShapeType["FACE"])
geompy.UnionIDs(section_2, [1])
back = geompy.CreateGroup(Revolution_3_3, geompy.ShapeType["FACE"])
geompy.UnionIDs(back, [1])
Fuse_1 = geompy.MakeFuseList([Nose, section_1, back, section_2], True, True)
Rocket = geompy.MakeSolid([Fuse_1])
[geomObj_39,geomObj_40,geomObj_41,geomObj_42] = geompy.SubShapeAll(Rocket, geompy.ShapeType["VERTEX"])
[geomObj_43,geomObj_44,geomObj_45,geomObj_46] = geompy.SubShapeAll(Rocket, geompy.ShapeType["FACE"])
[geomObj_47,geomObj_48,geomObj_49,geomObj_50] = geompy.SubShapeAll(Rocket, geompy.ShapeType["FACE"])
Vector_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
Vertex_1 = geompy.MakeVertex(-200, 0, 0)
Cylinder_1 = geompy.MakeCylinder(Vertex_1, Vector_1, 200, 400)
[geomObj_51,geomObj_52,geomObj_53] = geompy.SubShapeAll(Cylinder_1, geompy.ShapeType["FACE"])
[geomObj_54,geomObj_55,geomObj_56] = geompy.SubShapeAll(Cylinder_1, geompy.ShapeType["FACE"])
[geomObj_51, geomObj_52, geomObj_53, geomObj_54, geomObj_55, geomObj_56] = geompy.GetExistingSubObjects(Cylinder_1, False)
Domain = geompy.MakeCutList(Cylinder_1, [Rocket], True)
[geomObj_57,geomObj_58,geomObj_59,geomObj_60,geomObj_61,geomObj_62,geomObj_63] = geompy.SubShapeAllSortedCentres(Domain, geompy.ShapeType["FACE"])
Farfield = geompy.CreateGroup(Domain, geompy.ShapeType["FACE"])
geompy.UnionIDs(Farfield, [3, 10, 12])
Rocket_1 = geompy.CreateGroup(Domain, geompy.ShapeType["FACE"])
geompy.UnionIDs(Rocket_1, [15, 22, 27, 32])
[Farfield, Rocket_1] = geompy.GetExistingSubObjects(Domain, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Revolution_1_1, 'Revolution_1_1' )
geompy.addToStudy( Revolution_1_2, 'Revolution_1_2' )
geompy.addToStudy( Revolution_2_1, 'Revolution_2_1' )
geompy.addToStudy( Revolution_2_2, 'Revolution_2_2' )
geompy.addToStudy( Revolution_2_3, 'Revolution_2_3' )
geompy.addToStudy( Revolution_3_1, 'Revolution_3_1' )
geompy.addToStudy( Revolution_3_2, 'Revolution_3_2' )
geompy.addToStudy( Revolution_3_3, 'Revolution_3_3' )
geompy.addToStudyInFather( Revolution_1_1, Nose, 'Nose' )
geompy.addToStudyInFather( Revolution_2_2, section_1, 'section_1' )
geompy.addToStudyInFather( Revolution_3_2, section_2, 'section_2' )
geompy.addToStudyInFather( Revolution_3_3, back, 'back' )
geompy.addToStudy( Fuse_1, 'Fuse_1' )
geompy.addToStudy( Rocket, 'Rocket' )
geompy.addToStudy( Vector_1, 'Vector_1' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( Domain, 'Domain' )
geompy.addToStudyInFather( Domain, Farfield, 'Farfield' )
geompy.addToStudyInFather( Domain, Rocket_1, 'Rocket' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(Domain,'Mesh_1')
NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 30 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 4 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(Nose, 3)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(section_1, 3)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(section_2, 4)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(back, 5)
NETGEN_2D_Parameters_1.SetMinSize( 0.1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 22050 )

NETGEN_3D = Mesh_1.Tetrahedron()
NETGEN_3D_Parameters_1 = NETGEN_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 30 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 4 )
NETGEN_3D_Parameters_1.SetNbVolOptSteps( 4 )
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(Nose, 3)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(section_1, 4)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(section_2, 5)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(back, 5)
NETGEN_3D_Parameters_1.SetMinSize( 0.1 )
NETGEN_3D_Parameters_1.SetElemSizeWeight( 4.67919e-310 )

Farfield_1 = Mesh_1.GroupOnGeom(Farfield,'Farfield',SMESH.FACE)
Rocket_2 = Mesh_1.GroupOnGeom(Rocket_1,'Rocket',SMESH.FACE)
isDone = Mesh_1.Compute()
[ Farfield_1, Rocket_2 ] = Mesh_1.GetGroups()
Viscous_Layers_1 = NETGEN_3D.ViscousLayers(1.5,20,1.2,[ 3, 10, 12 ],1,smeshBuilder.SURF_OFFSET_SMOOTH)
isDone = Mesh_1.Compute()
[ Farfield_1, Rocket_2 ] = Mesh_1.GetGroups()

## Set names of Mesh objects
smesh.SetName(Rocket_2, 'Rocket')
smesh.SetName(Farfield_1, 'Farfield')
smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(Viscous_Layers_1, 'Viscous Layers_1')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
