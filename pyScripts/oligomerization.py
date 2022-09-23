"""
Author: Rodolfo Blanco-Rodriguez
Creation date: September 21st 2022
"""

import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis import distances
from igraph import Graph
import matplotlib.pyplot as plt

eps = 3 # minimum distance to declare cluster in Angstroms
refStruc = 'ang.pdb' # Location of Reference structure file
traj = 'nopbc_vmd.trr' #  and Trajectories file (it can be XTC format)
initF = 20000
finishF = None

# Load trajectories
angs = mda.Universe(refStruc, traj)

molecules = angs.segments.n_segments
residues = angs.residues.n_residues
aminoAcids = residues//molecules
box = angs.dimensions

g = Graph();
g.add_vertices(molecules)
frame = []
oligomers = []
contactMap = np.zeros((aminoAcids, aminoAcids))

for tt in angs.trajectory[initF:finishF]:
    for i in range(molecules-1):
        for j in range(i+1,molecules):
            minDist = distances.distance_array(angs.segments[i].atoms.positions,
                                               angs.segments[j].atoms.positions, box).min()
            if(minDist > eps):
                continue
                
            g.add_edge(i,j)
            
            for m in range(aminoAcids):
                for n in range(aminoAcids):
                    minDistRes = distances.distance_array(angs.segments[i].residues[m].atoms.positions,
                                                        angs.segments[j].residues[n].atoms.positions, box).min()
                    if (minDistRes > eps):
                        continue
                        
                    contactMap[m][n] += 1
                    contactMap[n][m] += 1
                    
    cs = g.clusters()
    
    clusters = [0 for i in range(molecules)]
    
    for cc in cs:
        clusters[len(cc)-1] += 1
        
    oligomers.append(clusters)
    
    frame.append(tt.frame)
     
    g.delete_edges()

# Save data

fOut = open ('oligomers.dat', 'w')
for i, val in enumerate(oligomers):
    fOut.write(f'{frame[i]}\t')
    for j in range(molecules):
        if j == molecules - 1:
            fOut.write(f'{val[j]}\n')
        else:
            fOut.write(f'{val[j]}\t')
fOut.close()

normContactMap = contactMap/(contactMap.sum()/2) # It is divided by 2 because double count by pair
np.savetxt('cMap.dat', normContactMap, fmt = '%0.6f') # Save matrix in a file

resNames = angs.segments.resnames[0]
np.savetxt('resNames.dat', resNames, fmt='%s') # Save residues names
