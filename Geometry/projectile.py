
from salome.shaper import model

from Geometry.section import ConicNose, TangenOgiveNose, SecantOgiveNose, HorizontalSection, LinearTransitionSection 

class ProjectileModel:
    def __init__(self):
    
        model.begin()

        self.partSet = model.moduleDocument()
        #self.crossSectionSketch = model.addSketch(self.partSet, model.defaultPlane("YOZ"))
        self.part = model.addPart(self.partSet)
        self.part_doc = self.part.document()
#
        self.sections  = [] #Ordered list containing the object of each section
 
        self.sideProfileSketch = model.addSketch(self.part_doc, model.defaultPlane("XOY"))

        self.sketchProjection = self.sideProfileSketch.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
        self.sketchPoint = self.sketchProjection.createdFeature()

        self.totalLength = 0

        print("Projectile Initilized")


    def exportToGeom(self):
        print("Exporting projectile to geom module")

    def generateProjectile(self,**kwargs):

        import salome
        
        if kwargs.get("noseParams"):
            self.createNose(**kwargs.get("noseParams"))
        else:
            raise RuntimeError("Nose parameters must be specified")
    
        if kwargs.get("bodyParams"):
            self.createBodies(**kwargs.get("bodyParams"))

        self.sections[-1].makeEndSection() #Make last section end section      
      
        self.connectSections()

        model.do()
        self.revoluteSections()

        
       
    def createNose(self,**noseParam):

        print("Creating nose section")
        if noseParam["bodyType"] == "ConicNose":
            nose = ConicNose(0,**noseParam)
        elif noseParam["bodyType"] == "TangentOgiveNose":
            nose = TangenOgiveNose(0,**noseParam)
        elif noseParam["bodyType"] == "SecantOgiveNose":
            nose = SecantOgiveNose(0,**noseParam)
        else:
            raise RuntimeError("No valid nose type specified")
        
        self.sections.insert(0,nose)
        self.sections[0].addSketchLines(self.sideProfileSketch,axialStartPoint=0.0)
        self.totalLength = self.totalLength + self.sections[0].baseLength

    def createBodies(self,**bodyParamList):

        print("Creating body sections")

        currentAxialLength = self.sections[0].baseLength #Begin after the nose

        for i in range(1,len(bodyParamList)+1):
            sectionParams = bodyParamList["section_{}".format(i)]
            if sectionParams["bodyType"] == "HorizontalSection":
                body = HorizontalSection(i,**sectionParams)
            elif sectionParams["bodyType"] == "LinearTransitionSection":
                body = LinearTransitionSection(i,**sectionParams)
            else:
                raise AssertionError("Invalid body type specified")
                
            self.sections.append(body)
            
            #Assume straight projectile for now, so no need to parametrize body radius

            self.sections[i].addSketchLines(self.sideProfileSketch,currentAxialLength)

            currentAxialLength = currentAxialLength + self.sections[i].baseLength
            self.totalLength = self.totalLength + self.sections[i].baseLength

        
        

    def connectSections(self):
        """
        Connects the coincident points between each section
        """

        #Connect nose to origo
        self.sideProfileSketch.setCoincident(self.sections[0].baseAxialLine.startPoint(), self.sketchPoint.result())
        
        for i in range(1,len(self.sections)):
            
            #Connect base axial lines
            self.sideProfileSketch.setCoincident(self.sections[i-1].baseAxialLine.endPoint(),self.sections[i].baseAxialLine.startPoint())
            
            #Connect upper lines
            if (self.sections[i-1].baseRadius == self.sections[i].frontRadius):
                self.sideProfileSketch.setCoincident(self.sections[i-1].baseRadialLine.endPoint(),self.sections[i].upperContourLine.startPoint())



    def revoluteSections(self):

        self.revolutions = [] 
        self.shaperstudy = []
        for section in self.sections:
            revolution_selections, revolution_vector = section.generateRevolution()   
            
            #Note that the selections must be passed in revere order in order to get correct relation between faces 
            #and their respective ID's in shaper
            revolution = model.addRevolution(self.part_doc, revolution_selections, revolution_vector, 360, 0)  
            
            self.revolutions.append(revolution)
            
    