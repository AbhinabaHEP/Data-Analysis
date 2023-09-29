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
## Extract mass and momentum (p<sub>x</sub>,p<sub>y</sub>,p<sub>z</sub>) values of decay particles
Decay modes of k* :<br/>
$k^* \rightarrow k^- + \pi^+$
$k^* \rightarrow k^- + \pi^+$
So we need to store m,p<sub>x</sub>,p<sub>y</sub>,p<sub>z</sub> values of corresponding aprticle ID's (k <sup>+</sup> =321, $\pi^- =-221$, $k^- =-321$, $\pi^+ =221$)
We apply loop for $k^+$ as :
```
if (float(ax[0])==321):
                par_array_m1.append(float(ax[4]))
                #par_array_pt1.append(np.sqrt(float(ax[1])**2 + float(ax[2])**2))
                par_array_pz1.append(float(ax[3]))
                par_array_py1.append(float(ax[2]))
                par_array_px1.append(float(ax[1]))
```
