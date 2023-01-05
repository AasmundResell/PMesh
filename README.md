# PMesh
Projectile Meshing


## Dependencies 

Tkinter
salome

Salome installation procedure: (This is probably not a good way to do it and it may not work for later versions or other systems)

1: go to https://www.salome-platform.org/?page_id=15 and download the installation files for your linux didtribution (Ubuntu 22.04 in this case)

2: unzip the files in a random directory which we label $SALOME_INSTALL_DIR

3: It might be a good idea to read the README located in this folder.

4: add the following lines to ~/.bashrc: (modify according to the salome version you are using)
```
export SALOME_INSTALL_DIR=$SALOME_INSTALL_DIR/SALOME-9.9.0-native-UB22.04-SRC
source $SALOME_INSTALL_DIR/env_launch.sh
alias salome="$SALOME_INSTALL_DIR/salome"
```
5: some dependencies are needed. 

type
```
sat/sat config SALOME-9.9.0-native --check_system
```
to see which dependencies you are missing.
The script: salome_dependencies.sh located in the root folder of PMesh can be used to install some of them, unless it has depreciated. 

6: If everything went according to plan, salome can now be run simply typing ```salome``` in a terminal.
