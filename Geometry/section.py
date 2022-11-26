from SketchAPI import *

from salome.shaper import model

from Geometry.geometryFunctions import *

from SketchAPI import *


#Parent class for all projectile sections
class Section:
  def __init__(self, sectionNumber,**bodyParam ):
    
    self.baseLength = bodyParam.get("bodyLength")
    self.baseRadius = bodyParam.get("radiusBase")

    
    if bodyParam.get("radiusFront"):
      self.frontRadius = bodyParam["radiusFront"]
    elif bodyParam.get("meplatRadius"):
      self.frontRadius = bodyParam["meplatRadius"]
    else:
      self.frontRadius = None  
    
    self.sectionNumber = sectionNumber
    
    self.faceID = None #Contain the face names for each face of the geometry
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
      
      #Adds the rear surface to the geometry
      self.faceID.append("rear_{}".format(self.sectionNumber)) 

class ConicNose(Section):    
    def __init__(self,sectionNumber,**noseParam):
      Section.__init__(self,sectionNumber,**noseParam)
      
      
      if self.frontRadius is None:
        self.calculateFrontRadius(noseParam)
      
      if self.frontRadius > 0.0:
        self.faceID = ["start_0","ConicNose"] 
      elif self.frontRadius == 0.0:
        self.faceID = ["ConicNose"] 
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

      if self.isEndSection:
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
        self.faceID = ["start_0","TangentOgiveNose"]    
      elif self.frontRadius == 0.0:
        self.faceID = ["TangentOgiveNose"]    
      else:
        raise RuntimeError("Front radius of TangentOgiveNose most be zero or a postive number")
    
      
    def calculateGeometry(self,**noseParams): 

      import copy

      #See: https://en.wikipedia.org/wiki/Nose_cone_design#Tangent_ogive for reference to variables info

      
      R = copy.deepcopy(self.baseRadius) #Base radius is unambiguously defined

      if noseParams.get("tangentOgiveRadius"):
        self.rho = noseParams.get("tangentOgiveRadius")
        L = calcTangentOgiveLength(self.rho,R) #If rho is defined, L is unambiguously defined

        #Any defined front radius is overriden when rho is specified
        if self.baseLength > self.L:
          self.baseLength = self.L
          self.frontRadius = 0.0
        else: 
            self.frontRadius = calcTangentOgiveY(self.rho, R, L - self.baseLength)

      else: #If rho is not defined in config file
        L = copy.deepcopy(self.baseLength) #In this case, the original base length is always equal to L
        self.rho = calcTangentOgiveRadius(L ,R )
        
        if noseParams.get("meplatCutLength"):
          l = noseParams.get("meplatCutLength")
          self.frontRadius = calcTangentOgiveY(self.rho, R, L - l)
        elif self.frontRadius > 0.0:
          l = calcTangentOgiveX(self.rho, R, self.frontRadius)
        else: #No tip cut defined
          l = 0.0
          self.frontRadius = 0.0

        self.baseLength = L - l 

      
      if self.sphericalBluntedNose:
        radius_sphere = noseParams.get("sphericallyBluntedNose").get("sphereRadius")
        
        
        (self.point_center_x, _ , offset , _, self.point_tangent_x,self.point_tangent_y) = calcSphereBluntedOgiveNose(self.rho,R,radius_sphere)
        
        #Subtract the offset to place noce tip in origo, the offset is the x coordinate of the front tip of the blunted nose
        
        #Subtract the offset to place noce tip in origo, the offset is the x coordinate of the front tip of the blunted nose
        self.baseLength = L - offset
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
      
      if self.sphericalBluntedNose and (noseParams.get("meplatCutLength") or 
      noseParams.get("meplatRadius") or noseParams.get("frontRadius")):
        Warning('Any defined nose cutting parameters is overriden by the spherically blunted nose!')

      if self.sphericalBluntedNose:
        try:
         r = noseParams.get("sphericallyBluntedNose").get("sphereRadius")
        except:
          RuntimeError('Sphere radius must be defined when spherically blunted nose is defined')


    def addSketchLines(self,Sketch,axialStartPoint):

      
      Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)
      
      if self.sphericalBluntedNose:

        #Blunted tip arch
        self.noseBluntArc = Sketch.addArc(self.point_center_x, 0, self.point_tangent_x, self.point_tangent_y, 0, 0, False)
        Sketch.setCoincident(self.noseBluntArc.endPoint(), self.baseAxialLine.result())

        #Tangent ogive nose arc
        self.noseOgiveArc = Sketch.addArc(self.baseLength, self.baseRadius-self.rho, self.point_tangent_x,self.point_tangent_y, self.baseLength, self.baseRadius, True)
        
        Sketch.setCoincident(self.baseRadialLine.result(), self.noseOgiveArc.endPoint())
 
      else:
        Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)
        self.noseOgiveArc = Sketch.addArc(self.baseLength, self.baseRadius-self.rho, 0.0, self.frontRadius, self.baseLength, self.baseRadius, True)
        self.noseBluntArc = None
    
        Sketch.setCoincident(self.baseRadialLine.endPoint(),self.noseOgiveArc.endPoint())
    
        if self.frontRadius > 0.0:
        
          self.noseFrontLine = Sketch.addLine(0,0,0,self.frontRadius)
          Sketch.setVertical(self.noseFrontLine)

          self.noseFrontLine.setName("noseFrontLine")
          self.noseFrontLine.result().setName("noseFrontLine")

          #Complete section for the nose
          Sketch.setCoincident(self.noseFrontLine.endPoint(),self.noseOgiveArc.startPoint())
          Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseFrontLine.startPoint())
        


    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Section.generateRevolutionBase(self)
      if self.sphericalBluntedNose:
        revolution_selections.append(model.selection("EDGE","Sketch_1/SketchArc_1_2"))  
        revolution_selections.append(model.selection("EDGE","Sketch_1/SketchArc_2_2"))  
      else:
        if self.frontRadius > 0.0 and not self.sphericalBluntedNose:
          revolution_selections.append(model.selection("EDGE","Sketch_1/noseFrontLine"))
      
        revolution_selections.append(model.selection("EDGE","Sketch_1/SketchArc_1_2"))

      if self.isEndSection:
        revolution_selections.append(radialLine)

      return revolution_selections,revolutionVector

class SecantOgiveNose(Section):
    
    def __init__(self,sectionNumber,**noseParams):
      Section.__init__(self,sectionNumber,**noseParams)
      
      if noseParams.get("sphericallyBluntedNose"):
        self.sphericalBluntedNose = True
      else:
        self.sphericalBluntedNose = False
      
      self.warningParameters(**noseParams)
      self.calculateGeometry(**noseParams)
        
      if self.frontRadius > 0.0 or self.sphericalBluntedNose: 
        self.faceID = ["start_0","SecantOgiveNose"]    
      elif self.frontRadius == 0.0:
        self.faceID = ["SecantOgiveNose"]    
      else:
        raise RuntimeError("Front radius of SecantOgiveNose most be zero or a postive number")
    
      
    def calculateGeometry(self,**noseParams): 

      import copy

      #See: https://en.wikipedia.org/wiki/Nose_cone_design#Tangent_ogive for reference to variables info

      R = copy.deepcopy(self.baseRadius) #Base radius is unambiguously defined
      L = copy.deepcopy(self.baseLength) #Base radius is unambiguously defined
      
      self.rho = noseParams.get("secantOgiveRadius")
      
      #Calculate base tangent ogive parameters
      alpha = calcSecantOgiveAlpha(self.rho,R,L)
      self.R_0 = self.rho - self.rho*sin(alpha)
      self.L_0 = self.rho*cos(alpha)
        
        
      if noseParams.get("meplatCutLength"):
        x = noseParams.get("meplatCutLength")
        self.frontRadius = calcSecantOgiveY(self.rho, R, L, x )
      elif self.frontRadius is not None :
        if self.frontRadius > 0.0:
          l = calcSecantOgiveX(self.rho, R, L, self.frontRadius)
        else:
          Warning("Front radius of the nose must be positive!")
      else: #No tip cut defined
        l = 0.0
        self.frontRadius = 0.0
      self.baseLength = L - l  


      if self.sphericalBluntedNose:

        radius_sphere = noseParams.get("sphericallyBluntedNose").get("sphereRadius")
        (self.point_center_x, _ , offset , _, self.point_tangent_x,self.point_tangent_y) = calcSphereBluntedOgiveNose(
          self.rho, self.R_0, radius_sphere)
        
        #Subtract the offset to place noce tip in origo, the offset is the x coordinate of the front tip of the blunted nose
        self.baseLength = L - offset
        self.L_0 = self.L_0 - offset
        self.point_center_x = self.point_center_x - offset
        self.point_tangent_x = self.point_tangent_x - offset



    def warningParameters(self,**noseParams):
      """
      Warns the user if conflicting configurations are defined and which parameters
      that are overidden. 
      """
      if not noseParams.get("secantOgiveRadius"):
        RuntimeError('Secant radius must be specified for the secant ogive nose')

      if self.sphericalBluntedNose and (noseParams.get("meplatCutLength") or 
        noseParams.get("meplatRadius") or noseParams.get("frontRadius")):
        Warning('Any defined nose cutting parameters is overriden by the spherically blunted nose!')

      
      if self.sphericalBluntedNose:
        try:
         r = noseParams.get("sphericallyBluntedNose").get("sphereRadius")
        except:
          RuntimeError('Sphere radius must be defined when spherically blunted nose is defined')


    def addSketchLines(self,Sketch,axialStartPoint):

      
      Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)
      
      if self.sphericalBluntedNose:

        self.noseBluntArc = Sketch.addArc(self.point_center_x, 0, self.point_tangent_x, self.point_tangent_y, 0, 0, False)
        Sketch.setCoincident(self.noseBluntArc.endPoint(), self.baseAxialLine.result())

        #Secant ogive nose arc
        self.noseOgiveArc = Sketch.addArc(self.L_0, self.R_0-self.rho, self.point_tangent_x,self.point_tangent_y, self.baseLength, self.baseRadius, True)
        
        Sketch.setCoincident(self.baseRadialLine.result(), self.noseOgiveArc.endPoint())

        #Blunted tip arch
        self.noseBluntArc = Sketch.addArc(self.point_center_x, 0, self.point_tangent_x, self.point_tangent_y, 0, 0, False)
        Sketch.setCoincident(self.baseRadialLine.result(), self.noseOgiveArc.endPoint())
 
      else:
        
        self.noseOgiveArc = Sketch.addArc(self.L_0, self.R_0-self.rho, 0.0, self.frontRadius, self.baseLength, self.baseRadius, True)
        self.noseBluntArc = None
    
        Sketch.setCoincident(self.baseRadialLine.endPoint(),self.noseOgiveArc.endPoint())
      

        if self.frontRadius > 0.0:
      
          self.noseFrontLine = Sketch.addLine(0,0,0,self.frontRadius)
          Sketch.setVertical(self.noseFrontLine)

          self.noseFrontLine.setName("noseFrontLine")
          self.noseFrontLine.result().setName("noseFrontLine")

          #Complete section for the nose
          Sketch.setCoincident(self.noseFrontLine.endPoint(),self.noseOgiveArc.startPoint())
          Sketch.setCoincident(self.baseAxialLine.startPoint(),self.noseFrontLine.startPoint())
        


    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Section.generateRevolutionBase(self)
      if self.sphericalBluntedNose:
        revolution_selections.append(model.selection("EDGE","Sketch_1/SketchArc_1_2"))  
        revolution_selections.append(model.selection("EDGE","Sketch_1/SketchArc_2_2"))  
      else:
        if self.frontRadius > 0.0 and not self.sphericalBluntedNose:
          revolution_selections.append(model.selection("EDGE","Sketch_1/noseFrontLine"))
      
        revolution_selections.append(model.selection("EDGE","Sketch_1/SketchArc_1_2"))
      
      if self.isEndSection:
        revolution_selections.append(radialLine)

      return revolution_selections,revolutionVector

               
class HorizontalSection(Section):    
    def __init__(self,sectionNumber,**bodyParams):
      
      baseRadius = bodyParams.get("radiusRear")

      bodyParams["radiusFront"]=baseRadius

      Section.__init__(self,sectionNumber,**bodyParams)


      self.faceID = ["middle_{}".format(sectionNumber)]    
      
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

 
      #Defines the upper edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/upperContourLine_{}".format(self.sectionNumber))) 
      
      if self.isEndSection:
        revolution_selections.append(radialLine)

      return revolution_selections,revolutionVector



class LinearTransitionSection(Section):    
    def __init__(self,sectionNumber,**bodyParams):
  
      Section.__init__(self,sectionNumber,**bodyParams)
      
      self.faceID = ["middle_{}".format(sectionNumber)]    
      
    

    def addSketchLines(self, Sketch, axialStartPoint):
      
      Sketch = Section.addSketchLines(self,Sketch,axialStartPoint)

      self.upperContourLine = Sketch.addLine(axialStartPoint,self.frontRadius,axialStartPoint + self.baseLength,self.baseRadius)
      self.upperContourLine.setName("upperContourLine_{}".format(self.sectionNumber))
      self.upperContourLine.result().setName("upperContourLine_{}".format(self.sectionNumber))

      Sketch.setCoincident(self.baseRadialLine.endPoint(),self.upperContourLine.endPoint())


    def generateRevolution(self):

      revolution_selections = []
      
      radialLine, revolutionVector = Section.generateRevolutionBase(self)
      
      #Defines the upper edge of the face that is revoluted
      revolution_selections.append(model.selection("EDGE","Sketch_1/upperContourLine_{}".format(self.sectionNumber))) 
      
      if self.isEndSection:
        revolution_selections.append(radialLine)

      return revolution_selections,revolutionVector








    
