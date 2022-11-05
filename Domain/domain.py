
from Domain.projectile import ProjectileModel

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
    
   
from salome.shaper import model


class DomainGenerator:
    def __init__(self,name):

        self.projectile = ProjectileModel(name) 
    
        self.FrontDomainLength = 200
        self.BackDomainLength = 200
        self.domainRadius = 200

    def importProjectileFromShaper(self):
        

        print("Exporting all faces to geom module")
        ### Create Fuse
        
        
        model.publishToShaperStudy()
        import SHAPERSTUDY

        self.revolutionFacesShaper = []
        for i,section in enumerate(self.projectile.sections):
            revoluteSection = []
            for j in range(len(section.faceID)):
                print(section.faceID[j])
                ### Create Export
                export = model.exportToXAO(self.projectile.part_doc, '/tmp/shaper_{}.xao'.format(section.faceID[j]), model.selection("FACE", "Revolution_{0}_{1}".format(i+1,j+1)), 'XAO')
                
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

    def makeGeometry(self,params):
        
        self.projectile.generateProjectile(**params) 

        
        self.geompy = geomBuilder.New()

        self.importProjectileFromShaper()

        self.generateGeomProjectileFromFaces()

        self.generateOuterDomain()
        
    def generateGeomProjectileFromFaces(self):

        self.projectileGroups = [] #Contains all groups that holds faces desbribing the projectile geometry
        
        for i,section in enumerate(self.projectile.sections):
            geoms = []
            for j,faceNum in enumerate(section.outerFacesID):
                
                group =self.geompy.CreateGroup(self.revolutionFacesGeom[i][faceNum],self.geompy.ShapeType["FACE"])
                self.geompy.UnionIDs(group, [1])
                self.projectileGroups.append(group)

                self.geompy.addToStudyInFather( self.revolutionFacesGeom[i][faceNum], group, section.faceID[faceNum] )
                
        fuseGeom =self.geompy.MakeFuseList(self.projectileGroups, True, True)
        self.projectileGeom =self.geompy.MakeSolid([fuseGeom])
        self.geompy.addToStudy( fuseGeom, 'FuseProjectile' )
        self.geompy.addToStudy( self.projectileGeom, 'Projectile' )


    def generateOuterDomain(self):

        totalDomainLength = self.FrontDomainLength + self.BackDomainLength + self.projectile.totalLength
        startCylindeVertex = self.geompy.MakeVertex(-self.FrontDomainLength, 0, 0) #Point where the cylinder is extruded from
        unitVecX = self.geompy.MakeVectorDXDYDZ(1, 0, 0) #Negative direction of the projectile rocket
        cylinderDomain = self.geompy.MakeCylinder(startCylindeVertex, unitVecX, self.domainRadius, totalDomainLength)

        self.domain = self.geompy.MakeCutList(cylinderDomain, [self.projectileGeom], True)

        self.geompy.addToStudy( startCylindeVertex, 'VertexCylinder' )
        self.geompy.addToStudy( cylinderDomain, 'Cylinder' )
        self.geompy.addToStudy( self.domain, 'Domain' )
