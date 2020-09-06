text=r'''



\left. { A B ^ { 2 } + B C ^ { 2 } - 2 A B \cdot B C \cos \theta = A C ^ { 2 } } \\ { A B ^ { 2 } + A ( B C ) ^ { 2 } - 2 A B \cdot B C \cos ( \pi - \theta ) = B B ^ { 2 } } \\ { 2 ( A B ^ { 2 } + B C ^ { 2 } ) : A _ { c } ^ { 2 } + B D ^ { 2 } } \right.



'''
text=text.replace('\n', '').replace('\r', '')#去除最前面换行
print(text)
arr=text.split(r"\\")
print(arr)
print('\n\n\n')
arr[0]=arr[0][6:]
arr[-1]=arr[-1][:-7]
for i in arr:
    i='$'+i+'$'
    print(i)
