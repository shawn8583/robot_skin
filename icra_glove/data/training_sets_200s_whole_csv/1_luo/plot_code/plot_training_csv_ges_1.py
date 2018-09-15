import csv
from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl

filename_1 = '1.csv'
#filename_2 = '2.csv'
#filename_3 = '3.csv'
#filename_4 = '4.csv'
#filename_5 = '5.csv'
#filename_6 = '6.csv'
#filename_7 = '7.csv'
#filename_8 = '8.csv'
#filename_9 = '9.csv'
#filename_N = 'N.csv'
#filename_C = 'C.csv'
#filename_k = 'K.csv'

with open(filename_1) as f1:
    reader = csv.reader(f1)
    header_row = next(reader)
    sequence, taxel0, taxel1, taxel2, taxel3, taxel4, taxel5, taxel6, taxel7, taxel8, taxel9, taxel10, taxel11 = [],[],[],[],[],[],[],[],[],[],[],[],[]
    maxi = 1024
    for row in reader:
        seq = float(row[1])
        sequence.append(seq/maxi)
        data0 = float(row[4])
        taxel0.append(data0/maxi)
        data1 = float(row[5])
        taxel1.append(data1/maxi)
        data2 = float(row[6])
        taxel2.append(data2/maxi)
        data3 = float(row[7])
        taxel3.append(data3/maxi)
        data4 = float(row[8])
        taxel4.append(data4/maxi)
        data5 = float(row[9])
        taxel5.append(data5/maxi)
        data6 = float(row[10])
        taxel6.append(data6/maxi)
        data7 = float(row[11])
        taxel7.append(data7/maxi)
        data8 = float(row[12])
        taxel8.append(data8/maxi)
        data9 = float(row[13])
        taxel9.append(data9/maxi)
        data10 = float(row[14])
        taxel10.append(data10/maxi)
        data11 = float(row[15])
        taxel11.append(data11/maxi)

np.array(sequence)
np.array(taxel0)
np.array(taxel1)
np.array(taxel2)
np.array(taxel3)
np.array(taxel4)
np.array(taxel5)
np.array(taxel6)
np.array(taxel7)
np.array(taxel8)
np.array(taxel9)
np.array(taxel10)
np.array(taxel11)

# plot data
plt.figure('Draw')
plt.title('gesture_1_csv_plot')
plt.plot(sequence, taxel0, label='taxel_1')
plt.plot(sequence, taxel1, label='taxel_2')
plt.plot(sequence, taxel2, label='taxel_3')
plt.plot(sequence, taxel3, label='taxel_4')
plt.plot(sequence, taxel4, label='taxel_5')
plt.plot(sequence, taxel5, label='taxel_6')
plt.plot(sequence, taxel6, label='taxel_7')
plt.plot(sequence, taxel7, label='taxel_8')
plt.plot(sequence, taxel8, label='taxel_9')
plt.plot(sequence, taxel9, label='taxel_10')
plt.plot(sequence, taxel10, label='taxel_11')
plt.plot(sequence, taxel11, label='taxel_12')
plt.legend()

plt.xlabel('time sequence')
plt.ylabel('taxel value')
plt.show()
