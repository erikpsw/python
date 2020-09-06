text=r'''



\left. { 4 y = 2 t x - t ^ { 2 } } \\ { t ^ { 2 } - 2 t x + 4 y = 0 } \\ { F ( x , y , t ) = t ^ { 2 } - 2 t x + 4 y }  \right.



'''
text=text.replace('\n', '').replace('\r', '')#去除最前面换行
text=text.replace(' ','')#去除空格
print(text)
arr=text.split(r"\\")
print(arr)
print('\n\n\n')
arr[0]=arr[0][6:]
arr[-1]=arr[-1][:-7]
for i in arr:
    i='$'+i+'$'
    print(i)
