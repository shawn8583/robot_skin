import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# plot functions
x = np.linspace(200,1000,800)

x1_for_scatter = [936,520,380,333,264,249,238]
x2_for_scatter = [1023,555,321,281,250,224,211]
x3_for_scatter = [1023,510,319,250,225,204,185]
x4_for_scatter = [936,470,325,280,255,220,215]
x5_for_scatter = [1023,675,395,300,257,240,227]
x6_for_scatter = [999,515,338,295,230,213,191]
x7_for_scatter = [936,490,373,290,260,239,226]
x8_for_scatter = [1010,535,400,268,258,229,214]
x9_for_scatter = [1010,589,370,247,235,232,205]
x10_for_scatter = [815,480,365,270,255,223,221]
x11_for_scatter = [455,230,212,200,180,170,163]
x12_for_scatter = [856,445,370,271,235,192,181]
y_for_scatter = [0,1,2,3,4,5,6]

plt.scatter(x1_for_scatter,y_for_scatter)

def y1(x):
    y1 = (3.28e+05)*(x**(-1.995)) + (-0.313)
    return y1

def y2(x):
#    y2 = 

    return y2

def y3(x):
#    y3 = 

    return y3

def y3(x):
#    y3 =

    return y3

def y4(x):
#    y4 = 

    return y4

def y5(x):
#    y5 = 

    return y5

def y6(x):
#    y6 = 

    return y6

def y7(x):
#    y7 = 

    return y7

def y8(x):
#    y8 = 

    return y8

def y9(x):
#    y9 = 

    return y9

def y10(x):
#    y10 = 

    return y10

def y11(x):
#    y11 = 

    return y11

def y12(x):
#    y12 = 

    return y12


plt.plot(x, y1(x), linewidth=1,  label='id_1')
#plt.plot(x, y2(x), linewidth=1,  label='id_2')
#plt.plot(x, y3(x), linewidth=1,  label='id_3')
#plt.plot(x, y4(x), linewidth=1,  label='id_4')
#plt.plot(x, y5(x), linewidth=1,  label='id_5')
#plt.plot(x, y6(x), linewidth=1,  label='id_6')
#plt.plot(x, y7(x), linewidth=1,  label='id_7')
#plt.plot(x, y8(x), linewidth=1,  label='id_8')
#plt.plot(x, y9(x), linewidth=1,  label='id_9')
#plt.plot(x, y10(x), linewidth=1,  label='id_10')
#plt.plot(x, y11(x), linewidth=1,  label='id_11')
#plt.plot(x, y12(x), linewidth=1,  label='id_12')
plt.legend()
plt.show()


# This is done by the Curve Fitting Toolbox in MATLAB using "power fitting":
# 1. set x,y as inputs
# 2. open app --> curve fitting toolbox --> choose x and y --> choose power
#
# ***********************************************************************
# Getting functions after Curve Fitting:
# ***********************************************************************
#
# y1 = 
#
#
#
#



# For plotting scatter plots, reference: https://www.cnblogs.com/sunshinewang/p/6853813.html
