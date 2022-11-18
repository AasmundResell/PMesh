


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

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")

def str2bool(v):
    if v.lower() in ("yes", "true", "t", "1"):
        return True 
    elif v.lower() in ("no", "false", "f", "0"):
        return False
    else:
        raise ValueError("invalid command line argument for True/False: '%s'" % v)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        salomeRun = str2bool(sys.argv[1])
        print(salomeRun)
    else:
        salomeRun = True
        
        
    notebook = salomeInit(salomeRun)
    ymlFile = open("Configurations/Ogive_test.yml") 
    
    parsedValues = yaml.load(ymlFile, Loader=yaml.FullLoader)
    SystemSettings = parsedValues['system']
    GeometryParams = parsedValues['geometry']
    MeshParams = parsedValues['mesh']
    
    name = SystemSettings['name']

    

    geomDomain = DomainGenerator(**GeometryParams)

    geomDomain.makeGeometry()

    mesher = MeshGenerator(name,**MeshParams)

    if salomeRun:
        Mesh = mesher.generateMesh(geomDomain)
    else:   
        question = "Do you want to generate the mesh? \n"
        if (query_yes_no(question)):
            Mesh = mesher.generateMesh(geomDomain)
        else:
            quit()
    
    ExportSU2File(mesh=Mesh,file=name)


    if salome.sg.hasDesktop():
        salome.sg.updateObjBrowser()


