dir='C:\\Users\\Shiwei Pan\\source\\repos'
import os
import shutil
import time
num=11
list=os.listdir(dir)
for file in list:
    file_path = dir + '\\' + file
    mouth = time.localtime(os.stat(file_path).st_mtime).tm_mon
    if (mouth < num):
        list1 = os.listdir(file_path)
        for i in list1:
            (shotname, extension) = os.path.splitext(i)
            if(shotname=='.vs'):
                vs_path = dir + '\\' + file
                str1 = 'cd ' + vs_path
                str2 = 'rd /s /q .vs'
                print(str1)
                print(str2)


