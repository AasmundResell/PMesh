# Import the necessary modules
import pyvista as pv
from pyvista import PolyData

# Create a cone
cone = PolyData.Cone(height=1.0, radius=0.5, resolution=16)

# Visualize the cone using PyVista's plotter
plotter = pv.Plotter()
plotter.add_mesh(cone)
plotter.show()

