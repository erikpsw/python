dir='C:\\Users\\Shiwei Pan\\source\\repos'
import os
import shutil
import time
despath='C:\mine\Qt\\'
list=os.listdir(dir)

num=9
#st_atime (访问时间), st_mtime (修改时间), st_ctime（创建时间）
for file in list:
    file_path=dir+'\\'+file
    mouth=time.localtime(os.stat(file_path).st_mtime).tm_mon
    if(mouth>=num):
        list1 = os.listdir(file_path)
        os.mkdir(despath+file)
        for i in list1:
            (shotname, extension)=os.path.splitext(i)
            if(extension!=''):
                print(despath+file+'\\'+i)
                shutil.copyfile(file_path+'\\'+i, despath+file+'\\'+i)

