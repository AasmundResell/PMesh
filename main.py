


from Geometry.domain import DomainGenerator
from Mesh.mesh import MeshGenerator
from Mesh.SU2msh import ExportSU2File
import sys
import salome
import os 

def salomeInit(salomeRun = True):
        
    salome.salome_init()
    import salome_notebook
    notebook = salome_notebook.NoteBook()
    
    if salomeRun == True:
        dir_path = '/home/asmund/dev/PMesh'
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))
    
    sys.path.insert(0, r'{}'.format(dir_path))

    return notebook


if __name__ == "__main__":

    if len(sys.argv) > 1:
        notebook = salomeInit(salomeRun = sys.argv[1])
    else:
        notebook = salomeInit()
        
    #name = input("Please enter model name: ")

    name = "test_mesh"
    
    #M910 Bullet
    params =  {
        "noseParams" : 
            {
                "bodyType": "ConicNose",
                "bodyLength": 41.2,
                "bodyRadius": 16.2/2,
                "bodyRadiusFront": 2.2/2,
            },
        "bodyParams" : 
            {
            1 : {
                "bodyType": "HorizontalSection",
                "bodyLength": 73.9-41.2,
                "bodyRadius": 16.2/2,
                },
            2 : { 
                "bodyType": "LinearTransitionSection",
                "bodyLength": 0.2,
                "bodyRadius": 30,
                "bodyRadiusFront": 50,
                },
            },
        "finParams":
            {
                "finType": "SquareFins",
                "axialStartPosition": 100,
                "radialBasePosition": 20,
                "thickness" : 2,
                "baseLength" : 20,
                "baseHeight" : 10,
            },
        "domainParams":
        {
            "lengthFront": 200,
            "lengthBack": 200,
            "radius": 200,
        }    
    }

    geomDomain = DomainGenerator(name)

    geomDomain.makeGeometry(params)

    mesher = MeshGenerator()

    Mesh = mesher.generateMesh(geomDomain)

    ExportSU2File(mesh=Mesh,file=name)

    if salome.sg.hasDesktop():
        salome.sg.updateObjBrowser()


