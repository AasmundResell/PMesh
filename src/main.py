

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


#import tkinter as tk
#from tkinter import ttk
#from tkinter import filedialog as fd
#from tkinter.messagebox import showinfo


from Geometry.domain import DomainGenerator
from Mesh.mesh import MeshGenerator
from CFDMSH import ExportSU2File
import sys
import salome
import os 
import yaml

def programInit():

    salomeRun = True

    if len(sys.argv) > 1:
        salomeRun = str2bool(sys.argv[1])
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
 

        filetypes = (
            ('text files', '*.yml'),
            ('All files', '*.*')
        )

        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

        filename = askopenfilename(
            title='Open a config file',
            initialdir=r'{}/../Configurations'.format(dir_path),
            filetypes=filetypes)

        ymlFile = open(filename) 

    else:
        salomeRun = True
        
        ###Filename must be specified manually for salome run###
        ymlFile = open("Configurations/Simple_Bullet.yml") 
        dir_path = '/home/asmund/dev/PMesh'
        
        
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
    if salomeRun:
        Mesh = mesher.generateMesh()
    else:   
        question = "Do you want to generate the mesh? \n"
        if (query_yes_no(question)):
            Mesh = mesher.generateMesh()
        else:
            quit()
    
    print("Exporting to SU2 ...")
    name = "/home/asmund/dev/PMesh/{}".format(name)
    
    ExportSU2File(mesh=Mesh,file=name)
    

    
    
    if salome.sg.hasDesktop():
        salome.sg.updateObjBrowser()


