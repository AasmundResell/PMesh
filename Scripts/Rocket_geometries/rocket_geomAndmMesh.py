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
model.addParameter(Part_1_doc, "L", '100')
model.addParameter(Part_1_doc, "rho", '(R**2+L**2)/(2*R)', 'radius ogive angle')

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("YOZ"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 0, 100, 0)

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
Sketch_1.setLength(SketchLine_1.result(), 100)

### Create SketchLine
SketchLine_9 = Sketch_1.addLine(0, 7.5, -22.4, 5.5)
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_9.endPoint())

### Create SketchLine
SketchLine_10 = Sketch_1.addLine(-12.1, 12.5, 0, 7.5)
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_10.startPoint())
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_10.endPoint())

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(2.912762408282777e-13, -662.9166666666666, 0, 7.5, 100, 0, True)
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

### Create SketchLine
SketchLine_16 = Sketch_1.addLine(100, 0, 98.59999999999999, 0)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_16.startPoint())
Sketch_1.setHorizontal(SketchLine_16.result())
Sketch_1.setHorizontalDistance(SketchLine_1.endPoint(), SketchLine_16.endPoint(), 1.4)

### Create SketchPoint
SketchPoint_2 = Sketch_1.addPoint(98.59999999999999, 0)
Sketch_1.setCoincident(SketchLine_16.endPoint(), SketchPoint_2.coordinates())

### Create SketchLine
SketchLine_17 = Sketch_1.addLine(98.59999999999999, 0, 98.59999999999999, 0.2096764569940392)
Sketch_1.setCoincident(SketchLine_16.endPoint(), SketchLine_17.startPoint())
Sketch_1.setCoincident(SketchLine_17.endPoint(), SketchArc_1.results()[1])
Sketch_1.setVertical(SketchLine_17.result())
model.do()
Sketch_1.changeFacesOrder([[SketchLine_8.result(), SketchLine_11.result(), SketchLine_4.result(), SketchLine_15.result(), SketchLine_14.result(), SketchLine_3.result(), SketchLine_2.result()],
                           [SketchLine_1.result(), SketchLine_17.result(), SketchArc_1.results()[1], SketchLine_8.result()],
                           [SketchLine_14.result(), SketchLine_15.result(), SketchLine_4.result(), SketchLine_3.result()],
                           [SketchLine_4.result(), SketchLine_7.result(), SketchLine_9.result(), SketchLine_4.result()],
                           [SketchLine_7.result(), SketchLine_9.result(), SketchLine_10.result()],
                           [SketchLine_9.result(), SketchLine_7.result(), SketchLine_6.result(), SketchLine_5.result()],
                           [SketchLine_7.result(), SketchLine_11.result(), SketchLine_9.result()],
                           [SketchLine_1.result(), SketchArc_1.results()[1], SketchLine_17.result()]
                          ])
model.do()

### Create Revolution
Revolution_1_objects = [model.selection("FACE", "Sketch_1/Face-SketchLine_1r-SketchLine_17f-SketchArc_2_2f-SketchLine_8r"),
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
Fuse_3_objects_1 = [model.selection("SOLID", "Revolution_1_1_5"),
                    model.selection("SOLID", "Revolution_1_1_4"),
                    model.selection("SOLID", "AngularCopy_1_1_1"),
                    model.selection("SOLID", "AngularCopy_1_1_4"),
                    model.selection("SOLID", "AngularCopy_1_1_3"),
                    model.selection("SOLID", "AngularCopy_1_1_2"),
                    model.selection("SOLID", "Revolution_1_1_2"),
                    model.selection("SOLID", "Revolution_1_1_1")]
Fuse_3 = model.addFuse(Part_1_doc, Fuse_3_objects_1, keepSubResults = True)

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, '/tmp/shaper_qbbsy4us.xao', model.selection("COMPSOLID", "Fuse_3_1"), 'XAO')

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.standardPlane("XOZ"))

### Create SketchProjection
SketchProjection_2 = Sketch_2.addProjection(model.selection("VERTEX", "[Fuse_3_1_2/Modified_Face&Sketch_1/SketchArc_2_2][(Fuse_3_1_2/Modified_Face&Sketch_1/SketchArc_2_2)(Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_17)2(AngularCopy_1_1_4/MF:Rotated&Extrusion_1_1_2/To_Face)2(AngularCopy_1_1_1/MF:Rotated&Extrusion_1_1_2/From_Face)2]__cc"), False)
SketchPoint_3 = SketchProjection_2.createdFeature()

### Create SketchCircle
SketchCircle_1 = Sketch_2.addCircle(0, 0, 300)
Sketch_2.setCoincident(SketchPoint_3.result(), SketchCircle_1.center())
Sketch_2.setRadius(SketchCircle_1.results()[1], 300)
model.do()

### Create Extrusion
Extrusion_2 = model.addExtrusion(Part_1_doc, [model.selection("WIRE", "Sketch_2/Face-SketchCircle_1_2f_wire")], model.selection(), 300, 500, "Faces|Wires")

### Create Export
Export_2 = model.exportToXAO(Part_1_doc, '/tmp/shaper_z4r73e9g.xao', model.selection("COMPSOLID", "Fuse_3_1"), 'XAO')

### Create Export
Export_3 = model.exportToXAO(Part_1_doc, '/tmp/shaper_m5pd1gxl.xao', model.selection("SOLID", "Extrusion_2_1"), 'XAO')

### Create Export
Export_4 = model.exportToXAO(Part_1_doc, '/tmp/shaper_b0pqzhjh.xao', model.selection("COMPSOLID", "Fuse_3_1"), 'XAO')

### Create Export
Export_5 = model.exportToXAO(Part_1_doc, '/tmp/shaper_50_xusul.xao', model.selection("SOLID", "Extrusion_2_1"), 'XAO')

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
Fuse_3_1, = SHAPERSTUDY.shape(model.featureStringId(Fuse_3))
Extrusion_2_1, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_2))
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

(imported, geomObj_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_qbbsy4us.xao")
(imported, Fuse_3_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_z4r73e9g.xao")
[geomObj_2,geomObj_3,geomObj_4,geomObj_5,geomObj_6,geomObj_7,geomObj_8,geomObj_9,geomObj_10,geomObj_11,geomObj_12,geomObj_13,geomObj_14,geomObj_15,geomObj_16,geomObj_17,geomObj_18,geomObj_19,geomObj_20,geomObj_21,geomObj_22,geomObj_23,geomObj_24,geomObj_25,geomObj_26,geomObj_27,geomObj_28,geomObj_29,geomObj_30,geomObj_31,geomObj_32,geomObj_33,geomObj_34,geomObj_35,geomObj_36,geomObj_37,geomObj_38,geomObj_39,geomObj_40,geomObj_41,geomObj_42,geomObj_43,geomObj_44,geomObj_45,geomObj_46,geomObj_47,geomObj_48,geomObj_49,geomObj_50,geomObj_51,geomObj_52,geomObj_53,geomObj_54,geomObj_55,geomObj_56,geomObj_57,geomObj_58,geomObj_59,geomObj_60,geomObj_61,geomObj_62,geomObj_63,geomObj_64,geomObj_65,geomObj_66,geomObj_67,geomObj_68,geomObj_69,geomObj_70,geomObj_71,geomObj_72,geomObj_73,geomObj_74,geomObj_75,geomObj_76,geomObj_77,geomObj_78,geomObj_79,geomObj_80,geomObj_81,geomObj_82,geomObj_83,geomObj_84,geomObj_85,geomObj_86,geomObj_87,geomObj_88,geomObj_89,geomObj_90,geomObj_91,geomObj_92] = geompy.SubShapeAll(Fuse_3_1, geompy.ShapeType["FACE"])
[geomObj_93,geomObj_94,geomObj_95,geomObj_96,geomObj_97,geomObj_98,geomObj_99,geomObj_100,geomObj_101,geomObj_102,geomObj_103,geomObj_104,geomObj_105,geomObj_106,geomObj_107,geomObj_108,geomObj_109,geomObj_110,geomObj_111,geomObj_112,geomObj_113,geomObj_114,geomObj_115,geomObj_116,geomObj_117,geomObj_118,geomObj_119,geomObj_120,geomObj_121,geomObj_122,geomObj_123,geomObj_124,geomObj_125,geomObj_126,geomObj_127,geomObj_128,geomObj_129,geomObj_130,geomObj_131,geomObj_132,geomObj_133,geomObj_134,geomObj_135,geomObj_136,geomObj_137,geomObj_138,geomObj_139,geomObj_140,geomObj_141,geomObj_142,geomObj_143,geomObj_144,geomObj_145,geomObj_146,geomObj_147,geomObj_148,geomObj_149,geomObj_150,geomObj_151,geomObj_152,geomObj_153,geomObj_154,geomObj_155,geomObj_156,geomObj_157,geomObj_158,geomObj_159,geomObj_160,geomObj_161,geomObj_162,geomObj_163,geomObj_164,geomObj_165,geomObj_166,geomObj_167,geomObj_168,geomObj_169,geomObj_170,geomObj_171,geomObj_172,geomObj_173,geomObj_174,geomObj_175,geomObj_176,geomObj_177,geomObj_178,geomObj_179,geomObj_180,geomObj_181,geomObj_182,geomObj_183] = geompy.SubShapeAll(Fuse_3_1, geompy.ShapeType["FACE"])
(imported, Extrusion_2_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_m5pd1gxl.xao")
(imported, geomObj_184, [], [], []) = geompy.ImportXAO("/tmp/shaper_b0pqzhjh.xao")
(imported, geomObj_185, [], [], []) = geompy.ImportXAO("/tmp/shaper_50_xusul.xao")
Cut_1 = geompy.MakeCutList(Extrusion_2_1, [Fuse_3_1], True)
farfield = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(farfield, [3, 10, 12])
rocket = geompy.CreateGroup(Fuse_3_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(rocket, [4, 11, 38, 45, 50, 55, 60, 67, 74, 79, 84, 89, 94, 98, 109, 120, 131, 142, 153, 158, 163, 171, 178, 181, 186, 191, 199, 206, 209, 214, 219, 227, 234, 237, 242, 247, 255, 262, 265, 272, 277, 280, 283, 288, 291, 296, 301, 304, 309, 312, 317, 320, 325, 330, 333, 338, 341, 346, 349, 354, 359, 362, 367, 370, 375, 378, 381, 388, 391, 394, 397, 402, 407, 410, 413, 416, 421, 426, 429, 432, 435, 440, 445, 448, 451, 454, 457, 459, 461, 463, 465])
rocket_1 = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(rocket_1, [404, 204, 104, 306, 407, 409, 207, 309, 109, 412, 314, 415, 114, 217, 15, 319, 222, 324, 225, 125, 327, 330, 230, 130, 335, 237, 338, 137, 240, 140, 343, 346, 44, 145, 46, 249, 148, 351, 354, 51, 254, 153, 257, 359, 262, 364, 62, 164, 367, 269, 67, 372, 272, 171, 375, 72, 174, 275, 380, 280, 179, 383, 182, 83, 285, 387, 389, 187, 88, 391, 290, 394, 293, 93, 296, 397, 197, 399, 401, 301])
[farfield, rocket_1] = geompy.GetExistingSubObjects(Cut_1, False)
[farfield, rocket_1] = geompy.GetExistingSubObjects(Cut_1, False)
geompy.addToStudy( Extrusion_2_1, 'Extrusion_2_1' )
geompy.addToStudy( Fuse_3_1, 'Fuse_3_1' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudyInFather( Cut_1, farfield, 'farfield' )
geompy.addToStudyInFather( Fuse_3_1, rocket, 'rocket' )
geompy.addToStudyInFather( Cut_1, rocket_1, 'rocket' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

#hyp_0.SetLength( 116.619 ) ### not created Object
NETGEN_3D_Parameters_1 = smesh.CreateHypothesisByAverageLength( 'NETGEN_Parameters', 'NETGENEngine', 116.619, 0 )
NETGEN_1D_2D_3D = smesh.CreateHypothesis('NETGEN_2D3D', 'NETGENEngine')
NETGEN_3D_Parameters_2 = smesh.CreateHypothesis('NETGEN_Parameters', 'NETGENEngine')
NETGEN_3D_Parameters_2.SetMaxSize( 100 )
NETGEN_3D_Parameters_2.SetMinSize( 1 )
NETGEN_3D_Parameters_2.SetSecondOrder( 0 )
NETGEN_3D_Parameters_2.SetOptimize( 1 )
NETGEN_3D_Parameters_2.SetFineness( 2 )
NETGEN_3D_Parameters_2.SetChordalError( -1 )
NETGEN_3D_Parameters_2.SetChordalErrorEnabled( 0 )
NETGEN_3D_Parameters_2.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_2.SetFuseEdges( 1 )
NETGEN_3D_Parameters_2.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_2.SetCheckChartBoundary( 3 )
Mesh_2 = smesh.Mesh(Cut_1,'Mesh_2')
status = Mesh_2.AddHypothesis(NETGEN_3D_Parameters_2)
status = Mesh_2.AddHypothesis(NETGEN_1D_2D_3D)
farfield_1 = Mesh_2.GroupOnGeom(farfield,'farfield',SMESH.FACE)
rocket_2 = Mesh_2.GroupOnGeom(rocket_1,'rocket',SMESH.FACE)
isDone = Mesh_2.Compute()
[ farfield_1, rocket_2 ] = Mesh_2.GetGroups()
NETGEN_3D_Parameters_2.SetMinSize( 0.2 )
NETGEN_3D_Parameters_2.SetCheckChartBoundary( 3 )
isDone = Mesh_2.Compute()
[ farfield_1, rocket_2 ] = Mesh_2.GetGroups()
Viscous_Layers_1 = smesh.CreateHypothesis('ViscousLayers')
Viscous_Layers_1.SetTotalThickness( 10 )
Viscous_Layers_1.SetNumberLayers( 4 )
Viscous_Layers_1.SetStretchFactor( 1.2 )
Viscous_Layers_1.SetMethod( smeshBuilder.SURF_OFFSET_SMOOTH )
Viscous_Layers_1.SetFaces( [ 404, 204, 104, 306, 407, 409, 207, 309, 109, 412, 314, 415, 114, 217, 15, 319, 222, 324, 225, 125, 327, 330, 230, 130, 335, 237, 338, 137, 240, 140, 343, 346, 44, 145, 46, 249, 148, 351, 354, 51, 254, 153, 257, 359, 262, 364, 62, 164, 367, 269, 67, 372, 272, 171, 375, 72, 174, 275, 380, 280, 179, 383, 182, 83, 285, 387, 389, 187, 88, 391, 290, 394, 293, 93, 296, 397, 197, 399, 401, 301 ], 0 )
status = Mesh_2.AddHypothesis(Viscous_Layers_1)
isDone = Mesh_2.Compute()
[ farfield_1, rocket_2 ] = Mesh_2.GetGroups()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D, 'NETGEN 1D-2D-3D')
smesh.SetName(Mesh_2.GetMesh(), 'Mesh_2')
smesh.SetName(farfield_1, 'farfield')
smesh.SetName(rocket_2, 'rocket')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(NETGEN_3D_Parameters_2, 'NETGEN 3D Parameters_2')
smesh.SetName(Viscous_Layers_1, 'Viscous Layers_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
