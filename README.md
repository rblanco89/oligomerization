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
- **traj**: Pathway to trajectory file (extensions: TRR, XTC)
- **initF**: Initial frame to start the measurement.
- **finishF**: Final frame to stop the measurement.

In the directory *pyNotebooks/*, there are the Jupyter notebook versión  of the script above
and also a notebook to plot results.

## Extra files

- In the directory *input/* there are the PDB input files to run the python script.
- In the "input_MD.zip" file there are the neccesary files to run MD as described in our work.
- In the "plots_data.zip" file there are the data of the figures presented in our work.


## Cite our work
Chi-Uluac, L. A., Asgharpour, S., Blanco-Rodríguez, R. G., & Martínez-Archundia, M. (2023). Atomistic Molecular Insights into Angiotensin-(1-7) Interpeptide Interactions. *Journal of Chemical Information and Modeling*, 63(16), 5331-5340.
