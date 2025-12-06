# w1d4-1.py
h=173
match h:
    case x if x<=140:
        print('not very tall')
    case y if y<=160:
        print('not bad')
    case z if z<=170:
        print('it\'s ok')
    case 171|172|173|174|175:
        print('good')
    case 176|177|178|179|180:
        print('very good')
    case t if t<=190:
        print('so good')
    case g if g<191:
        print('perfect')
color = ['red','black','green']
match color:
    case list() if 'black' in color:
        print('not good')
    case['red',file1,*files]:
        print('so much colors')
    case['red']:
        print('good')
    case _:
        print('well')