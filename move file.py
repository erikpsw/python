dir='C:\\Users\\Shiwei Pan\\source\\repos'
import os
import shutil
import time
despath='C:\mine\windows_app'
list=os.listdir(dir)

num=9
#st_atime (访问时间), st_mtime (修改时间), st_ctime（创建时间）
for file in list:
    file_path=dir+'\\'+file
    mouth=time.localtime(os.stat(file_path).st_mtime).tm_mon
    if(mouth>=num):
        list1 = os.listdir(file_path)
        tar_list=os.listdir(despath)
        if(file not in tar_list):
            os.mkdir(despath+'\\'+file)
        for i in list1:
            (shotname, extension)=os.path.splitext(i)
            if(extension!=''):
                shutil.copyfile(file_path+'\\'+i, despath+'\\'+file+'\\'+i)
        if ('obj' in list1):
            list2=os.listdir(file_path+ '\\' + 'obj'+'\\'+'Debug')
            for j in list2:
                (shotname, extension) = os.path.splitext(j)
                if (extension=='.exe'):
                    shutil.copyfile(file_path + '\\' + 'obj'+'\\'+'Debug'+'\\'+j, despath+'\\'+file+'\\'+ j)
