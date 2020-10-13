poly = input('please input the polynomial: ')

l = int(input('left? '))
r = int(input('right? '))

if l > r:
    l, r = r, l

while r - l > 1e-5:
    mid = (l + r)/2
    if (eval(poly.replace('x', str(mid))) > 0) == (l > 0):
        l = mid
    else:
        r = mid

print(l)

