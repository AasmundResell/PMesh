


from Geometry.domain import DomainGenerator
from Mesh.mesh import MeshGenerator
from Mesh.SU2msh import ExportSU2File
import sys
import salome
import os 
import yaml

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
        
    
    ymlFile = open("Configurations/M910_bullet.yml") 
    
    parsedValues = yaml.load(ymlFile, Loader=yaml.FullLoader)
    SystemSettings = parsedValues['system']
    GeometryParams = parsedValues['geometry']
    MeshParams = parsedValues['mesh']
    
    name = SystemSettings['name']

    

    geomDomain = DomainGenerator(**GeometryParams)

    geomDomain.makeGeometry()

    mesher = MeshGenerator(name,**MeshParams)

    Mesh = mesher.generateMesh(geomDomain)

    ExportSU2File(mesh=Mesh,file=name)

    if salome.sg.hasDesktop():
        salome.sg.updateObjBrowser()


