#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.9.0 with dump python functionality
###
if __name__ == "__main__":
  from salome.shaper import model

  model.begin()
  partSet = model.moduleDocument()

  ### Create Part
  Part_1 = model.addPart(partSet)
  Part_1_doc = Part_1.document()

  ### Create Sketch
  Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
  import sys
  import salome

  salome.salome_init()
  import salome_notebook
  notebook = salome_notebook.NoteBook()
  sys.path.insert(0, r'/home/asmund/dev/PMesh/Scripts')

  ###
  ### SHAPER component
  ###


  ### Create SketchLine
  SketchLine_1 = Sketch_1.addLine(0, 0, 43.39721792890265, 29.81607418856261)

  ### Create SketchProjection
  SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
  SketchPoint_1 = SketchProjection_1.createdFeature()
  Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchPoint_1.result())

  ### Create SketchLine
  SketchLine_2 = Sketch_1.addLine(43.39721792890265, 29.81607418856261, 43.39721792890265, 0)
  Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())

  ### Create SketchLine
  SketchLine_3 = Sketch_1.addLine(43.39721792890265, 0, 0, 0)

  SketchLine_3.setName("noseOgiveCurve")
  SketchLine_3.result().setName("noseOgiveCurve")

  Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
  Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_3.endPoint())
  Sketch_1.setHorizontal(SketchLine_3.result())
  Sketch_1.setVertical(SketchLine_2.result())

  ### Create SketchLine
  SketchLine_4 = Sketch_1.addLine(43.39721792890265, 29.81607418856261, 81.79907264296753, 29.81607418856261)
  Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_4.startPoint())
  Sketch_1.setHorizontal(SketchLine_4.result())

  ### Create SketchLine
  SketchLine_5 = Sketch_1.addLine(81.79907264296753, 29.81607418856261, 81.79907264296753, 0)
  Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())
  Sketch_1.setVertical(SketchLine_5.result())

  ### Create SketchLine
  SketchLine_6 = Sketch_1.addLine(81.79907264296753, 0, 43.39721792890265, 0)
  Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())
  Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_6.endPoint())
  Sketch_1.setHorizontal(SketchLine_6.result())

  ### Create SketchLine
  SketchLine_7 = Sketch_1.addLine(81.79907264296753, 29.81607418856261, 120.8253477588871, 40.43122102009275)
  Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_7.startPoint())

  ### Create SketchLine
  SketchLine_8 = Sketch_1.addLine(120.8253477588871, 40.43122102009275, 120.8253477588871, -0.1561051004636752)
  Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
  Sketch_1.setVertical(SketchLine_8.result())

  ### Create SketchLine
  SketchLine_9 = Sketch_1.addLine(120.8253477588871, -0.1561051004636752, 82.11128284389493, -0.1561051004636752)
  Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
  Sketch_1.setHorizontal(SketchLine_9.result())
  model.do()

  ### Create Revolution
  Revolution_1_objects = [model.selection("EDGE", "Sketch_1/SketchLine_1"),
                          model.selection("EDGE", "Sketch_1/SketchLine_2")]
  vec1 = model.selection("EDGE", "Sketch_1/noseOgiveCurve")

  Revolution_1 = model.addRevolution(Part_1_doc, Revolution_1_objects, vec1 , 360, 0)

  ### Create Revolution
  Revolution_2_objects = [model.selection("EDGE", "Sketch_1/SketchLine_2"),
                          model.selection("EDGE", "Sketch_1/SketchLine_5"),
                          model.selection("EDGE", "Sketch_1/SketchLine_4")]

  vec2 = model.selection("EDGE", "Sketch_1/SketchLine_9")
  Revolution_2 = model.addRevolution(Part_1_doc, Revolution_2_objects, vec2, 360, 0)

  ### Create Revolution
  Revolution_3_objects = [model.selection("EDGE", "Sketch_1/SketchLine_7"),
                          model.selection("EDGE", "Sketch_1/SketchLine_8"),
                          model.selection("EDGE", "Sketch_1/SketchLine_5")]
  vec3 = model.selection("EDGE", "Sketch_1/SketchLine_9")

  Revolution_3 = model.addRevolution(Part_1_doc, Revolution_3_objects,vec3 , 360, 0)

  model.end()

  ###
  ### SHAPERSTUDY component
  ###

  model.publishToShaperStudy()
  import SHAPERSTUDY
  Revolution_1_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1))
  Revolution_2_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_2))
  Revolution_3_1, = SHAPERSTUDY.shape(model.featureStringId(Revolution_3))
  Revolution_3_2, = SHAPERSTUDY.shape(model.featureStringId(Revolution_3, 1))
  Revolution_3_3, = SHAPERSTUDY.shape(model.featureStringId(Revolution_3, 2))

  if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()
