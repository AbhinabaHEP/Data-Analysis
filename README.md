# Invariant Mass Reconstruction of K*
Data Analysis for reconstructed K* decay modes.
## Read collision data file
```
with open('ampt.dat') as f:
lines = f.readlines()
```
To read a line that denotes an event:
```
for line in lines:
        count_lines = count_lines+1
        ax = line.split()
        if (len(ax) ==11):
```
To read particle information for particle IDs under a particular event :
```
elif (len(ax)==9):
```
## Extract mass and momentum (px,py,pz) values of decay particles
K* decays into :
1) $k^+ + \pi^-$
