
from Geometry.projectile import ProjectileModel

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
    
   
from salome.shaper import model


class DomainGenerator:
    def __init__(self,**kwargs):

        self.projectileParams = kwargs.get("projectile")
        
        domainParams = kwargs.get("domain")

        if kwargs.get("unit") == "mm":
            self.LengthConversion = 1.0
        elif kwargs.get("unit") == "cal":
            self.LengthConversion = 0.254
        elif kwargs.get("unit") == "m":
            self.LengthConversion = 1000.0      
        elif kwargs.get("unit") == "inch":
            self.LengthConversion = 25.4     
        else:
            self.LengthConversion = 1.0 #mm by default
            
        if domainParams.get("domain_method") == "manual":
            self.readDomain(**domainParams)
        elif domainParams.get("domain_method") == "automatic":
            self.calculateDomain()
        else:
          raise AssertionError("Method to specify the domain must be defined.")

        self.projectile = ProjectileModel(self.LengthConversion) 
        

    def readDomain(self,**kwargs):
        
        self.FrontDomainLength = kwargs.get("lengthFront")*self.LengthConversion
        self.BackDomainLength = kwargs.get("lengthBack")*self.LengthConversion
        self.domainRadius = kwargs.get('radius')*self.LengthConversion

    def calculateDomain(self):
        """
        Function that calculates the size of the domain based on the size of the projectile
        and the specified mach number.
        """
        
        #Front of the inner cylinder surrounding the projectile
        front_innerDomain = -self.projectile.totalLength/4
        
        #End of the inner cylinder
        back_innerDomain = self.projectile.totalLength*3

        


    def importProjectileFromShaper(self):
        

        print("Exporting all faces to geom module")
        ### Create Fuse
        
        
        model.publishToShaperStudy()
        import SHAPERSTUDY

        self.revolutionFacesShaper = []
        for i,section in enumerate(self.projectile.sections):
            revoluteSection = []
            for j in range(len(section.faceID)):
                
                ### Create Export
                
                model.exportToXAO(self.projectile.part_doc, '/tmp/shaper_{}.xao'.format(section.faceID[j]), model.selection("FACE", "Revolution_{0}_{1}".format(i+1,j+1)), 'XAO')
                
                if j == 0:
                    revoluteSection.append(SHAPERSTUDY.shape(model.featureStringId(self.projectile.revolutions[i])))
                else:    
                    revoluteSection.append(SHAPERSTUDY.shape(model.featureStringId(self.projectile.revolutions[i],j+1)))
            
            self.revolutionFacesShaper.append(revoluteSection)
        
        model.end()
        
        self.revolutionFacesGeom = []

        for i,section in enumerate(self.projectile.sections):
            revolutions_section = []
            for j in range(len(section.faceID)):
                
                (imported, revolution, [], [], []) = self.geompy.ImportXAO("/tmp/shaper_{}.xao".format(section.faceID[j]))
                self.geompy.addToStudy( revolution, 'Revolution_{0}_{1}'.format(i+1,j+1) )

                revolutions_section.append(revolution)
            self.revolutionFacesGeom.append(revolutions_section)

    def makeGeometry(self):
        
        self.projectile.generateProjectile(**self.projectileParams) 

        
        self.geompy = geomBuilder.New()

        self.importProjectileFromShaper()

        self.generateGeomProjectileFromFaces()

        self.generateDomainSimple()

    def generateGeomProjectileFromFaces(self):

        self.projectileGroups = [] #Contains all groups that holds faces desbribing the projectile geometry
        
        for i,section in enumerate(self.projectile.sections):
            geoms = []
            for j in range(len(section.faceID)):
                
                group =self.geompy.CreateGroup(self.revolutionFacesGeom[i][j],self.geompy.ShapeType["FACE"])
                self.geompy.UnionList(group, [self.revolutionFacesGeom[i][j]])
                self.projectileGroups.append(group)

                self.geompy.addToStudyInFather( self.revolutionFacesGeom[i][j], group, section.faceID[j] )
                
        
        shellProjectile = self.geompy.MakeShell([item for sublist in self.revolutionFacesGeom for item in sublist])
        self.projectileGeom =self.geompy.MakeSolid([shellProjectile])
        self.geompy.addToStudy( shellProjectile, 'ShellProjectile' )
        self.geompy.addToStudy( self.projectileGeom, 'Projectile' )


    def generateDomainSimple(self):

        ### Define the outer domain ####
        totalDomainLength = self.FrontDomainLength + self.BackDomainLength + self.projectile.totalLength
        startOuterVertex = self.geompy.MakeVertex(-self.FrontDomainLength, 0, 0) #Point where the cylinder is extruded from
        self.geompy.addToStudy( startOuterVertex, 'VertexCylinder' )

        unitVecX = self.geompy.MakeVectorDXDYDZ(1, 0, 0) #Negative direction of the projectile rocket
        outerDomain = self.geompy.MakeCylinder(startOuterVertex, unitVecX, self.domainRadius, totalDomainLength)
        outer_domainID = self.geompy.addToStudy( outerDomain, 'Outer_domain' )

        
        
        self.domain = self.geompy.MakeCutList(outerDomain, [self.projectileGeom], True)

        self.geompy.addToStudy( self.domain, 'domain' )
    

        faceIDs = self.geompy.SubShapeAllIDs(self.domain, self.geompy.ShapeType["FACE"])

        self.domainFaces = 3
        
        self.domainIDs = faceIDs[0:self.domainFaces]
        self.projectileIDs = faceIDs[self.domainFaces:]
       
    
        self.Farfield = self.geompy.CreateGroup(self.domain, self.geompy.ShapeType["FACE"])
        self.geompy.UnionIDs(self.Farfield, self.domainIDs)


        self.Projectile = self.geompy.CreateGroup(self.domain, self.geompy.ShapeType["FACE"])
        self.geompy.UnionIDs(self.Projectile, self.domainIDs)

        self.geompy.addToStudyInFather( self.domain, self.Farfield, 'Farfield' )
        self.geompy.addToStudyInFather( self.domain, self.Projectile, 'Projectile' )

    def generateDomainInnerRefinement(self):

        ### Define the outer domain ####
        totalDomainLength = self.FrontDomainLength + self.BackDomainLength + self.projectile.totalLength
        startOuterVertex = self.geompy.MakeVertex(-self.FrontDomainLength, 0, 0) #Point where the cylinder is extruded from
        self.geompy.addToStudy( startOuterVertex, 'VertexCylinder' )

        unitVecX = self.geompy.MakeVectorDXDYDZ(1, 0, 0) #Negative direction of the projectile rocket
        outerDomain = self.geompy.MakeCylinder(startOuterVertex, unitVecX, self.domainRadius, totalDomainLength)
        outer_domainID = self.geompy.addToStudy( outerDomain, 'Outer_domain' )

        ### Define the inner domain, ie. the refinement zone surrounding the projectile ####
        
        #For now, the refinement zone extends 1/3 of the projectile length in the front
        #startInnerVertex = self.geompy.MakeVertex(-self.projectile.totalLength/3, 0, 0) 
        #unitVecX = self.geompy.MakeVectorDXDYDZ(1, 0, 0) #Negative direction of the projectile rocket

        #Extends 1/2 behind the projectile
        #innerCylinder = self.geompy.MakeCylinder(startInnerVertex, unitVecX, self.projectile.maxRadius*3, self.projectile.totalLength*(1/3+3/2))
        #innerCylinderID = self.geompy.addToStudy( innerCylinder, 'innerCylinder' )

        
        #self.innerDomain = self.geompy.MakeCutList(innerCylinder, [self.projectileGeom], True)

        #self.geompy.addToStudyInFather( self.innerDomain, self.Farfield, 'Farfield' )
        #self.geompy.addToStudyInFather( self.innerDomain, self.Projectile, 'Projectile' )
        
        #self.geompy.addToStudy( self.innerDomain, 'innerDomain' )

        self.domain = self.geompy.MakeCutList(outerDomain, [self.projectileGeom], True)

        self.geompy.addToStudy( self.domain, 'domain' )
        


        ###Generate domain ###
        #Vector_z = self.geompy.MakeVectorDXDYDZ(0, 0, 1)
        #origo = self.geompy.MakeVertex(0, 0, 0) #Point where the cylinder is extruded from
        #symmetricCutPlane = self.geompy.MakePlane(origo, Vector_z, 2000)

        #Partition_1 = self.geompy.MakePartitionNonSelfIntersectedShape([outerDomain, self.innerDomain], [symmetricCutPlane], [], [], self.geompy.ShapeType["SOLID"], 0, [], 1, True)

        

        faceIDs = self.geompy.SubShapeAllIDs(self.domain, self.geompy.ShapeType["FACE"])

        self.domainFaces = 3
        
        self.domainIDs = faceIDs[0:self.domainFaces]
        self.projectileIDs = faceIDs[self.domainFaces:]
       
        #[self.Farfield, self.Projectile] = self.geompy.GetExistingSubObjects(self.domain, False)

        self.Farfield = self.geompy.CreateGroup(self.domain, self.geompy.ShapeType["FACE"])
        self.geompy.UnionIDs(self.Farfield, self.domainIDs)


        self.Projectile = self.geompy.CreateGroup(self.domain, self.geompy.ShapeType["FACE"])
        self.geompy.UnionIDs(self.Projectile, self.domainIDs)

        self.geompy.addToStudyInFather( self.domain, self.Farfield, 'Farfield' )
        self.geompy.addToStudyInFather( self.domain, self.Projectile, 'Projectile' )
  