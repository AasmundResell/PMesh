from SketchAPI import *

from salome.shaper import model



from SketchAPI import *


#Parent class for all projectile sections
class Body:
  def __init__(self, bodyParam, sectionNumber):
    
    self.baseLength = bodyParam["bodyLength"]
    self.baseRadius = bodyParam["bodyRadius"]

    self.startRadius = None
    self.sectionNumber = sectionNumber
    
    self.faceID = None
    self.outerFacesID = None #Contain the id's for the faces that are exposed to flow  
    self.isEndSection = False

  def addSketchLines(self, Sketch, axialStartPoint):

    #Axial lines always defined from left to right
    self.baseAxialLine = Sketch.addLine(axialStartPoint,0,axialStartPoint + self.baseLength,0)
    
    #Radial lines always defined from center and out
    self.baseRadialLine = Sketch.addLine(axialStartPoint + self.baseLength,0,axialStartPoint + self.baseLength,self.baseRadius)
    
    self.baseAxialLine.setName("baseAxialLine_{}".format(self.sectionNumber))
    self.baseAxialLine.result().setName("baseAxialLine_{}".format(self.sectionNumber))

    self.baseRadialLine.setName("baseAxialLine_{}".format(self.sectionNumber))
    self.baseRadialLine.result().setName("baseRadialLine_{}".format(self.sectionNumber))


    #Constraints    
    Sketch.setHorizontal(self.baseAxialLine)
    Sketch.setVertical(self.baseRadialLine)

    #Ensure coindident points
    Sketch.setCoincident(self.baseAxialLine.endPoint(), self.baseRadialLine.startPoint())

    return Sketch

  def generateRevolutionBase(self):

      #Defines the right edge of the face that is revoluted
      radialLine = model.selection("EDGE","Sketch_1/baseRadialLine_{}".format(self.sectionNumber))

      #Defines the vector that the face is revoluted around 
      axialLine = model.selection("EDGE","Sketch_1/baseAxialLine_{}".format(self.sectionNumber))
      return radialLine,axialLine


  def renumberSection(self,newSectionNumber):
    self.sectionNumber = newSectionNumber
  
  def makeEndSection(self):

      self.isEndSection = True
      self.outerFacesID.append(len(self.faceID)-1) #Adds the back surface to the faces exposed to flow

class ConicNose(Body):    
    def __init__(self,noseParam,sectionNumber):
      Body.__init__(self,noseParam,sectionNumber)
      
      self.faceID = ["ConicNose","end_0"]    
      self.outerFacesID = [0]

    def addSketchLines(self,Sketch,axialStartPoint):

      Sketch = Body.addSketchLines(self,Sketch,axialStartPoint)

      self.noseConicLine = Sketch.addLine(self.baseLength,self.baseRadius,0,0)

      self.noseConicLine.setName("noseConicLine")
      self.noseConicLine.result().setName("noseConicLine")

      #Complete section for the nose
      Sketch.setCoincident(self.baseRadialLine.endPoint(),self.noseConicLine.startPoint())
      Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseConicLine.endPoint())


    def generateRevolution(self):

      revolution_selections = []
      

      revolution_selections.append(model.selection("EDGE","Sketch_1/noseConicLine"))
      
      radialLine, revolutionVector = Body.generateRevolutionBase(self)
      revolution_selections.append(radialLine)

      
      return revolution_selections,revolutionVector

class TangenOgiveNose(Body):
    
    def __init__(self,noseParam,sectionNumber):
      
      Body.__init__(self,noseParam,sectionNumber)
      self.outerFacesID = [0]
      
      self.faceID = ["TangentOgiveNose","end_0"]    
      assert (self.sectionNumber != 0); ValueError("Nose is always section zero")


      #TODO Implement additional functionality for ogive radius

    def addSketchLines(self,Sketch,axialStartPoint):

      Sketch = Body.addSketchLines(self,Sketch,axialStartPoint)

      #NEEDS TO BE IMPLEMENTED PROPERLY
      self.noseOgiveCurve = Sketch.addLine(self.baseLength,self.baseRadius,0,0)

      self.noseOgiveCurve.setName("noseOgiveCurve")
      self.noseOgiveCurve.result().setName("noseOgiveCurve")


      #Complete section for the nose
      Sketch.setCoincident(self.baseRadialLine.endPoint(),self.noseOgiveCurve.startPoint())
      Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseOgiveCurve.endPoint())
    
    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Body.generateRevolutionBase(self)

      revolution_selections.append(model.selection("EDGE","Sketch_1/noseOgiveCurve"))
      
      revolution_selections.append(radialLine)
      
      return revolution_selections,revolutionVector

           
class HorizontalSection(Body):    
    def __init__(self,bodyDict,sectionNumber):
      
      Body.__init__(self,bodyDict,sectionNumber)
      self.outerFacesID = [1]
      
      self.faceID = ["start_{0}_{1}".format(sectionNumber-1,sectionNumber),"middle_{}".format(sectionNumber),"end_{0}_{1}".format(sectionNumber-1,sectionNumber)]    
      
      self.startRadius = self.baseRadius
    
    def addSketchLines(self, Sketch, axialStartPoint):

      Sketch = Body.addSketchLines(self,Sketch,axialStartPoint)


      self.upperContourLine = Sketch.addLine(axialStartPoint,self.baseRadius,axialStartPoint + self.baseLength,self.baseRadius)
      
      self.upperContourLine.setName("upperContourLine_{}".format(self.sectionNumber))
      self.upperContourLine.result().setName("upperContourLine_{}".format(self.sectionNumber))

      Sketch.setHorizontal(self.upperContourLine)

      Sketch.setCoincident(self.baseRadialLine.endPoint(),self.upperContourLine.endPoint())

  
    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Body.generateRevolutionBase(self)

      #Defines the left edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/baseRadialLine_{}".format(self.sectionNumber-1)))
      
      #Defines the upper edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/upperContourLine_{}".format(self.sectionNumber))) 
      
      revolution_selections.append(radialLine)
      
      return revolution_selections,revolutionVector



class LinearTransitionSection(Body):    
    def __init__(self,bodyDict,sectionNumber):
      
      Body.__init__(self,bodyDict,sectionNumber)
      self.outerFacesID = [1]
      
      self.faceID = ["start_{0}_{1}".format(sectionNumber-1,sectionNumber),"middle_{}".format(sectionNumber),"end_{0}_{1}".format(sectionNumber-1,sectionNumber)]    
      
      self.startRadius = bodyDict["bodyRadiusFront"]
    

    def addSketchLines(self, Sketch, axialStartPoint):
      
      Sketch = Body.addSketchLines(self,Sketch,axialStartPoint)

      self.upperContourLine = Sketch.addLine(axialStartPoint,self.startRadius,axialStartPoint + self.baseLength,self.baseRadius)
      self.upperContourLine.setName("upperContourLine_{}".format(self.sectionNumber))
      self.upperContourLine.result().setName("upperContourLine_{}".format(self.sectionNumber))

      Sketch.setCoincident(self.baseRadialLine.endPoint(),self.upperContourLine.endPoint())


    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Body.generateRevolutionBase(self)
      
      #Defines the left edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/baseRadialLine_{}".format(self.sectionNumber-1)))

      #Defines the upper edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/upperContourLine_{}".format(self.sectionNumber))) 
      
      revolution_selections.append(radialLine)
      
      return revolution_selections,revolutionVector








    
