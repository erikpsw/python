datanames ='C:\\Users\\Shiwei Pan\\source\\repos'
import os
import shutil
i=1
despath='C:\mine\mine\python\computational geometry\\'
List=[]
Name=[]
for root, dirs, files in os.walk(datanames, topdown=False):
    for name in files:
        file_name=os.path.join(root, name)
        (shotname, extension)=os.path.splitext(name)
        if(extension=='.cpp'):
            List.append(file_name)
            Name.append(name)
            i=i+1
print(List)
print(Name)
for i in range(len(List)):
    shutil.copyfile(List[i], despath+Name[i])

