text=r'''



\left. { y ^ { 2 } - a y + \frac { 1 } { 4 } a ^ { 2 } = 2 b x } \\ { 2 y \cdot \frac { d y } { d x } - a \frac { d y } { d x } + 0 = 2 b } \\ { \frac { d y } { d x } = \frac { 2 b } { 2 y - a } = \frac { b } { y - \frac { 1 } { 2 } a } } \right.




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
    print("\n")
