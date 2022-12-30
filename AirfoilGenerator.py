import salome
import os
import sys

### DO NOT REMOVE: Ensures that all files in src are available ###
sys.path.append('src')

from Geometry.airfoil import generateAirfoilGeometry
from salome.geom import geomBuilder

import tkinter as tk
from tkinter import filedialog,Tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure





def readAirfoil():
    # Create the main window
    root = tk.Tk()

    #Locally global variables
    fig,name= None,None

    # Create a set to store the airfoil points for use in the meshing
    points = set()

    # Create a function that will be called when the user clicks the "Browse" button
    def browse_file():

        #This ensures that the variables defined in the outer scope 
        #(readAirfoil) are avaible in the inner function
        nonlocal fig,name,canvas,points
        
        # Remove any previous plot from the GUI
        if fig is not None:
            fig.clear()
            canvas.get_tk_widget().pack_forget()


        # Open a file dialog to let the user select a .dat file
        filepath = filedialog.askopenfilename(
            title='Open a airfoil file',
            initialdir='/home/asmund/dev/PMesh/src/Data/Airfoils',
            filetypes=(("Data files", "*.dat"),("All files","*.*"))
        )

        
        if name == None:
            # Schedule the "continue" button to appear after 1 second
            root.after(100, show_continue_button)

        points.clear
        
        points, name, x, y = readPointsAndName(filepath,points)


        # Create a new Matplotlib figure
        fig = Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)


        # Plot the points on the figure
        ax.plot(x,y)
        ax.set_title(name)
        ax.set_ylim(min(-0.3,min(y)),max(0.3,max(y)))


        # Display the figure in the GUI

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)


    # Define a function that creates the "continue" button
    def show_continue_button():
        # Create a function that will be called when the user clicks the "Continue" button
        def continue_program():
            # End the main event loop, which will close the GUI window
            root.quit()
        ## Create the "continue" button
        continue_button = tk.Button(root, text="Continue", command=continue_program)
        continue_button.grid(row=0, column=1)


    # Create an empty Matplotlib figure to display in the GUI
    fig = Figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.set_ylim(-0.3,0.3)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)

    # Create a button that will call the "browse_file" function when clicked
    browse_button = tk.Button(root, text="Browse", command=browse_file)

    browse_button.grid(row=0, column=0)

    # Set the window title
    root.title("Select airfoil")


    # Start the main event loop
    root.mainloop()

    return name, points



def readPointsAndName(filepath,points):

    # Read the selected file and extract the x and y coordinates of the points
    with open(filepath, "r") as f:
        x_list,y_list = [],[]
    
        for line in f:
            point = line.strip().split()            
            if len(point) != 2:
                continue
            try:
                x_coord = float(point[0])
                y_coord = float(point[1])
            except ValueError:
                continue
            if not (-1 <= x_coord <= 1) or not (-1 <= y_coord <= 1):
                continue

    
            x_list.append(x_coord)
            y_list.append(y_coord)
            


    x_upper,y_upper = [],[]
    x_lower,y_lower = [],[]

    for i,x in enumerate(x_list[2:]):
        if (x[i-2] > x[i-1] and x[i] > x[i-1]) and x[i-2:i] < 0.2: #In this case the upper list is given in reverse order (from back to front)
            x_upper = x_list[i-1:-1:]
            y_upper = y_list[i-1:-1:]
            x_lower = x_list[i:]
            y_lower = y_list[i:]
            
            break
    
        elif (x[i-2] < x[i-1] and x[i] < x[i-1]):
            x_upper = x_list[i:-1:]
            y_upper = y_list[i:-1:]
            x_lower = x_list[i:-1:]
            y_lower = y_list[i:-1:]
            
            break
    
    ## list of numbers
    #numbers = [1, 2, 3, 4, 5]
#
    ## check if the list is strictly increasing
    #is_increasing = all(x < y for x, y in zip(numbers, numbers[1:]))
    #print(is_increasing)  # True

    # check if the list is strictly decreasing
    #is_decreasing = all(x > y for x, y in zip(numbers, numbers[1:]))
    #print(is_decreasing)  # False

    #Coordinates put into tuples
    points.add((x_coord,y_coord))
    # Split the filepath into the root directory and file extension
    filepathNoExt, _ = os.path.splitext(filepath)
    # Extract the filename from the root directory
    name = os.path.basename(filepathNoExt)

    return points,name,x,y

def readAirfoilInSalome():

    filetypes = (
    ('text files', '*.dat'),
    ('All files', '*.*')
    )
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

    filename = filedialog.askopenfilename(
        title='Select an airfoil file',
        initialdir='/home/asmund/dev/PMesh/src/Data/Airfoils',
        filetypes=filetypes
    )

    # Create a set to store the airfoil points for use in the meshing
    points = set()

    points, name, _, _ = readPointsAndName(filename,points)

    return name, points

def programInit():


    if salome.sg.hasDesktop():
        print("The script is running inside the Salome GUI.")
        salomeRun = True
    else:
        print("The script is running in a regular Python environment.")
        salomeRun = False


    if salomeRun is False:
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
 
        name, points = readAirfoil()
        
    elif salomeRun is True:
 
 
        dir_path = '/home/asmund/dev/PMesh/src'
        
        name, points = readAirfoilInSalome()
          
    salome.salome_init()
    import salome_notebook
    notebook = salome_notebook.NoteBook()
    
 
    
    sys.path.insert(0, r'{}'.format(dir_path))

    return name,points,notebook, salomeRun


if __name__ == "__main__":

    name,points,notebook, salomeRun = programInit()

    generateAirfoilGeometry(points)

    print("Generated geometry for the {} airfoil".format(name))

    
    if salome.sg.hasDesktop():
        salome.sg.updateObjBrowser()

