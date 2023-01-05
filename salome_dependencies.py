import os
import sys
import subprocess
path_to_file = os.path.dirname(os.path.abspath(__file__))
filename = path_to_file+'/salome_dependencies.txt'
file = open(filename, 'r')
lines = file.readlines()
  

os.system('sudo apt-get upgrade') #?

for line in lines:
    
    line = line.strip().split()

    if len(line) == 0 or line[0] == '' or line[3] == 'OK':
        continue
    package = line[1]
    
    print('Attempting to install',package)
        
    os.system('sudo apt install '+package)
os.system('sudo apt autoremove')