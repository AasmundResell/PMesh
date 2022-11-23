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
    Sketch.setHorizontal(self.baseAxialLine.result())
    Sketch.setVertical(self.baseRadialLine.result())

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
      
      if noseParams.get("sphericallyBluntedNose"):
        self.sphericalBluntedNose = True
      else:
        self.sphericalBluntedNose = False
      
      self.warningParameters(**noseParams)
      self.calculateGeometry(**noseParams)
        
      if self.frontRadius > 0.0 or self.sphericalBluntedNose: 
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


      #TODO: Consider making seperate class for spherically blunted tangent ogive
      #Defines geometrical parameters if spherically blunted nose is defined
      if self.sphericalBluntedNose:
        radius_sphere = noseParams.get("sphericallyBluntedNose").get("sphereRadius")
        
        
        (self.point_center_x, _ , offset , _, self.point_tangent_x,self.point_tangent_y) = calcSphereBluntedOgiveNose(self.rho,self.R,radius_sphere)
        
        #Subtract the offset to place noce tip in origo, the offset is the x coordinate of the front tip of the blunted nose
        
        #Subtract the offset to place noce tip in origo, the offset is the x coordinate of the front tip of the blunted nose
        self.baseLength = self.L - offset
        self.point_center_x = self.point_center_x - offset
        self.point_tangent_x = self.point_tangent_x - offset



    def warningParameters(self,**noseParams):
      """
      Warns the user if conflicting configurations are defined and which parameters
      that are overidden. 
      """

      if noseParams.get("tangentOgiveRadius") and (noseParams.get("meplatCutLength") or 
      noseParams.get("meplatRadius") or noseParams.get("frontRadius")):
        Warning('Any defined nose cutting parameters is overriden by the tangent ogive radius!')
      else:
        print("HEi")

      if self.sphericalBluntedNose:
        try:
         r = noseParams.get("sphericallyBluntedNose").get("sphereRadius")
        except:
          RuntimeError('Sphere radius must be defined when spherically blunted nose is defined')


    def addSketchLines(self,Sketch,axialStartPoint):

      
      Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)
      
      #Assuming absolute values specify the tangent ogive nose
      if self.sphericalBluntedNose:

     


        ### Create SketchLine
        self.baseRadialLine = Sketch.addLine(self.baseLength, 0, self.baseLength, self.baseRadius)
        
        Sketch.setVerticalDistance(self.baseAxialLine.endPoint(), self.baseRadialLine.endPoint(), self.baseRadius)

        ### Create SketchLine
        self.supportLineNose = Sketch.addLine(self.point_tangent_x, 0, self.point_tangent_x, self.point_tangent_y)
        self.supportLineNose.setName("supportLineNose")
        self.supportLineNose.result().setName("supportLineNose")
        Sketch.setVertical(self.supportLineNose.result())

        ### Create SketchPoint
        self.tangentNosePoint = Sketch.addPoint(self.point_tangent_x, self.point_tangent_y)
        self.tangentNosePoint.setName("tangentNosePoint")
        self.tangentNosePoint.result().setName("tangentNosePoint")
        Sketch.setCoincident(self.supportLineNose.endPoint(), self.tangentNosePoint.coordinates())

        ### Create SketchLine
        self.supportLineOgive = Sketch.addLine(self.baseLength, 0, self.baseLength, self.baseRadius-self.rho)
        self.supportLineOgive.setName("supportLineOgive")
        self.supportLineOgive.result().setName("supportLineOgive")
        Sketch.setCoincident(self.baseAxialLine.endPoint(), self.supportLineOgive.startPoint())
        Sketch.setVertical(self.supportLineOgive.result())
        Sketch.setVerticalDistance(self.supportLineOgive.startPoint(), self.supportLineOgive.endPoint(), self.rho-self.baseRadius)

        ### Create SketchPoint
        self.supportPointNose = Sketch.addPoint(self.point_tangent_x, 0)
        self.supportPointNose.setName("supportPointNose")
        self.supportPointNose.result().setName("supportPointNose")
        Sketch.setCoincident(self.supportLineNose.startPoint(), self.supportPointNose.coordinates())

        ### Create SketchPoint
        self.supportPointOgive = Sketch.addPoint(self.baseLength, self.baseRadius)
        self.supportPointOgive.setName("supportPointOgive")
        self.supportPointOgive.result().setName("supportPointOgive")
        Sketch.setCoincident(self.baseRadialLine.endPoint(), self.supportPointOgive.coordinates())
        Sketch.setVerticalDistance(self.supportPointNose.coordinates(), self.supportLineNose.endPoint(), self.point_tangent_y)

        ### Create SketchArc
        self.noseBluntArc = Sketch.addArc(self.point_center_x, 0, self.point_tangent_x, self.point_tangent_y, 0, 0, False)
        Sketch.setCoincident(self.supportLineNose.endPoint(), self.noseBluntArc.startPoint())
        Sketch.setCoincident(self.noseBluntArc.endPoint(), self.baseAxialLine.result())

        ### Create SketchArc
        self.noseOgiveArc = Sketch.addArc(self.baseLength, self.baseRadius-self.rho, self.point_tangent_x,self.point_tangent_y, self.baseLength, self.baseRadius, True)
        Sketch.setCoincident(self.supportLineOgive.endPoint(), self.noseOgiveArc.center())
        Sketch.setCoincident(self.supportLineNose.endPoint(), self.noseOgiveArc.startPoint())
        Sketch.setCoincident(self.baseRadialLine.result(), self.noseOgiveArc.endPoint())
 


        
      else:
        Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)
        self.noseOgiveArc = Sketch.addArc(self.baseLength, self.baseRadius-self.rho, 0.0, self.frontRadius, self.baseLength, self.baseRadius, True)
        self.noseBluntArc = None
    
        Sketch.setCoincident(self.baseRadialLine.endPoint(),self.noseOgiveArc.endPoint())
      

      if self.frontRadius > 0.0 and not self.sphericalBluntedNose:
      
        self.noseFrontLine = Sketch.addLine(0,0,0,self.frontRadius)
        Sketch.setVertical(self.noseFrontLine)

        self.noseFrontLine.setName("noseFrontLine")
        self.noseFrontLine.result().setName("noseFrontLine")

        #Complete section for the nose
        Sketch.setCoincident(self.noseFrontLine.endPoint(),self.noseOgiveArc.startPoint())
        Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseFrontLine.startPoint())
      #else:
        #Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseOgiveArc.startPoint())
        


    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Section.generateRevolutionBase(self)
      if self.sphericalBluntedNose:
        revolution_selections.append(model.selection("EDGE","Sketch_1/SketchArc_1_2"))  
        revolution_selections.append(model.selection("EDGE","Sketch_1/SketchArc_2_2"))  
      else:
        if self.frontRadius > 0.0 and not self.sphericalBluntedNose:
          revolution_selections.append(model.selection("EDGE","Sketch_1/noseFrontLine"))
      
        revolution_selections.append(model.selection("EDGE","Sketch_1/noseOgiveCurve"))
      
      revolution_selections.append(radialLine)
      
      return revolution_selections,revolutionVector

    
class SecantOgiveNose(Section):
    
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
      
      self.faceID = ["start_{0}_{1}".format(sectionNumber-1,sectionNumber),"middle_{}".format(sectionNumber),"end_{0}_{1}".format(sectionNumber,sectionNumber+1)]    
      
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
      
      self.faceID = ["start_{0}_{1}".format(sectionNumber-1,sectionNumber),"middle_{}".format(sectionNumber),"end_{0}_{1}".format(sectionNumber,sectionNumber+1)]    
      
    

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








    
