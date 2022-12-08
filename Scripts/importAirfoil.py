import salome
import os

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap

from salome.geom import geomBuilder

import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to retrieve the .dat files from
base_url = "https://m-selig.ae.illinois.edu/ads/coord_database.html"

# Use the requests library to fetch the HTML of the website
response = requests.get(base_url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the links on the page
links = soup.find_all("a")

# Iterate over the links and extract the URLs that link to .dat files
dat_file_urls = []

for link in links:
    
    if "href" in link.attrs and link["href"].endswith(".dat"):
        dat_file_urls.append(link["href"])
    

# Create the main application window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Airfoil Selector")
#window.setGeometry(100, 100, 1000, 1000)

url_combo_box = QComboBox(window)

# Create a combo box with the list of URLs
for url in dat_file_urls:
    
    filenameExt = os.path.basename(url)
    file_name, _ = os.path.splitext(filenameExt)
    print(url)
    url_combo_box.addItem(file_name,url)


# Create a label to display the image
image_label = QLabel(window)
image_label.setGeometry(50, 50, 1000, 1000)


# Define a function to handle the user's selection
@pyqtSlot()
def on_selection():
    # Get the selected URL
    selected_url = url_combo_box.currentData()

    selected_url ="{0}{1}".format("https://m-selig.ae.illinois.edu/ads/",selected_url)

    # Get the HTML content of the selected URL
    response = requests.get(selected_url)
    html_content = response.text

    

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Print the content of the website
    print(soup.prettify())


    selected_file = url_combo_box.currentText()
    print(selected_file)
    # Download the corresponding image file
    response = requests.get("https://m-selig.ae.illinois.edu/ads/afplots/{}.gif".format(selected_file))
    image_data = response.content

    # Load the image from the downloaded data
    image = QPixmap()
    image.loadFromData(image_data)

    # Display the image in the label
    image_label.setPixmap(image)


# Connect the combo box's "activated" signal to the handler function
url_combo_box.activated.connect(on_selection)

# Show the application window
window.show()

# Run the application
sys.exit(app.exec_())

"""
# Create the tkinter window and set its title
root = Tk()
root.title("Dat File Viewer")

# Create a variable to hold the selected URL
selected_url = StringVar()

# Create a dropdown list of the URLs that link to .dat files
dropdown = OptionMenu(root, selected_url, *dat_file_urls)
dropdown.pack()

# Create a button to view the selected .dat file
button = Button(root, text="View Dat File", command=lambda: view_dat_file(selected_url.get()))
button.pack()

# Define the function to view the selected .dat file
def view_dat_file(url):
    # Send a GET request to the URL and retrieve the response
    response = requests.get(url)
    
    # Print the content of the .dat file
    print(response.text)

# Start the tkinter event loop
root.mainloop()

dat_file_url ="{0}{1}".format("https://m-selig.ae.illinois.edu/ads/",dat_files)
# Use the requests library to download the content of the chosen file
response = requests.get(dat_file_url)
"""

"""
# Print out the content of the chosen file
print(response.text)
# Get the GEOM module
geompy = geomBuilder.New()

         
filetypes = (
    ('text files', '*.dat'),
    ('All files', '*.*')
    )

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearin
filename = askopenfilename(
    title='Open a config file',
    initialdir='/home/asmund/dev/PMesh/Scripts/Airfoils',
    filetypes=filetypes
)


# Open the file containing the points
with open(filename,"r") as f:
    #Last bit makes it ignore lines that are empty
    points = [tuple(map(float, line.split())) for line in f if line.strip()]



# Loop over the lines and create a point for each set of coordinates
geom_points = [geompy.MakeVertex(x,y, 0.0) for x,y in points]


for i,point in enumerate(geom_points):
    geompy.addToStudy(point, "Point_{}".format(i))

#Create compound for compatability with CFDMSH
compound = geompy.MakeCompound(geom_points)

geompy.addToStudy(compound,"Compound")

salome.sg.updateObjBrowser()
"""