# PMesh
Projectile Meshing


## Dependencies 

Tkinter
salome

Salome installation procedure: (shady and should be improved)

1: go to https://www.salome-platform.org/?page_id=15 and download the installation files for you linux didtribution. 
2: unzip the files in a random directory which we label $SALOME_INSATLL_DIR
3: add the following lines to ~/.bashrc: (modify according to the salome version you are using)
\\
export SALOME_INSTALL_DIR=~/dev/SALOME-9.9.0-native-UB22.04-SRC
source $SALOME_INSTALL_DIR/env_launch.sh
alias salome="$SALOME_INSTALL_DIR/salome"
\\
4: some dependencies are needed. The script: "" can be used to install many of them
5: If everything went according to plan, salome can now be run simply typing "salome" in a terminal.
