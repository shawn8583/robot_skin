import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

def taxel_2cm_x_2cm(x):
    taxel_2cm_x_2cm = (-3.103e-08)*(x-10)**3 + (6.976e-05)*(x-10)**2 + (-0.05346)*(x-10) + 14.17
    return taxel_2cm_x_2cm

def taxel_15cm_x_15cm(x):
    taxel_15cm_x_15cm = (8.355e-11)*x**4 + (-2.17e-07)*x**3 + (0.0002153)*x**2 + (-0.09995)*x + 18.9
    return taxel_15cm_x_15cm

def taxel_1cm_x_1cm(x):
    taxel_1cm_x_1cm = (-2.391e-08)*(x+5)**3 + (5.507e-05)*(x+5)**2 + (-0.04256)*(x+5) + 11.13
    return taxel_1cm_x_1cm

# tested taxel 4
original = np.array([1024,1024,1024,1024,1024,1024])
newton = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4]
cm2_1 = [902,725,690,665,640,634,580,552,545,518,508,490,478,459,450,469,440,438,421,402,390,371,374,370,363,365,340,335,329,320,319,322,325,311,314,318,310,305,294,284,292]
cm2_2 = [908,775,730,692,668,654,606,601,584,548,550,525,500,498,480,455,433,430,445,425,409,401,371,390,380,375,355,350,330,339,320,329,327,325,320,310,320,312,300,298,297]
cm2_3 = [905,490,396,320,290,269]
cm2_4 = [900,502,392,319,286,267]
cm2_5 = [899,499,394,328,282,263]

cm15_1 = [900,675,660,625,612,584,551,534,510,498,470,465,450,433,432,418,411,370,379,366,360,355,349,347,337,336,332,318,315,311,300,307,310,289,290,288,280,277,271,268,250]
cm15_2 = [902,668,655,627,601,564,533,545,500,479,460,421,430,418,409,411,398,377,368,370,359,360,342,338,325,314,318,305,300,289,292,275,280,277,268,266,260,262,258,252,245]
cm15_3 = [901,468,363,317,269,255]
cm15_4 = [901,469,366,316,270,251]
cm15_5 = [902,462,365,319,267,253]

cm1_1 = [900,634,622,601,578,522,504,497,471,459,435,420,411,409,400,381,391,377,369,351,340,334,319,320,315,310,301,305,297,307,290,274,266,249,245,237,246,232,238,227,225]
cm1_2 = [902,605,579,567,556,520,500,477,476,437,430,415,402,386,377,360,355,369,346,323,332,320,315,325,300,308,297,294,289,276,280,260,255,264,252,255,240,246,242,250,234]
cm1_3 = [900,430,328,300,259,248]
cm1_4 = [906,440,340,302,258,250]
cm1_5 = [900,445,338,310,257,244]

# plot scatter
plt.figure('Draw')
plt.scatter(cm2_1, newton, linewidth=3, color='red', label='2cm x 2cm')
plt.scatter(cm2_2, newton, linewidth=3, color='red')
# plt.scatter(cm2_3, newton, linewidth=3, color='red')
# plt.scatter(cm2_4, newton, linewidth=4, color='red')
# plt.scatter(cm2_5, newton, linewidth=4, color='red')

plt.scatter(cm15_1, newton, linewidth=3, color='green', label='1.5cm x 1.5cm')
plt.scatter(cm15_2, newton, linewidth=3, color='green')
# plt.scatter(cm15_3, newton, linewidth=4, color='green')
# plt.scatter(cm15_4, newton, linewidth=4, color='green')
# plt.scatter(cm15_5, newton, linewidth=4, color='green')

plt.scatter(cm1_1, newton, linewidth=3, color='blue', label='1cm x 1cm')
plt.scatter(cm1_2, newton, linewidth=3, color='blue')
# plt.scatter(cm1_3, newton, linewidth=4, color='blue')
# plt.scatter(cm1_4, newton, linewidth=4, color='blue')
# plt.scatter(cm1_5, newton, linewidth=4, color='blue')


# polynomial fitting
x2 = np.linspace(300, 800, (800-300)*100)
x15 = np.linspace(265,700, (800-265)*100)
x1 = np.linspace(230,640, (640-230)*100)
plt.plot(x2, taxel_2cm_x_2cm(x2), linewidth=4, color='black')
plt.plot(x15, taxel_15cm_x_15cm(x15), linewidth=4, color='black')
plt.plot(x1, taxel_1cm_x_1cm(x1), linewidth=4, color='black')
plt.plot()


plt.ylabel('Force/N', fontsize = 14)
plt.xlabel('ADC', fontsize = 14)
plt.legend()
plt.show()
