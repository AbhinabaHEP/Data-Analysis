import numpy as np
import matplotlib.pyplot as plt
from itertools import product
array_nkaons=[]
par_array_pz1=[]
par_array_pz2=[]
par_array_pz3=[]
par_array_pz4=[]
par_array_py1=[]
par_array_py2=[]
par_array_py3=[]
par_array_py4=[]
par_array_px1=[]
par_array_px2=[]
par_array_px3=[]
par_array_px4=[]
par_array_m1=[]
par_array_m2=[]
par_array_m3=[]
par_array_m4=[]
#opp_pairs
m1_m2=0
m3_m4=0
m2_m3=0
m1_m4=0
par_array_x=[]
par_array_pt1=[]
par_array_pt2=[]#1!!
par_array_pt3=[]
par_array_pt4=[]
#count1_2_opp=[]
#energy1_array=[]
#energy2_array=[]
E1=0
E2=0
E3=0
E4=0

avg_pt1=[]
evt_arr_count_dndy = [] #11!!
evt_arr_b = []   #111!!
evt_arr_nparts = []
count1=[]
count2=[]
count1_2_opp=[]
count3=[]
count4=[]
count3_4_sim=[]
count_final=[]
#count_opp_pair_comb=[]
for i in range(0,20):
    count1.append(0)#1111!!
    count2.append(0)
    count1_2_opp.append(0)
    count3.append(0)
    count4.append(0)
    count3_4_sim.append(0)
    count_final.append(0)
with open('ampt.dat') as f:

    lines = f.readlines()
    #started reading the file line by line
    count_bin_kaons =0
    count_lines =0
    count_dndy = 0  #2!!
    sum_pt1=0
    for line in lines:
        count_lines = count_lines+1
        ax = line.split()
        #print(type(ax), len(ax))
        if (len(ax) ==11): #2!!
            evt_arr_b.append(ax[3])
            evt_arr_nparts.append(ax[2])
            if( int(ax[0]) > 1):
                array_nkaons.append(count_bin_kaons)
                evt_arr_count_dndy.append(count_dndy)
        
                #avg_pt1.append(sum(par_array_pt1)/len(par_array_pt1))
                #print avg_pt1
            count_bin_kaons =0
            count_dndy = 0
            
            for i in range(0,len(par_array_m1)):
                E1 = (np.sqrt(float(par_array_px1[i])**2+float(par_array_py1[i])**2+float(par_array_pz1[i])**2+float(par_array_m1[i])**2))
                for j in range(0,len(par_array_m2)):
                    E2 = (np.sqrt(float(par_array_px2[j])**2+float(par_array_py2[j])**2+float(par_array_pz2[j])**2+float(par_array_m2[j])**2))
                    m1_m2=(np.sqrt(((E1+E2)**2)-((par_array_px1[i]+par_array_px2[j])**2+(par_array_py1[i]+par_array_py2[j])**2+(par_array_pz1[i]+par_array_pz2[j])**2)))
                    if (m1_m2>=0 and m1_m2<=0.2):
                        #print par_array_m1[i],par_array_m2[j],par_array_px1[i],par_array_py1[i],par_array_pz1[i],par_array_px2[j],par_array_py2[j],par_array_pz2[j],E1,E2,m1_m2
                        #exit()
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
                    #par_array_m1_m2.append(np.sqrt((E1 + E2)**2 -(((energy1_array[1][i])+(energy2_array[1][j]))**2 +((energy1_array[2][i])+(energy2_array[2][j]))**2 +((energy1_array[3][i])+(energy2_array[3][j]))**2))
           
            #print (count1)
            E1=[]
            E2=[]
            par_array_m1=[]
            par_array_m2=[]
            par_array_px1=[]
            par_array_px2=[]
            par_array_py1=[]
            par_array_py2=[]
            par_array_pz1=[]
            par_array_pz2=[]
            par_array_m1_m2=[]
            par_array_pt1=[]

            for i in range(0,len(par_array_m3)):
                E3=(np.sqrt(float(par_array_px3[i])**2+float(par_array_py3[i])**2+float(par_array_pz3[i])**2+float(par_array_m3[i])**2))
                for j in range(0,len(par_array_m4)):
                    E4=(np.sqrt(float(par_array_px4[j])**2+float(par_array_py4[j])**2+float(par_array_pz4[j])**2+float(par_array_m4[j])**2))
                    m3_m4=(np.sqrt(((E3+E4)**2)-((par_array_px3[i]+par_array_px4[j])**2+(par_array_py3[i]+par_array_py4[j])**2+(par_array_pz3[i]+par_array_pz4[j])**2)))
                    if (m3_m4>=0 and m3_m4<=0.2):
                        #print par_array_m1[i],par_array_m2[j],par_array_px1[i],par_array_py1[i],par_array_pz1[i],par_array_px2[j],par_array_py2[j],par_array_pz2[j],E1,E2,m1_m2
                        #exit()
                        count2[0]+=1
                    elif (m3_m4>0.2 and m3_m4<=0.4):
                        count2[1]+=1
                    elif (m3_m4>0.4 and m3_m4<=0.6):
                        count2[2]+=1
                    elif (m3_m4>0.6 and m3_m4<=0.8):
                        count2[3]+=1
                    elif (m3_m4>0.8 and m3_m4<=1.0):
                        count2[4]+=1
                    elif (m3_m4>1.0 and m3_m4<=1.2):
                        count2[5]+=1
                    elif (m3_m4>1.2 and m3_m4<=1.4):
                        count2[6]+=1
                    elif (m3_m4>1.4 and m3_m4<=1.6):
                        count2[7]+=1
                    elif (m3_m4>1.6 and m3_m4<=1.8):
                        count2[8]+=1
                    elif (m3_m4>1.8 and m3_m4<=2.0):
                        count2[9]+=1
                    elif (m3_m4>2.0 and m3_m4<=2.2):
                        count2[10]+=1
                    elif (m3_m4>2.2 and m3_m4<=2.4):
                        count2[11]+=1
                    elif (m3_m4>2.4 and m3_m4<=2.6):
                        count2[12]+=1
                    elif (m3_m4>2.6 and m3_m4<=2.8):
                        count2[13]+=1
                    elif (m3_m4>2.8 and m3_m4<=3.0):
                        count2[14]+=1
                    elif (m3_m4>3.0 and m3_m4<=3.2):
                        count2[15]+=1
                    elif (m3_m4>3.2 and m3_m4<=3.4):
                        count2[16]+=1
                    elif (m3_m4>3.4 and m3_m4<=3.6):
                        count2[17]+=1
                    elif (m3_m4>3.6 and m3_m4<=3.8):
                        count2[18]+=1
                    elif (m3_m4>3.8 and m3_m4<=4.0):
                        count2[19]+=1
            #print(count2)
            E3=[]
            E4=[]
            par_array_m3=[]
            par_array_m4=[]
            par_array_px3=[]
            par_array_px4=[]
            par_array_py3=[]
            par_array_py4=[]
            par_array_pz3=[]
            par_array_pz4=[]
            #//reset

            #count opp pairs addition
            #count1_2_opp=np.add(count1,count2)

            #similar pairs
            for i in range(0,len(par_array_m2)):
                E2 = (np.sqrt(float(par_array_px2[i])**2+float(par_array_py2[i])**2+float(par_array_pz2[i])**2+float(par_array_m2[i])**2))
                for j in range(0,len(par_array_m3)):
                    E3 = (np.sqrt(float(par_array_px3[j])**2+float(par_array_py3[j])**2+float(par_array_pz3[j])**2+float(par_array_m3[j])**2))
                    m2_m3=(np.sqrt(((E2+E3)**2)-((par_array_px2[i]+par_array_px3[j])**2+(par_array_py2[i]+par_array_py3[j])**2+(par_array_pz2[i]+par_array_pz3[j])**2)))
                    if (m2_m3>=0 and m2_m3<=0.2):
                        #print par_array_m1[i],par_array_m2[j],par_array_px1[i],par_array_py1[i],par_array_pz1[i],par_array_px2[j],par_array_py2[j],par_array_pz2[j],E1,E2,m1_m2
                        #exit()
                        count3[0]+=1
                    elif (m2_m3>0.2 and m2_m3<=0.4):
                        count3[1]+=1
                    elif (m2_m3>0.4 and m2_m3<=0.6):
                        count3[2]+=1
                    elif (m2_m3>0.6 and m2_m3<=0.8):
                        count3[3]+=1
                    elif (m2_m3>0.8 and m2_m3<=1.0):
                        count3[4]+=1
                    elif (m2_m3>1.0 and m2_m3<=1.2):
                        count3[5]+=1
                    elif (m2_m3>1.2 and m2_m3<=1.4):
                        count3[6]+=1
                    elif (m2_m3>1.4 and m2_m3<=1.6):
                        count3[7]+=1
                    elif (m2_m3>1.6 and m2_m3<=1.8):
                        count3[8]+=1
                    elif (m2_m3>1.8 and m2_m3<=2.0):
                        count3[9]+=1
                    elif (m2_m3>2.0 and m2_m3<=2.2):
                        count3[10]+=1
                    elif (m2_m3>2.2 and m2_m3<=2.4):
                        count3[11]+=1
                    elif (m2_m3>2.4 and m2_m3<=2.6):
                        count3[12]+=1
                    elif (m2_m3>2.6 and m2_m3<=2.8):
                        count3[13]+=1
                    elif (m2_m3>2.8 and m2_m3<=3.0):
                        count3[14]+=1
                    elif (m2_m3>3.0 and m2_m3<=3.2):
                        count3[15]+=1
                    elif (m2_m3>3.2 and m2_m3<=3.4):
                        count3[16]+=1
                    elif (m2_m3>3.4 and m2_m3<=3.6):
                        count3[17]+=1
                    elif (m2_m3>3.6 and m2_m3<=3.8):
                        count3[18]+=1
                    elif (m2_m3>3.8 and m2_m3<=4.0):
                        count3[19]+=1
                    #par_array_m1_m3.append(np.sqrt((E1 + E)**2 -(((energy1_array[1][i])+(energy2_array[1][j]))**2 +((energy1_array[2][i])+(energy2_array[2][j]))**2 +((energy1_array[3][i])+(energy2_array[3][j]))**2))
           
            #print (count3)
            #E1=[]
            #E3=[]
            par_array_m2=[]
            par_array_m3=[]
            par_array_px2=[]
            par_array_px3=[]
            par_array_py2=[]
            par_array_py3=[]
            par_array_pz2=[]
            par_array_pz3=[]
            #par_array_m1_m3=[]
            #par_array_pt1=[]

            for i in range(0,len(par_array_m1)):
                E1 = (np.sqrt(float(par_array_px1[i])**2+float(par_array_py1[i])**2+float(par_array_pz1[i])**2+float(par_array_m1[i])**2))
                for j in range(0,len(par_array_m4)):
                    E4 = (np.sqrt(float(par_array_px4[j])**2+float(par_array_py4[j])**2+float(par_array_pz4[j])**2+float(par_array_m4[j])**2))
                    m1_m4=(np.sqrt(((E1+E4)**2)-((par_array_px1[i]+par_array_px4[j])**2+(par_array_py1[i]+par_array_py4[j])**2+(par_array_pz1[i]+par_array_pz4[j])**2)))
                    if (m1_m4>=0 and m1_m4<=0.2):
                        #print par_array_m1[i],par_array_m2[j],par_array_px1[i],par_array_py1[i],par_array_pz1[i],par_array_px2[j],par_array_py2[j],par_array_pz2[j],E1,E2,m1_m2
                        #exit()
                        count4[0]+=1
                    elif (m1_m4>0.2 and m1_m4<=0.4):
                        count4[1]+=1
                    elif (m1_m4>0.4 and m1_m4<=0.6):
                        count4[2]+=1
                    elif (m1_m4>0.6 and m1_m4<=0.8):
                        count4[3]+=1
                    elif (m1_m4>0.8 and m1_m4<=1.0):
                        count4[4]+=1
                    elif (m1_m4>1.0 and m1_m4<=1.2):
                        count4[5]+=1
                    elif (m1_m4>1.2 and m1_m4<=1.4):
                        count4[6]+=1
                    elif (m1_m4>1.4 and m1_m4<=1.6):
                        count4[7]+=1
                    elif (m1_m4>1.6 and m1_m4<=1.8):
                        count4[8]+=1
                    elif (m1_m4>1.8 and m1_m4<=2.0):
                        count4[9]+=1
                    elif (m1_m4>2.0 and m1_m4<=2.2):
                        count4[10]+=1
                    elif (m1_m4>2.2 and m1_m4<=2.4):
                        count4[11]+=1
                    elif (m1_m4>2.4 and m1_m4<=2.6):
                        count4[12]+=1
                    elif (m1_m4>2.6 and m1_m4<=2.8):
                        count4[13]+=1
                    elif (m1_m4>2.8 and m1_m4<=3.0):
                        count4[14]+=1
                    elif (m1_m4>3.0 and m1_m4<=3.2):
                        count4[15]+=1
                    elif (m1_m4>3.2 and m1_m4<=3.4):
                        count4[16]+=1
                    elif (m1_m4>3.4 and m1_m4<=3.6):
                        count4[17]+=1
                    elif (m1_m4>3.6 and m1_m4<=3.8):
                        count4[18]+=1
                    elif (m1_m4>3.8 and m1_m4<=4.0):
                        count4[19]+=1
                    #par_array_m1_m3.append(np.sqrt((E1 + E)**2 -(((energy1_array[1][i])+(energy2_array[1][j]))**2 +((energy1_array[2][i])+(energy2_array[2][j]))**2 +((energy1_array[3][i])+(energy2_array[3][j]))**2))
           
            #print (count3)
            #E1=[]
            #E3=[]
            par_array_m1=[]
            par_array_m4=[]
            par_array_px1=[]
            par_array_px4=[]
            par_array_py1=[]
            par_array_py4=[]
            par_array_pz1=[]
            par_array_pz4=[]

            count3_4_sim=np.add(count3,count4)

            
        elif (len(ax)==9):  # 3!!
            #par_array_pz.append(float(ax[3]))
            #par_array_py.append(float(ax[2]))
            #par_array_px.append(float(ax[1]))
            #invariant_mass
            #par_array_m.append(float(ax[4]))
            #transverse_momentum
            #par_array_pt.append(np.sqrt(float(ax[1])**2 + float(ax[2])**2))
           # energy=np.sqrt(float(ax[1])**2+float(ax[2])**2+float(ax[3])**2+float(ax[4])**2)
            #print(abs(rapidity(energy, float(ax[3]))), rapidity(energy, float(ax[3])))
            #rapidity
           # if (abs(rapidity(energy, float(ax[3]))) < 0.8):
            #    count_dndy = count_dndy + 1
           # par_array_x.append(float(ax[5]))
           
            if (float(ax[0])==321):
                par_array_m1.append(float(ax[4]))
                #par_array_pt1.append(np.sqrt(float(ax[1])**2 + float(ax[2])**2))
                par_array_pz1.append(float(ax[3]))
                par_array_py1.append(float(ax[2]))
                par_array_px1.append(float(ax[1]))
                #for i in range(1,4):
                    #b1=(float(ax[i]))
                #energy1_array=np.vstack(float(ax[1]),float(ax[2]),float(ax[3]),float(ax[4]))
                #print energy1_array
                #count_bin_kaons = count_bin_kaons+1
            if (float(ax[0])==-211):
                par_array_m2.append(float(ax[4]))
                #par_array_pt2.append(np.sqrt(float(ax[1])**2 + float(ax[2])**2))
                par_array_pz2.append(float(ax[3]))
                par_array_py2.append(float(ax[2]))
                par_array_px2.append(float(ax[1]))
                #energy2_array=np.vstack(float(ax[1]),float(ax[2]),float(ax[3]),float(ax[4]))
                #count_bin_kaons = count_bin_kaons+1
            if (float(ax[0])==-321):
                par_array_m3.append(float(ax[4]))
                par_array_pz3.append(float(ax[3]))
                par_array_py3.append(float(ax[2]))
                par_array_px3.append(float(ax[1]))
                #par_array_pt3.append(np.sqrt(float(ax[1])**2 + float(ax[2])**2))
                #count_bin_kaons = count_bin_kaons+1
            if (float(ax[0])==211):
                par_array_m4.append(float(ax[4]))
                par_array_pz4.append(float(ax[3]))
                par_array_py4.append(float(ax[2]))
                par_array_px4.append(float(ax[1]))
                #par_array_pt4.append(np.sqrt(float(ax[1])**2 + float(ax[2])**2))
    
        #if(len(lines)==count_lines):
            #array_nkaons.append(count_bin_kaons)
            #evt_arr_count_dndy.append(count_dndy)
           
print(len(array_nkaons))
#print(len(par_array_pz))
print(len(par_array_pt1))
print (len(par_array_pt2))
print(evt_arr_nparts)
#print "count1:"
#print (count1)
#print "count2:"
#print (count2)
#print "count1_2_opp:"    
#print (count1_2_opp)
print "count3:"
print (count3)
print "count4:"
print (count4)
print "count3_4_sim:"
print (count3_4_sim)
#print (par_array_m1)
#print invariant mass
#print "Invariant Mass"
#print(par_array_m)
#histogram inv. mass
#plt.hist(par_array_m,bins=40)
#plt.xlabel("invariant mass")
#plt.ylabel("count")

#histogram trans. momentum
#plt.hist(par_array_pt, bins=70)
#plt.xlabel("Transverse momentum")
#plt.ylabel("count")
#plt.style.use('seaborn-deep')
'''plt.figure(1)
#plt.hist([par_array_m1,par_array_pt1],bins=40,label=['inv. mass','trans. momentum'])
plt.plot([par_array_m1])
plt.xlabel("inv. mass")
plt.title("k+")'''
'''
plt.figure(1)
plt.plot([par_array_m1,par_array_pt1])
plt.xlabel("tp & inv. mass")
#plt.legend(loc='upper right')
plt.title("k+")

plt.figure(2) #memory error!!
plt.plot([par_array_m2,par_array_pt2])
plt.xlabel("tp & inv. mass")
#plt.legend(loc='upper right')
plt.title("pi-")
'''
#plt.figure(3)
#plt.subplot(1,2,1)
#plt.hist([par_array_m1],bins=40)
#plt.xlabel("inv. mass")
#plt.subplot(1,2,2)
#plt.hist([par_array_pt1],bins=40)
#plt.xlabel("trans. momentum")
#plt.title("k+")

#plt.figure(4)
#plt.subplot(1,2,1)
#plt.hist([par_array_m2],bins=40)
#plt.xlabel("inv. mass")
#plt.subplot(1,2,2)
#plt.hist([par_array_pt2],bins=40)
#plt.xlabel("trans. momentum")
#plt.title("pi-")
#plt.xlim(xmin=-8,xmax=8)
#plt.legend(loc='upper right')

#plt.figure(5)
#plt.subplot(1,2,1)
#plt.hist([par_array_m3],bins=40)
#plt.xlabel("inv. mass")
#plt.subplot(1,2,2)
#plt.hist([par_array_pt3],bins=40)
#plt.xlabel("trans. momentum")
#plt.title("k-")

#plt.figure(6)
#plt.subplot(1,2,1)
#plt.hist([par_array_m4],bins=40)
#plt.xlabel("inv. mass")
#plt.subplot(1,2,2)
#plt.hist([par_array_pt4],bins=40)
#plt.xlabel("trans. momentum")
#plt.title("pi+")

#par_array_m1_m2=[x+y for x,y in product(par_array_m1,par_array_m2)]
#plt.figure(7)
#plt.hist([par_array_m1_m2],bins=40)
#plt.xlabel("inv. mass")
#plt.title("k+ + pi-")
#plt.figure(7)
#plt.hist( avg_pt1,bins=100)
#plt.title("k+ _pt_avg")
print "ok3"
#bin_array1=[]
#for i in np.arange(0.1,4,0.2):
    #bin_array1.append(float(i))
#plt.figure(8)
#plt.plot(bin_array1,count1)
#plt.scatter(bin_array1,count1)
#plt.xlim(xmin=0,xmax=4)
#plt.title("k+ + pi-")

#bin_array2=[]
#for i in np.arange(0.1,4,0.2):
    #bin_array2.append(float(i))
#plt.figure(9)
#plt.plot(bin_array2,count2)
#plt.scatter(bin_array2,count2)
#plt.xlim(xmin=0,xmax=4)
#plt.title("k- + pi+")

#bin_array3=[]
#for i in np.arange(0.1,4,0.2):
    #bin_array3.append(float(i))
#plt.figure(10)
#plt.plot(bin_array3,count1_2_opp)
#plt.scatter(bin_array3,count1_2_opp)
#plt.xlim(xmin=0,xmax=4)
#plt.title("k- + pi+ & k+ + pi-")

bin_array4=[]
for i in np.arange(0.1,4,0.2):
    bin_array4.append(float(i))
plt.figure(11)
plt.plot(bin_array4,count3)
plt.scatter(bin_array4,count3)
#plt.xlim(xmin=0,xmax=4)
plt.title("k- + pi-")

bin_array5=[]
for i in np.arange(0.1,4,0.2):
    bin_array5.append(float(i))
plt.figure(12)
plt.plot(bin_array5,count4)
plt.scatter(bin_array5,count4)
#plt.xlim(xmin=0,xmax=4)
plt.title("k+ + pi+")

bin_array6=[]
for i in np.arange(0.1,4,0.2):
    bin_array6.append(float(i))
plt.figure(13)
plt.plot(bin_array6,count3_4_sim)
plt.scatter(bin_array6,count3_4_sim)
#plt.xlim(xmin=0,xmax=4)
plt.title("k- + pi- & k+ + pi+")

count_final=np.subtract(count1_2_opp,count3_4_sim)
print "Invariant mass of kaon star :"
print (count_final)
bin_array7=[]
for i in np.arange(0.1,4,0.2):
    bin_array7.append(float(i))
plt.figure(14)
plt.plot(bin_array7,count_final)
plt.scatter(bin_array7,count_final)
#plt.xlim(xmin=0,xmax=4)
plt.title("kaon_star")
plt.show()
