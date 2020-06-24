datanames ='G:\programing\\vs\C++'
import os
import shutil
i=1
despath='C:\\mine\\mine\\c++\\'
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
    shutil.move(List[i], despath+Name[i])



