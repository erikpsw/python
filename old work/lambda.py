f=lambda x : 3*x+1
print(f(3))
#multiple
full_name=lambda fn,ln:fn.strip().title()+' '+ln.strip().title()
print('shiwei','pan')
name=['Isaac Asimov','Ray Bradbury','Robert Heinlein']
name.sort(key=lambda name:name.split(' ')[-1].lower())
print(name)