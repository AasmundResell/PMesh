
from Geometry.projectile import ProjectileModel

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
    
   
from salome.shaper import model


class DomainGenerator:
    def __init__(self,**kwargs):


        self.projectileParams = kwargs.get("projectile")
        self.projectile = ProjectileModel() 
        
        domainParams = kwargs.get("domain")

        if domainParams.get("domain_method") == "manual":
            self.readDomain(**domainParams)
        elif domainParams.get("domain_method") == "automatic":
            self.calculateDomain()
        else:
          raise AssertionError("Method to specify the domain must be defined.")

    def readDomain(self,**kwargs):
        
        self.FrontDomainLength = kwargs.get("lengthFront")
        self.BackDomainLength = kwargs.get("lengthBack")
        self.domainRadius = kwargs.get('radius')

    def caculateDomain(self):
        """
        Function that calculates the size of the domain based on the size of the projectile
        and the specified mach number.
        """
        print("TEMP")

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
                print('/tmp/shaper_{}.xao'.format(section.faceID[j]))
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
                print("/tmp/shaper_{}.xao".format(section.faceID[j]))
                (imported, revolution, [], [], []) = self.geompy.ImportXAO("/tmp/shaper_{}.xao".format(section.faceID[j]))
                self.geompy.addToStudy( revolution, 'Revolution_{0}_{1}'.format(i+1,j+1) )

                revolutions_section.append(revolution)
            self.revolutionFacesGeom.append(revolutions_section)

    def makeGeometry(self):
        
        self.projectile.generateProjectile(**self.projectileParams) 

        
        self.geompy = geomBuilder.New()

        self.importProjectileFromShaper()

        self.generateGeomProjectileFromFaces()

        self.generateDomains()

    def generateGeomProjectileFromFaces(self):

        self.projectileGroups = [] #Contains all groups that holds faces desbribing the projectile geometry
        
        for i,section in enumerate(self.projectile.sections):
            geoms = []
            for j,faceNum in enumerate(section.outerFacesID):
                
                group =self.geompy.CreateGroup(self.revolutionFacesGeom[i][faceNum],self.geompy.ShapeType["FACE"])
                self.geompy.UnionList(group, [self.revolutionFacesGeom[i][faceNum]])
                self.projectileGroups.append(group)

                self.geompy.addToStudyInFather( self.revolutionFacesGeom[i][faceNum], group, section.faceID[faceNum] )
                
        fuseGeom =self.geompy.MakeFuseList(self.projectileGroups, True, True)
        self.projectileGeom =self.geompy.MakeSolid([fuseGeom])
        self.geompy.addToStudy( fuseGeom, 'FuseProjectile' )
        self.geompy.addToStudy( self.projectileGeom, 'Projectile' )


    def generateDomains(self):

        totalDomainLength = self.FrontDomainLength + self.BackDomainLength + self.projectile.totalLength
        startCylindeVertex = self.geompy.MakeVertex(-self.FrontDomainLength, 0, 0) #Point where the cylinder is extruded from
        unitVecX = self.geompy.MakeVectorDXDYDZ(1, 0, 0) #Negative direction of the projectile rocket
        cylinderDomain = self.geompy.MakeCylinder(startCylindeVertex, unitVecX, self.domainRadius, totalDomainLength)

        self.domain = self.geompy.MakeCutList(cylinderDomain, [self.projectileGeom], True)
        
        self.geompy.addToStudy( startCylindeVertex, 'VertexCylinder' )
        cylinderID = self.geompy.addToStudy( cylinderDomain, 'Cylinder' )
        self.geompy.addToStudy( self.domain, 'Domain' )

        Farfield = self.geompy.CreateGroup(self.domain, self.geompy.ShapeType["FACE"])
        self.geompy.UnionIDs(Farfield, [3, 10, 12])
        Rocket_1 = self.geompy.CreateGroup(self.domain, self.geompy.ShapeType["FACE"])
        self.geompy.UnionIDs(Rocket_1, [15, 22, 27, 32])
        
        [self.Farfield, self.Projectile] = self.geompy.GetExistingSubObjects(self.domain, False)
        
        self.geompy.addToStudyInFather( self.domain, self.Farfield, 'Farfield' )
        self.geompy.addToStudyInFather( self.domain, self.Projectile, 'Projectile' )
        
        faceIDs = self.geompy.SubShapeAllIDs(self.domain, self.geompy.ShapeType["FACE"])

        self.domainFaces = 3
        
        self.domainIDs = faceIDs[0:self.domainFaces]
        self.projectileIDs = faceIDs[self.domainFaces:]
       

        