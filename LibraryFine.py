d,m,y = map(int, input().split(' '))
d2,m2,y2 = map(int, input().split(' '))

if y == y2:
    if m == m2:
        if d == d2 or d < d2:
            print(0)
        else:
            print ((d-d2) * 15)
            
    elif m > m2:
        print ((m-m2) * 500)
    elif m < m2:
        print(0)
 
elif y > y2:
    print(10000)
elif y < y2:
    print(0)
