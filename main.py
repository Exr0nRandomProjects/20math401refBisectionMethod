poly = input('please input the polynomial: ')

y = float(input('value? '))
l = float(input('left? '))
r = float(input('right? '))

if l > r:
    l, r = r, l

while r - l > 1e-5:
    mid = (l + r)/2
    if (eval(poly.replace('x', str(mid))) > y) == (l > y):
        l = mid
    else:
        r = mid

print(l)

