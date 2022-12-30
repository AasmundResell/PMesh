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

### Create Point
Point_2 = model.addPoint(Part_1_doc, 75.90000000000001, 0, 0)

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, '/tmp/shaper_if8vzq4n.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')
Export_1.setName("Export_6")

### Create Export
Export_2 = model.exportToXAO(Part_1_doc, '/tmp/shaper_y2iu8i25.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')
Export_2.setName("Export_7")

### Create Export
Export_3 = model.exportToXAO(Part_1_doc, '/tmp/shaper_rksjn16x.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')
Export_3.setName("Export_8")

### Create Export
Export_4 = model.exportToXAO(Part_1_doc, '/tmp/shaper_7n7tcb_0.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')
Export_4.setName("Export_9")

### Create Export
Export_5 = model.exportToXAO(Part_1_doc, '/tmp/shaper_sdf784l5.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')
Export_5.setName("Export_10")

### Create Export
Export_6 = model.exportToXAO(Part_1_doc, '/tmp/shaper_start_0.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')
Export_6.setName("Export_1")

### Create Export
Export_7 = model.exportToXAO(Part_1_doc, '/tmp/shaper_ConicNose.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')
Export_7.setName("Export_2")

### Create Export
Export_8 = model.exportToXAO(Part_1_doc, '/tmp/shaper_middle_1.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')
Export_8.setName("Export_3")

### Create Export
Export_9 = model.exportToXAO(Part_1_doc, '/tmp/shaper_middle_2.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')
Export_9.setName("Export_4")

### Create Export
Export_10 = model.exportToXAO(Part_1_doc, '/tmp/shaper_rear_2.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')
Export_10.setName("Export_5")

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
[Edge_1] = geompy.SubShapes(Projectile, [5])
[Vertex_3,Vertex_4,Vertex_5] = geompy.SubShapes(Projectile, [15, 10, 20])
geomObj_1 = geompy.MakeVertex(-200, 0, 0)
geomObj_2 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_3 = geompy.MakeCylinder(geomObj_1, geomObj_2, 200, 475.9)
geomObj_4 = geompy.MakeCutList(geomObj_3, [Projectile], True)
geomObj_5 = geompy.CreateGroup(geomObj_4, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_5, [3, 10, 12])
geomObj_6 = geompy.CreateGroup(geomObj_4, geompy.ShapeType["FACE"])
geompy.UnionIDs(geomObj_6, [15, 22, 27, 32])
[geomObj_5, geomObj_6] = geompy.GetExistingSubObjects(geomObj_4, False)
Vertex_1 = geompy.MakeVertex(0, 0, 0)
ox = geompy.MakeVectorDXDYDZ(1, 0, 0)
Cylinder_1 = geompy.MakeCylinder(Vertex_1, ox, 100, 300)
(imported, geomObj_7, [], [], []) = geompy.ImportXAO("/tmp/shaper_if8vzq4n.xao")
(imported, geomObj_8, [], [], []) = geompy.ImportXAO("/tmp/shaper_y2iu8i25.xao")
(imported, geomObj_9, [], [], []) = geompy.ImportXAO("/tmp/shaper_rksjn16x.xao")
(imported, geomObj_10, [], [], []) = geompy.ImportXAO("/tmp/shaper_7n7tcb_0.xao")
(imported, geomObj_11, [], [], []) = geompy.ImportXAO("/tmp/shaper_sdf784l5.xao")
oz = geompy.MakeVectorDXDYDZ(0, 0, 1)
oy = geompy.MakeVectorDXDYDZ(0, 1, 0)
Domain = geompy.MakeCutList(Cylinder_1, [Projectile], True)
Plane_3 = geompy.MakePlane(Vertex_3, ox, 2000)
Plane_4 = geompy.MakePlane(Vertex_4, ox, 2000)
Plane_5 = geompy.MakePlane(Vertex_5, ox, 2000)
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
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( ox, 'ox' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( oz, 'oz' )
geompy.addToStudy( oy, 'oy' )
geompy.addToStudyInFather( Projectile, Vertex_3, 'Vertex_3' )
geompy.addToStudy( Plane_3, 'Plane_3' )
geompy.addToStudy( Domain, 'Domain' )
geompy.addToStudyInFather( Projectile, Vertex_5, 'Vertex_5' )
geompy.addToStudy( Plane_5, 'Plane_5' )
geompy.addToStudyInFather( Projectile, Vertex_4, 'Vertex_4' )
geompy.addToStudy( Plane_4, 'Plane_4' )
geompy.addToStudyInFather( Projectile, Edge_1, 'Edge_1' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(__NOT__Published__Object__,'Mesh_1')
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 1 )
NETGEN_3D_Parameters_1.SetMinSize( 0.01 )
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 2 )
NETGEN_3D_Parameters_1.SetChordalError( 0.5 )
NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 1 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_1.SetCheckChartBoundary( 3 )
PDomain = Mesh_1.GroupOnGeom(__NOT__Published__Object__,'PDomain',SMESH.VOLUME)
back = Mesh_1.GroupOnGeom(__NOT__Published__Object__,'back',SMESH.VOLUME)
Regular_1D = Mesh_1.Segment(geom=__NOT__Published__Object__)
Sub_mesh_1 = Regular_1D.GetSubMesh()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(15)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=__NOT__Published__Object__)
Quadrangle_Parameters_1 = Quadrangle_2D.QuadrangleParameters(smeshBuilder.QUAD_STANDARD,-1,[],[])
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa,geom=__NOT__Published__Object__)
[ PDomain, back ] = Mesh_1.GetGroups()
NETGEN_1D_2D_3D_1 = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D,geom=__NOT__Published__Object__)
Sub_mesh_2 = NETGEN_1D_2D_3D_1.GetSubMesh()
status = Mesh_1.AddHypothesis(NETGEN_3D_Parameters_1,__NOT__Published__Object__)
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_1, Sub_mesh_2 ] ])
[ PDomain, back ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ PDomain, back ] = Mesh_1.GetGroups()


## Set names of Mesh objects
smesh.SetName(Quadrangle_Parameters_1, 'Quadrangle Parameters_1')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(PDomain, 'PDomain')
smesh.SetName(back, 'back')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
