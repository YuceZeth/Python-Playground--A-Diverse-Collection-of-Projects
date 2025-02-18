dikdortgenler = [(3, 4), (10, 3), (5, 6), (1, 9)]


def alan(x):
    for a,b in x:
       c = a * b
    return c

print(map(alan,[(3, 4), (10, 3), (5, 6), (1, 9)]))
