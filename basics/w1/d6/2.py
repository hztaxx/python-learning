import math
def quadratic(a,b,c):
    d=math.sqrt(b*b-4*a*c)
    x1=(-b+d)/2/a
    x2=(-b-d)/2/a
    print(x1,x2)
print(quadratic(1,8,3))
    


