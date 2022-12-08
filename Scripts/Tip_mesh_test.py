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
Vertex_1 = geompy.MakeVertex(0, 0, -200)
Cone_1 = geompy.MakeConeR1R2H(100, 0, 300)
[geomObj_1,geomObj_2] = geompy.SubShapeAll(Cone_1, geompy.ShapeType["FACE"])
[geomObj_3,geomObj_4] = geompy.SubShapeAll(Cone_1, geompy.ShapeType["FACE"])
Cylinder_1 = geompy.MakeCylinder(Vertex_1, OZ, 200, 600)
[geomObj_5,geomObj_6,geomObj_7] = geompy.SubShapeAll(Cylinder_1, geompy.ShapeType["FACE"])
[geomObj_8,geomObj_9,geomObj_10] = geompy.SubShapeAll(Cylinder_1, geompy.ShapeType["FACE"])
Cut_1 = geompy.MakeCutList(Cylinder_1, [Cone_1], True)
geomObj_11 = geompy.GetInPlace(Cut_1, Cylinder_1, True)
[geomObj_12,geomObj_13,geomObj_14,geomObj_15,geomObj_16] = geompy.SubShapeAll(geomObj_11, geompy.ShapeType["FACE"])
farfield = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(farfield, [3, 10, 12])
projectile = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(projectile, [15, 22])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Cone_1, 'Cone_1' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudyInFather( Cut_1, farfield, 'farfield' )
geompy.addToStudyInFather( Cut_1, projectile, 'projectile' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
