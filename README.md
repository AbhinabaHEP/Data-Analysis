# Invariant Mass Reconstruction of K*
Data Analysis for reconstruction of K*  from it's decay branches.
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
So we need to store m,p<sub>x</sub>,p<sub>y</sub>,p<sub>z</sub> values of corresponding aprticle ID's ($k^+ =321$, $\pi^- =-221$, $k^- =-321$, $\pi^+ =221$) <br/>
We apply loop for $k^+$ as :
```
if (float(ax[0])==321):
                par_array_m1.append(float(ax[4]))
                #par_array_pt1.append(np.sqrt(float(ax[1])**2 + float(ax[2])**2))
                par_array_pz1.append(float(ax[3]))
                par_array_py1.append(float(ax[2]))
                par_array_px1.append(float(ax[1]))
```
Similarly, we extract values for $\pi^-$, $k^-$, $\pi^+$.
## Particle counts for unsimilar charge pairs :
For $k^- + \pi^+$ the net invariant mass is counted in bins as :
```
for i in range(0,len(par_array_m1)):
                E1 = (np.sqrt(float(par_array_px1[i])**2+float(par_array_py1[i])**2+float(par_array_pz1[i])**2+float(par_array_m1[i])**2))
                for j in range(0,len(par_array_m2)):
                    E2 = (np.sqrt(float(par_array_px2[j])**2+float(par_array_py2[j])**2+float(par_array_pz2[j])**2+float(par_array_m2[j])**2))
                    m1_m2=(np.sqrt(((E1+E2)**2)-((par_array_px1[i]+par_array_px2[j])**2+(par_array_py1[i]+par_array_py2[j])**2+(par_array_pz1[i]+par_array_pz2[j])**2)))
                    if (m1_m2>=0 and m1_m2<=0.2):
                        #print par_array_m1[i],par_array_m2[j],par_array_px1[i],par_array_py1[i],par_array_pz1[i],par_array_px2[j],par_array_py2[j],par_array_pz2[j],E1,E2,m1_m2
                        
                        count1[0]+=1
                    elif (m1_m2>0.2 and m1_m2<=0.4):
                        count1[1]+=1
                    elif (m1_m2>0.4 and m1_m2<=0.6):
                        count1[2]+=1
                    elif (m1_m2>0.6 and m1_m2<=0.8):
                        count1[3]+=1
                    elif (m1_m2>0.8 and m1_m2<=1.0):
                        count1[4]+=1
                    elif (m1_m2>1.0 and m1_m2<=1.2):
                        count1[5]+=1
                    elif (m1_m2>1.2 and m1_m2<=1.4):
                        count1[6]+=1
                    elif (m1_m2>1.4 and m1_m2<=1.6):
                        count1[7]+=1
                    elif (m1_m2>1.6 and m1_m2<=1.8):
                        count1[8]+=1
                    elif (m1_m2>1.8 and m1_m2<=2.0):
                        count1[9]+=1
                    elif (m1_m2>2.0 and m1_m2<=2.2):
                        count1[10]+=1
                    elif (m1_m2>2.2 and m1_m2<=2.4):
                        count1[11]+=1
                    elif (m1_m2>2.4 and m1_m2<=2.6):
                        count1[12]+=1
                    elif (m1_m2>2.6 and m1_m2<=2.8):
                        count1[13]+=1
                    elif (m1_m2>2.8 and m1_m2<=3.0):
                        count1[14]+=1
                    elif (m1_m2>3.0 and m1_m2<=3.2):
                        count1[15]+=1
                    elif (m1_m2>3.2 and m1_m2<=3.4):
                        count1[16]+=1
                    elif (m1_m2>3.4 and m1_m2<=3.6):
                        count1[17]+=1
                    elif (m1_m2>3.6 and m1_m2<=3.8):
                        count1[18]+=1
                    elif (m1_m2>3.8 and m1_m2<=4.0):
                        count1[19]+=1
```
Simillarly, we find counts for $k^- + \pi^+$.
