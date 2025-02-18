"""
1-

for i in range(1, 11):
    print(i)
"""
"""
2-

s = int(input("Sayı giriniz : "))
t = 0
for i in range(1, s+1):
    t = t + i
print("Toplam : {}".format(t))
"""
"""
3-

x = int(input("Sayı giriniz : "))
f = 1
for i in range(1, x+1):
    f = f * i
print("{} Sayısının faktoriyeli {} dur...".format(x, f))
"""
"""
4-

x = input("Sayı giriniz : ")
rt = 0
rc = 1
for i in x:
    r = int(i)
    rt = rt + r
    rc = rc * r
print("Girilen sayının rakamları toplam {} dur. \nGirilen sayının rakamları çarpımı {} dur.".format(rt, rc))
"""
"""
5-

for i in range(1, 101):
    bt = 0
    for j in range(1, i):
        if i % j == 0:
            bt += j
    if i == bt:
        print("{} Sayısı mükemmel sayıdır...".format(i))
"""
"""
6-

for i in range(1, 101):
    at = 0
    for j in range(1, i+1):
        if i % j == 0:
            at = at + j
    if at == i+1:
        print("{} Sayısı asaldır...".format(i))
"""
"""
7-

s = int(input("Sayı giriniz : "))
asal = []
dizi = []
for i in range(1, s):
    at = 0
    for j in range(1, i + 1):
        if i % j == 0:
            at = at + j
    if at == i + 1:
        asal.append(i)

for q in asal:
    for w in asal:
        if q != w:
            if q * w < s:
                dizi.append(q*w)

dizi = list(set(dizi))
print("Yarı asal Sayılar : ",dizi)
"""
"""
8-

s = int(input("Sayı giriniz : "))
for i in range(10, s):
    b = str(i)
    t = 0
    for j in b:
        r = int(j)**len(b)
        t += r
    if i == t:
        print("{} Sayısı armstrong sayısıdır...".format(i))
"""