
def f(x):
    return eval(func.replace('x', str(x)))

if __name__ == '__main__':
    func = input("Polynomial")

    a = float(input('left? '))
    b = float(input('right? '))

    if f(a) * f(b) > 0: # one is below 0 and one is above
        print("invalid interval")
        exit()

    while max(a, b) - min(a, b) > 0.000001:
        mid = (a + b)/2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    print(a)
