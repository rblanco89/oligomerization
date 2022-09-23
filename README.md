# Oligomerization script

A python script that quantifies the clusters size (oligomerization of identical molecules)
and gets a contact matrix of residues between pairs of molecules from a Molecular Dynamics (MD)
trajectory.

## Requirements

- numpy
- MDAnalysis
- igraph
- matplotlib

## How to use

There is one python script *pyScripts/oligomerization.py* that measures the size of cluster
in each frame from a MD trajectory and write it out to a file named *oligomers.dat*. Also,
it gets a contact matrix of residues between pairs of molecules and write it out to a file
named *cMap.dat* (the residue's names are written in *resNames.dat*).

The parameters are:
- **eps**: minimum distance to declare the formation of an oligomer.
- **refStruct**: Pathway to reference structure file (PDB).
- **traj**: Pathway to trajectory file (extnsions: TRR, XTC)
- **initF**: Integer that indicates the initial frame to start the measurement.
- **finishF**: Integer that indicates the final frame to stop the measurement (not included).

In the directory *pyNotebooks/*, there are the Jupyter notebook versión  of the script above
and also a notebook to plot results.
