
print('Triangle Inequality')


x = input('enter value of side a -->')
a = int(x)

y = input('enter value of side b -->')
b = int(y)

z = input('enter value of side c -->')
c = int(z)


print('a + b =',a + b)
if a + b > c:
    print(a + b, '>', c)
else:
    print(a + b , '<=', c)

print('b + c =', b + c)
if b + c > a:
    print(b + c, '>', a)
else:
    print(b + c , '<=', a)

print('a + c =', a + c)
if a + c > b:
    print(a + c, '>', b)
else:
    print(a + c , '<=', b)

    
if a + b > c and b + c > a and a + c > b:
    print('this will form a triangle')
    
else:
    print('this cannot form a triangle')
    