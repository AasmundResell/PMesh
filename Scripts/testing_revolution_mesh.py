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
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

(imported, Revolution_1_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_Nose_0.xao")
(imported, Revolution_1_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_end_0.xao")
(imported, Revolution_2_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_gqux2zkv.xao")
(imported, Revolution_2_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_qx0sbcii.xao")
(imported, Revolution_2_3, [], [], []) = geompy.ImportXAO("/tmp/shaper_tpx9inko.xao")
(imported, Revolution_3_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_3ax5zd26.xao")
(imported, Revolution_3_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_izc5tcxm.xao")
(imported, Revolution_3_3, [], [], []) = geompy.ImportXAO("/tmp/shaper_8bnql_4p.xao")
Nose = geompy.CreateGroup(Revolution_1_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Nose, [1])
section_1 = geompy.CreateGroup(Revolution_2_2, geompy.ShapeType["FACE"])
geompy.UnionIDs(section_1, [1])
section_2 = geompy.CreateGroup(Revolution_3_2, geompy.ShapeType["FACE"])
geompy.UnionIDs(section_2, [1])
back = geompy.CreateGroup(Revolution_3_3, geompy.ShapeType["FACE"])
geompy.UnionIDs(back, [1])
Fuse_1 = geompy.MakeFuseList([Nose, section_1, back, section_2], True, True)
Rocket = geompy.MakeSolid([Fuse_1])
Vector_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
Vertex_1 = geompy.MakeVertex(-200, 0, 0)
Cylinder_1 = geompy.MakeCylinder(Vertex_1, Vector_1, 200, 400)
Domain = geompy.MakeCutList(Cylinder_1, [Rocket], True)
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

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

NETGEN_3D_Parameters_2 = smesh.CreateHypothesis('NETGEN_Parameters_3D', 'libNETGENEngine.so')
NETGEN_3D_Parameters_2.SetOptimize( 1 )
NETGEN_3D_Parameters_2.SetLocalSizeOnShape(section_2, 41.2311)
NETGEN_3D_Parameters_2.SetLocalSizeOnShape(back, 2)
NETGEN_3D_Parameters_2.SetLocalSizeOnShape(Revolution_1_1, 10)
NETGEN_3D_Parameters_2.SetLocalSizeOnShape(Revolution_2_2, 20)
NETGEN_3D_Parameters_2.SetLocalSizeOnShape(Revolution_3_2, 40)
NETGEN_3D_Parameters_2.SetMaxSize( 20 )
NETGEN_3D_Parameters_2.SetMinSize( 0.1 )
NETGEN_3D_Parameters_2.SetFineness( 3 )
NETGEN_3D_Parameters_2.SetElemSizeWeight( 4.63916e-310 )
Viscous_Layers_2 = smesh.CreateHypothesis('ViscousLayers')
Viscous_Layers_2.SetTotalThickness( 1 )
Viscous_Layers_2.SetNumberLayers( 20 )
Viscous_Layers_2.SetStretchFactor( 1.2 )
Viscous_Layers_2.SetFaces( [], 1 )
Viscous_Layers_2.SetMethod( smeshBuilder.SURF_OFFSET_SMOOTH )
Mesh = smesh.Mesh(Domain,'Mesh')
NETGEN_1D_2D = Mesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 41.2311 )
NETGEN_2D_Parameters_1.SetMinSize( 0.160716 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(Revolution_1_1, 10)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(Revolution_2_2, 20)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(Revolution_3_2, 40)
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 22031 )
Viscous_Layers_2D_1 = NETGEN_1D_2D.ViscousLayers2D(1,20,1.2,[],0)
NETGEN_3D = Mesh.Tetrahedron()
NETGEN_3D_Parameters_1 = NETGEN_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 29 )
NETGEN_3D_Parameters_1.SetMinSize( 0.160716 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 2 )
NETGEN_3D_Parameters_1.SetElemSizeWeight( 4.63916e-310 )
Viscous_Layers_1 = NETGEN_3D.ViscousLayers(1,20,1,[ 3 ],1,smeshBuilder.SURF_OFFSET_SMOOTH)
isDone = Mesh.Compute()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
smesh.SetName(Mesh.GetMesh(), 'Mesh')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(Viscous_Layers_1, 'Viscous Layers_1')
smesh.SetName(Viscous_Layers_2, 'Viscous Layers_2')
smesh.SetName(NETGEN_3D_Parameters_2, 'NETGEN 3D Parameters_2')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(Viscous_Layers_2D_1, 'Viscous Layers 2D_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
