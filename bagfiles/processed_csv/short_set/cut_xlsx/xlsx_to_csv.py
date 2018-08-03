# -*- coding:utf-8 –*-
'''
Reference: https://blog.csdn.net/Gipsy_Danger/article/details/80142396
程序用来将excel批量转换为csv文件。指定源路径和目标路径。
在main函数中指定源文件路径source，目标文件路径ob.
这个程序假设Excel文件放在：D:\CDDE
输出csv文件到：D:\cc
'''
 
#导入pandas
import pandas as pd
import os
 
 
#建立单个文件的excel转换成csv函数,file 是excel文件名，to_file 是csv文件名。
def excel_to_csv(file,to_file):
    data_xls=pd.read_excel(file,sheet_name=0)
    data_xls.to_csv(to_file,encoding='utf_8_sig')
 
 
 
#读取一个目录里面的所有文件：
def read_path(path):
    dirs=os.listdir(path)
    return dirs
 
#主函数
def main():
    #源文件路径
    source="C:\\Users\\苏宇恒\\Desktop\\数学建模\\25日"
 
    #目标文件路径
    ob="C:\\Users\\苏宇恒\\Desktop\\数学建模\\25日2"
 
    #将源文件路径里面的文件转换成列表file_list
    file_list=[source+'\\'+i for i in read_path(source)]
    j=1
    #建立循环对于每个文件调用excel_to_csv()
    for it in file_list:
        #给目标文件新建一些名字列表
        j_mid=str(j)
        j_csv=ob+'\\'+j_mid+".csv"
        excel_to_csv(it,j_csv)
        print(it)
        j=j+1
 
if __name__ == '__main__':
    main()
