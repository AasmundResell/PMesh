from SketchAPI import *

from salome.shaper import model

from Geometry.geometryFunctions import *

from SketchAPI import *


#Parent class for all projectile sections
class Section:
  def __init__(self, sectionNumber,**bodyParam ):
    
    self.baseLength = bodyParam.get("bodyLength")
    self.baseRadius = bodyParam.get("bodyRadius")

    
    if bodyParam.get("bodyRadiusFront"):
      self.frontRadius = bodyParam["bodyRadiusFront"]
    elif bodyParam.get("meplatRadius"):
      self.frontRadius = bodyParam["meplatRadius"]
    else:
      self.frontRadius = None  
    
    self.sectionNumber = sectionNumber
    
    self.faceID = None #Contain the face names for each face of the section
    self.outerFacesID = None #Contain the id numbers for the faces that are exposed to flow  
    self.isEndSection = False #Set to true if the section is the rear section of the projectile 

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

class ConicNose(Section):    
    def __init__(self,sectionNumber,**noseParam):
      Section.__init__(self,sectionNumber,**noseParam)
      
      
      if self.frontRadius is None:
        self.calculateFrontRadius(noseParam)
      
      if self.frontRadius > 0.0: 
        self.outerFacesID = [0,1]
        self.faceID = ["start_0","ConicNose","end_0"] 
      elif self.frontRadius == 0.0:
        self.outerFacesID = [0]
        self.faceID = ["ConicNose","end_0"] 
      else:
        raise RuntimeError("Front radius of ConicNose most be zero or a postive number")
    

    def calculateFrontRadius(self,**noseParam):      
      if noseParam.get("meplatCutLength"):
        cutLenght = noseParam.get("meplatCutLength")
        if noseParam.get("cutNoseBy") == "Absolute" or not noseParam.get("cutNoseBy"): #Absolute if not defined
          self.frontRadius = self.baseRadius/(self.baseLength + cutLenght)*cutLenght
        elif noseParam.get("meplatCutLength") and noseParam.get("cutNoseBy") == "Relative":
          self.frontRadius = self.baseRadius/self.baseLength*cutLenght
          self.baseAxialLine = self.baseAxialLine - cutLenght
      #elif noseParam.get("conicNoseAngle") TODO
      else:
        self.frontRadius = 0.0

      

    def addSketchLines(self,Sketch,axialStartPoint):

      Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)

      self.noseConicLine = Sketch.addLine(self.baseLength,self.baseRadius,0,self.frontRadius)

      self.noseConicLine.setName("noseConicLine")
      self.noseConicLine.result().setName("noseConicLine")

      Sketch.setCoincident(self.baseRadialLine.endPoint(),self.noseConicLine.startPoint())
      
      if self.frontRadius > 0.0:
        self.noseFrontLine = Sketch.addLine(0,0,0,self.frontRadius)
        Sketch.setVertical(self.noseFrontLine)

        self.noseFrontLine.setName("noseFrontLine")
        self.noseFrontLine.result().setName("noseFrontLine")
      
        Sketch.setCoincident(self.noseFrontLine.endPoint(),self.noseConicLine.endPoint())
        Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseFrontLine.startPoint())
      else:
        Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseConicLine.endPoint())

        

    def generateRevolution(self):

      revolution_selections = []
      
      revolution_selections.append(model.selection("EDGE","Sketch_1/noseFrontLine"))
      
      revolution_selections.append(model.selection("EDGE","Sketch_1/noseConicLine"))
      
      radialLine, revolutionVector = Section.generateRevolutionBase(self)
      revolution_selections.append(radialLine)

      
      return revolution_selections,revolutionVector

    
class TangenOgiveNose(Section):
    
    def __init__(self,sectionNumber,**noseParams):
      Section.__init__(self,sectionNumber,**noseParams)
      
      
      self.calculateGeometry(**noseParams)
      
      if self.frontRadius > 0.0: 
        self.outerFacesID = [0,1]
        self.faceID = ["start_0","TangentOgiveNose","end_0"]    
      elif self.frontRadius == 0.0:
        self.outerFacesID = [0]
        self.faceID = ["TangentOgiveNose","end_0"]    
      else:
        raise RuntimeError("Front radius of TangentOgiveNose most be zero or a postive number")
    
      
    def calculateGeometry(self,**noseParams): 

      import copy

      #See: https://en.wikipedia.org/wiki/Nose_cone_design#Tangent_ogive for reference to variables info

      self.R = copy.deepcopy(self.baseRadius) #Base radius is unambiguously defined

      if noseParams.get("tangentOgiveRadius"):
        self.rho = noseParams.get("tangentOgiveRadius")
        self.L = calcTangentOgiveLength(self.rho,self.R) #If rho is defined, L is unambiguously defined

        #Any defined front radius is overriden when rho is specified
        if self.baseLength > self.L:
          self.baseLength = self.L
          self.frontRadius = 0.0
        else: 
            self.frontRadius = calcTangentOgiveY(self.rho,self.R,self.L - self.baseLength)

      else: #If rho is not defined in config file
        self.L = copy.deepcopy(self.baseLength) #In this case, the original base length is always equal to L
        self.rho = calcTangentOgiveRadius(self.L,self.R)
        
        if noseParams.get("meplatCutLength"):
          l = noseParams.get("meplatCutLength")
          self.frontRadius = calcTangentOgiveY(self.rho,self.R,self.L - l)
        elif self.frontRadius > 0.0:
          l = calcTangentOgiveX(self.rho,self.R,self.frontRadius)
        else: #No tip cut defined
          l = 0.0
          self.frontRadius = 0.0
        self.baseLength = self.L - l  


    def addSketchLines(self,Sketch,axialStartPoint):

      Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)


      #Assuming absolute values specify the tangent ogive nose


      self.noseOgiveArc = Sketch.addArc(self.baseLength, self.baseRadius-self.rho, 0.0, self.frontRadius, self.baseLength, self.baseRadius, True)
      self.noseOgiveArc.setName("noseCurve")
      self.noseOgiveArc.results()[1].setName("noseOgiveCurve")
      self.noseOgiveArc.result().setName("noseCurve")

      Sketch.setCoincident(self.baseRadialLine.endPoint(),self.noseOgiveArc.endPoint())
      
      if self.frontRadius > 0.0:
      
        self.noseFrontLine = Sketch.addLine(0,0,0,self.frontRadius)
        Sketch.setVertical(self.noseFrontLine)

        self.noseFrontLine.setName("noseFrontLine")
        self.noseFrontLine.result().setName("noseFrontLine")

        #Complete section for the nose
        Sketch.setCoincident(self.noseFrontLine.endPoint(),self.noseOgiveArc.startPoint())
        Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseFrontLine.startPoint())
      else:
        Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseOgiveArc.startPoint())
        


    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Section.generateRevolutionBase(self)

      revolution_selections.append(model.selection("EDGE","Sketch_1/noseFrontLine"))
      
      revolution_selections.append(model.selection("EDGE","Sketch_1/noseOgiveCurve"))
      
      revolution_selections.append(radialLine)
      
      return revolution_selections,revolutionVector

           
class HorizontalSection(Section):    
    def __init__(self,sectionNumber,**bodyParams):
      
      baseRadius = bodyParams.get("bodyRadius")

      bodyParams["bodyRadiusFront"]=baseRadius

      Section.__init__(self,sectionNumber,**bodyParams)
      self.outerFacesID = [1]
      
      self.faceID = ["start_{0}_{1}".format(sectionNumber-1,sectionNumber),"middle_{}".format(sectionNumber),"end_{0}_{1}".format(sectionNumber-1,sectionNumber)]    
      
      self.frontRadius = self.baseRadius
    
    def addSketchLines(self, Sketch, axialStartPoint):

      Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)


      self.upperContourLine = Sketch.addLine(axialStartPoint,self.baseRadius,axialStartPoint + self.baseLength,self.baseRadius)
      
      self.upperContourLine.setName("upperContourLine_{}".format(self.sectionNumber))
      self.upperContourLine.result().setName("upperContourLine_{}".format(self.sectionNumber))

      Sketch.setHorizontal(self.upperContourLine)

      Sketch.setCoincident(self.baseRadialLine.endPoint(),self.upperContourLine.endPoint())

  
    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Section.generateRevolutionBase(self)

      #Defines the left edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/baseRadialLine_{}".format(self.sectionNumber-1)))
      
      #Defines the upper edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/upperContourLine_{}".format(self.sectionNumber))) 
      
      revolution_selections.append(radialLine)
      
      return revolution_selections,revolutionVector



class LinearTransitionSection(Section):    
    def __init__(self,sectionNumber,**bodyParams):
  
      Section.__init__(self,sectionNumber,**bodyParams)
      self.outerFacesID = [1]
      
      self.faceID = ["start_{0}_{1}".format(sectionNumber-1,sectionNumber),"middle_{}".format(sectionNumber),"end_{0}_{1}".format(sectionNumber-1,sectionNumber)]    
      
    

    def addSketchLines(self, Sketch, axialStartPoint):
      
      Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)

      self.upperContourLine = Sketch.addLine(axialStartPoint,self.frontRadius,axialStartPoint + self.baseLength,self.baseRadius)
      self.upperContourLine.setName("upperContourLine_{}".format(self.sectionNumber))
      self.upperContourLine.result().setName("upperContourLine_{}".format(self.sectionNumber))

      Sketch.setCoincident(self.baseRadialLine.endPoint(),self.upperContourLine.endPoint())


    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Section.generateRevolutionBase(self)
      
      #Defines the left edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/baseRadialLine_{}".format(self.sectionNumber-1)))

      #Defines the upper edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/upperContourLine_{}".format(self.sectionNumber))) 
      
      revolution_selections.append(radialLine)
      
      return revolution_selections,revolutionVector








    
