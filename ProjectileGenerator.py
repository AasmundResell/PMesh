import sys
import salome
import os 
import yaml

### DO NOT REMOVE: Ensures that all files in src are available ###
sys.path.append('src')


from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno

from Geometry.domain import DomainGenerator
from Mesh.mesh import MeshGenerator
from CFDMSH import ExportSU2File



def programInit():


    if salome.sg.hasDesktop():
        print("The script is running inside the Salome GUI.")
        salomeRun = True
    else:
        print("The script is running in a regular Python environment.")
        salomeRun = False

    
    filetypes = (
        ('text files', '*.yml'),
        ('All files', '*.*')
    )

    if salomeRun is False:
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
 
        if len(sys.argv) == 1:

            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

            filename = askopenfilename(
                title='Open a projectile config file',
                initialdir=r'{}/Configurations'.format(dir_path),
                filetypes=filetypes)
        

        elif len(sys.argv) > 1: #Read the config file as command line argument

            filename = "{0}/Configurations/{1}".format(dir_path,str2bool(sys.argv[1]))
        
    elif salomeRun is True:
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

        dir_path = '/home/asmund/dev/PMesh'
        
        filename = askopenfilename(
            title='Open a config file',
            initialdir=r'{}/Configurations'.format(dir_path),
            filetypes=filetypes)
        

    ###Filename must be specified manually for salome run###
    ymlFile = open(filename) 
        
        
    salome.salome_init()
    import salome_notebook
    notebook = salome_notebook.NoteBook()
    
 
    
    sys.path.insert(0, r'{}'.format(dir_path))

    return notebook, ymlFile, salomeRun

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

    
    notebook,ymlFile,salomeRun = programInit()
    
    parsedValues = yaml.load(ymlFile, Loader=yaml.FullLoader)
    SystemSettings = parsedValues['system']
    GeometryParams = parsedValues['geometry']
    MeshParams = parsedValues['mesh']
    
    name = SystemSettings['name']

    geomDomain = DomainGenerator(**SystemSettings,**GeometryParams)

    geomDomain.makeGeometry()
    
    mesher = MeshGenerator(name,geomDomain,**MeshParams)
    
    
    def askMeshGeneration():
        question = "Generate the mesh?"
        response = askyesno("Mesh", question)
        global name
        if response == True:
            Mesh = mesher.generateMesh()
            print("Exporting to SU2 ...")
            name = "/home/asmund/dev/PMesh/{}".format(name)

            ExportSU2File(mesh=Mesh,file=name)
            
    root = Tk()
    root.withdraw()
    askMeshGeneration()

    
    if salome.sg.hasDesktop():
        salome.sg.updateObjBrowser()


