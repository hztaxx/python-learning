# w1d3-3.py
x=float(input('h='))
y=float(input('w='))
bmi=y/(x*x)
print(bmi)
if bmi<=18.5:
    print('过轻')
elif bmi<=25:
    print('正常')
elif   bmi<=32:
    print('肥胖')
else:print('严重肥胖')