
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
def game(name,point,player='adult',year=2024):
    print('name:', name)
    print('point:', point)
    print('player:', player)
    print('year:', year)
game('black wukong',10.0)
def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end(L=[]))
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))
def game1(name,point,**kw):
    print('name:', name)
    print('point:', point)
    if 'player' in kw:
        pass
    if 'year'in kw:
        pass
    print('other',kw)
game1('black wukong',10.0,year=2024)
def game2(name,point,*,player,year):
    print('name:', name)
    print('point:', point)
    print('player:', player)
    print('year:', year)
game2('black wukong',10.0,player='me',year=2024)
def game3(name,point,*k,player,year):
    print('name:', name)
    print('point:', point)
    print(1,k)
    print('player:', player)
    print('year:', year)
game3('black wukong',10.0,player='me',year=2024)




