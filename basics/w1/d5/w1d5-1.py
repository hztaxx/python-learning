# w1d5-1.py
f={'kfc':50,'mcd':40, "bk":30}
print(f['bk'])
f['tst']=20
print(f['tst'])
if 'bsk' in f:
    print('y')
else : 
    print('n')
x=f.get('kfc')
print(x)
y=f.get('kfj')
print(y)
y=f.get('kfj','gg')
print(y)
s={1,2,3}
s2=set([1,2,3])
print(s2)
s={1,2,3,1,2,1,2,4,2,6}
print(s)
s.remove(6)
print(s)
print(s2 & s)
print(s2|s)
