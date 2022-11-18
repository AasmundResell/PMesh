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
SketchLine_1 = Sketch_1.addLine(0, 0, 9.200026755396529, 0)
SketchLine_1.setName("baseAxialLine_0")
SketchLine_1.result().setName("baseAxialLine_0")

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(9.200026755396529, 0, 9.200026755396529, 3.611144301867149)
SketchLine_2.setName("baseAxialLine_0")
SketchLine_2.result().setName("baseRadialLine_0")
Sketch_1.setHorizontal(SketchLine_1.result())
Sketch_1.setVertical(SketchLine_2.result())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(9.16943268533713, -24.51352758384406, 0, 2.074432264649553, 9.200026755396529, 3.611144301867149, True)
SketchArc_1.setName("noseOgiveCurve")
SketchArc_1.result().setName("noseOgiveCurve")
SketchArc_1.results()[1].setName("noseOgiveCurve_1")
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchArc_1.endPoint())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(0, 0, 0, 2.074432264649553)
SketchLine_3.setName("noseFrontLine")
SketchLine_3.result().setName("noseFrontLine")
Sketch_1.setVertical(SketchLine_3.result())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchArc_1.startPoint())
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_3.startPoint())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(9.200026755396529, 0, 14.2, 0)
SketchLine_4.setName("baseAxialLine_1")
SketchLine_4.result().setName("baseAxialLine_1")

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(14.2, 0, 14.2, 3.611144301867149)
SketchLine_5.setName("baseAxialLine_1")
SketchLine_5.result().setName("baseRadialLine_1")
Sketch_1.setHorizontal(SketchLine_4.result())
Sketch_1.setVertical(SketchLine_5.result())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(9.200026755396529, 3.611144301867149, 14.2, 3.611144301867149)
SketchLine_6.setName("upperContourLine_1")
SketchLine_6.result().setName("upperContourLine_1")
Sketch_1.setHorizontal(SketchLine_6.result())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.endPoint())

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(14.2, 0, 16.2, 0)
SketchLine_7.setName("baseAxialLine_2")
SketchLine_7.result().setName("baseAxialLine_2")

### Create SketchLine
SketchLine_8 = Sketch_1.addLine(16.2, 0, 16.2, 1.8)
SketchLine_8.setName("baseAxialLine_2")
SketchLine_8.result().setName("baseRadialLine_2")
Sketch_1.setHorizontal(SketchLine_7.result())
Sketch_1.setVertical(SketchLine_8.result())
Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())

### Create SketchLine
SketchLine_9 = Sketch_1.addLine(14.2, 3.611144301867149, 16.2, 1.8)
SketchLine_9.setName("upperContourLine_2")
SketchLine_9.result().setName("upperContourLine_2")
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.endPoint())
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchPoint_1.result())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_4.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_7.startPoint())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_9.startPoint())
model.do()

### Create Revolution
Revolution_1_objects = [model.selection("EDGE", "Sketch_1/noseFrontLine"),
                        model.selection("EDGE", "Sketch_1/noseOgiveCurve_1"),
                        model.selection("EDGE", "Sketch_1/baseRadialLine_0")]
Revolution_1 = model.addRevolution(Part_1_doc, Revolution_1_objects, model.selection("EDGE", "Sketch_1/baseAxialLine_0"), 360, 0)

### Create Revolution
Revolution_2_objects = [model.selection("EDGE", "Sketch_1/baseRadialLine_0"),
                        model.selection("EDGE", "Sketch_1/upperContourLine_1"),
                        model.selection("EDGE", "Sketch_1/baseRadialLine_1")]
Revolution_2 = model.addRevolution(Part_1_doc, Revolution_2_objects, model.selection("EDGE", "Sketch_1/baseAxialLine_1"), 360, 0)

### Create Revolution
Revolution_3_objects = [model.selection("EDGE", "Sketch_1/baseRadialLine_1"),
                        model.selection("EDGE", "Sketch_1/upperContourLine_2"),
                        model.selection("EDGE", "Sketch_1/baseRadialLine_2")]
Revolution_3 = model.addRevolution(Part_1_doc, Revolution_3_objects, model.selection("EDGE", "Sketch_1/baseAxialLine_2"), 360, 0)

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, '/tmp/shaper_start_0.xao', model.selection("FACE", "Revolution_1_1"), 'XAO')

### Create Export
Export_2 = model.exportToXAO(Part_1_doc, '/tmp/shaper_TangentOgiveNose.xao', model.selection("FACE", "Revolution_1_2"), 'XAO')

### Create Export
Export_3 = model.exportToXAO(Part_1_doc, '/tmp/shaper_end_0.xao', model.selection("FACE", "Revolution_1_3"), 'XAO')

### Create Export
Export_4 = model.exportToXAO(Part_1_doc, '/tmp/shaper_start_0_1.xao', model.selection("FACE", "Revolution_2_1"), 'XAO')

### Create Export
Export_5 = model.exportToXAO(Part_1_doc, '/tmp/shaper_middle_1.xao', model.selection("FACE", "Revolution_2_2"), 'XAO')

### Create Export
Export_6 = model.exportToXAO(Part_1_doc, '/tmp/shaper_end_0_1.xao', model.selection("FACE", "Revolution_2_3"), 'XAO')

### Create Export
Export_7 = model.exportToXAO(Part_1_doc, '/tmp/shaper_start_1_2.xao', model.selection("FACE", "Revolution_3_1"), 'XAO')

### Create Export
Export_8 = model.exportToXAO(Part_1_doc, '/tmp/shaper_middle_2.xao', model.selection("FACE", "Revolution_3_2"), 'XAO')

### Create Export
Export_9 = model.exportToXAO(Part_1_doc, '/tmp/shaper_end_1_2.xao', model.selection("FACE", "Revolution_3_3"), 'XAO')

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Revolution_1_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1))
Revolution_1_2, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1, 1))
Revolution_1_3, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1, 2))
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

(imported, Revolution_1_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_start_0.xao")
(imported, Revolution_1_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_TangentOgiveNose.xao")
(imported, Revolution_1_3, [], [], []) = geompy.ImportXAO("/tmp/shaper_end_0.xao")
(imported, Revolution_2_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_start_0_1.xao")
(imported, Revolution_2_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_middle_1.xao")
(imported, Revolution_2_3, [], [], []) = geompy.ImportXAO("/tmp/shaper_end_0_1.xao")
(imported, Revolution_3_1, [], [], []) = geompy.ImportXAO("/tmp/shaper_start_1_2.xao")
(imported, Revolution_3_2, [], [], []) = geompy.ImportXAO("/tmp/shaper_middle_2.xao")
(imported, Revolution_3_3, [], [], []) = geompy.ImportXAO("/tmp/shaper_end_1_2.xao")
start_0 = geompy.CreateGroup(Revolution_1_1, geompy.ShapeType["FACE"])
geompy.UnionList(start_0, [Revolution_1_1])
TangentOgiveNose = geompy.CreateGroup(Revolution_1_2, geompy.ShapeType["FACE"])
geompy.UnionList(TangentOgiveNose, [Revolution_1_2])
middle_1 = geompy.CreateGroup(Revolution_2_2, geompy.ShapeType["FACE"])
geompy.UnionList(middle_1, [Revolution_2_2])
middle_2 = geompy.CreateGroup(Revolution_3_2, geompy.ShapeType["FACE"])
geompy.UnionList(middle_2, [Revolution_3_2])
end_1_2 = geompy.CreateGroup(Revolution_3_3, geompy.ShapeType["FACE"])
geompy.UnionList(end_1_2, [Revolution_3_3])
FuseProjectile = geompy.MakeFuseList([start_0, TangentOgiveNose, middle_1, middle_2, end_1_2], True, True)
Projectile = geompy.MakeSolid([FuseProjectile])
VertexCylinder = geompy.MakeVertex(-200, 0, 0)
geomObj_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
Cylinder = geompy.MakeCylinder(VertexCylinder, geomObj_1, 200, 416.2)
Domain = geompy.MakeCutList(Cylinder, [Projectile], True)
Farfield = geompy.CreateGroup(Domain, geompy.ShapeType["FACE"])
geompy.UnionIDs(Farfield, [3, 10, 12])
Projectile_1 = geompy.CreateGroup(Domain, geompy.ShapeType["FACE"])
geompy.UnionIDs(Projectile_1, [15, 22, 27, 32])
[Farfield, Projectile_1] = geompy.GetExistingSubObjects(Domain, False)
geompy.addToStudy( Revolution_1_1, 'Revolution_1_1' )
geompy.addToStudy( Revolution_1_2, 'Revolution_1_2' )
geompy.addToStudy( Revolution_1_3, 'Revolution_1_3' )
geompy.addToStudy( Revolution_2_1, 'Revolution_2_1' )
geompy.addToStudy( Revolution_2_2, 'Revolution_2_2' )
geompy.addToStudy( Revolution_2_3, 'Revolution_2_3' )
geompy.addToStudy( Revolution_3_1, 'Revolution_3_1' )
geompy.addToStudy( Revolution_3_2, 'Revolution_3_2' )
geompy.addToStudy( Revolution_3_3, 'Revolution_3_3' )
geompy.addToStudyInFather( Revolution_1_1, start_0, 'start_0' )
geompy.addToStudyInFather( Revolution_1_2, TangentOgiveNose, 'TangentOgiveNose' )
geompy.addToStudyInFather( Revolution_2_2, middle_1, 'middle_1' )
geompy.addToStudyInFather( Revolution_3_2, middle_2, 'middle_2' )
geompy.addToStudyInFather( Revolution_3_3, end_1_2, 'end_1_2' )
geompy.addToStudy( FuseProjectile, 'FuseProjectile' )
geompy.addToStudy( Projectile, 'Projectile' )
geompy.addToStudy( VertexCylinder, 'VertexCylinder' )
geompy.addToStudy( Cylinder, 'Cylinder' )
geompy.addToStudy( Domain, 'Domain' )
geompy.addToStudyInFather( Domain, Farfield, 'Farfield' )
geompy.addToStudyInFather( Domain, Projectile_1, 'Projectile' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Ogive_Test = smesh.Mesh(Domain,'Ogive_Test')
NETGEN_1D_2D = Ogive_Test.Triangle(algo=smeshBuilder.NETGEN_1D2D)
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
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(start_0, 4)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(TangentOgiveNose, 4)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(middle_1, 4)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(middle_2, 4)
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(end_1_2, 4)
NETGEN_2D_Parameters_1.SetMinSize( 0.1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 22050 )
NETGEN_3D = Ogive_Test.Tetrahedron()
NETGEN_3D_Parameters_1 = NETGEN_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 30 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 4 )
NETGEN_3D_Parameters_1.SetNbVolOptSteps( 4 )
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(start_0, 4)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(TangentOgiveNose, 4)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(middle_1, 4)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(middle_2, 4)
NETGEN_3D_Parameters_1.SetLocalSizeOnShape(end_1_2, 4)
NETGEN_3D_Parameters_1.SetMinSize( 0.1 )
NETGEN_3D_Parameters_1.SetElemSizeWeight( 4.67919e-310 )
Farfield_1 = Ogive_Test.GroupOnGeom(Farfield,'Farfield',SMESH.FACE)
Rocket = Ogive_Test.GroupOnGeom(Projectile_1,'Projectile',SMESH.FACE)
isDone = Ogive_Test.Compute()
[ Farfield_1, Rocket ] = Ogive_Test.GetGroups()
Viscous_Layers_1 = NETGEN_3D.ViscousLayers(1.5,20,1.2,[ 3, 10, 12 ],1,smeshBuilder.SURF_OFFSET_SMOOTH)
isDone = Ogive_Test.Compute()
[ Farfield_1, Rocket ] = Ogive_Test.GetGroups()
Ogive_Test.RenumberNodes()
Ogive_Test.RenumberElements()
[ Farfield_1, Rocket ] = Ogive_Test.GetGroups()


## Set names of Mesh objects
smesh.SetName(Rocket, 'Rocket')
smesh.SetName(Farfield_1, 'Farfield')
smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(Ogive_Test.GetMesh(), 'Ogive_Test')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(Viscous_Layers_1, 'Viscous Layers_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
