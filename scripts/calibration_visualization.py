import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

newton = [0,1,2,3,4]
p1_value = [936,520,380,333,264]
p2_value = [1023,555,321,281,250]
p3_value = [1023,510,319,250,225]
p4_value = [936,470,325,280,255]
p5_value = [1023,675,395,300,257]
p6_value = [999,515,338,295,230]
p7_value = [936,490,373,290,260]
p8_value = [1010,535,400,268,258]
p9_value = [1010,589,370,247,235]
p10_value = [815,480,365,270,255]
p11_value = [455,230,212,200,180]
p12_value = [856,445,370,271,235]


plt.figure('Draw')
plt.title('Calibration')
plt.plot(newton, p1_value, marker='x', label='id_1')
plt.plot(newton, p2_value, marker='x', label='id_2')
plt.plot(newton, p3_value, marker='x', label='id_3')
plt.plot(newton, p4_value, marker='x', label='id_4')
plt.plot(newton, p5_value, marker='x', label='id_5')
plt.plot(newton, p6_value, marker='x', label='id_6')
plt.plot(newton, p7_value, marker='x', label='id_7')
plt.plot(newton, p8_value, marker='x', label='id_8')
plt.plot(newton, p9_value, marker='x', label='id_9')
plt.plot(newton, p10_value, marker='x', label='id_10')
plt.plot(newton, p11_value, marker='x', label='id_11')
plt.plot(newton, p12_value, marker='x', label='id_12')
plt.legend()

plt.xlabel('force/N')
plt.ylabel('values')
plt.show()
