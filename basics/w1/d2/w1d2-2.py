# w1d2-2.py
print(ord('A'))
print('\u4e2d\u6587')
result = 'ABC'.encode('ascii')
print(result)  # 输出: b'ABC'
a= b'ABC'.decode('ascii')
print(a)
b=b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(b)
c=len('wudihzt')
print(c)
d=len('大帅逼'.encode('utf-8'))
print(d)
print('fuck,%s'%'you')
print('i have %d,%s'%(100000,'do you know'))
print('%2d-%02d' % (3, 1))
print('you 100%% have a phone')
print('you 100%% have a phone')  # 正确！
print('you 100%% have a phone')  # 正确！
print('方法1: you 100% have a phone')
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
a=10
b=99999
print(f'hzt有{a}万，他未来会有{b:.3f}倍这个钱')
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print(f'{r:.1f}%')