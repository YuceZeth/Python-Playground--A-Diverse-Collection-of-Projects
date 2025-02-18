"""
1-

while True:
    s = int(input("Sayı giriniz : "))
    if 10 < s < 15:
        break
"""
"""
2-

s = int(input("Sayı giriniz : "))
i = 0
while i < s:
    i = i + 1
    if i % 2 == 1:
        print("{} Sayısı tektir...".format(i))
"""
"""
3-

i = 100
a = 0
z = 100
while z <= 110:
    if i % 2 == 0:
        i = i / 2
        a = a + 1
        continue
    elif i == 1:
        print("{} Sayısı {} Adımda gerçekleşti...".format(z, a))
        i = i + z
        z = z + 1
        a = 0
        continue
    else:
        i = 3 * i + 1
        a = a + 1
        continue
"""
"""
4-

s = int(input("Kaç sayı girmek istiyorsunuz : "))
i = 1
a = 0
at = 0
g = 1
gt = 0
b = []

while i <= s:
    z = int(input("Sayı giriniz : "))
    b.append(z)
    a = a + z
    g = g * z
    i = i + 1

min = b[1]
maks = b[1]
for o in b:
    if o < min:
        min = o
    elif o > maks:
        maks = o

at = a / s
gt = g ** (1/s)
print("Aritmetik ortalaması : {} \nGeometrik ortalaması : {} \nEn büyük sayı : {} \nEn küçük sayı : {}".format(at, gt, maks, min))
"""
"""
import random
ogr_no = []
vize = []
final = []
ortalama = []
durum = []
i = 0
j = 0
t = 0
w = 0
o = 0
while i <= 99:
    ogr_no.append(i)
    i = i + 1
print("Öğrenci numaraları : ", ogr_no)
while j <= 99:
    x = random.randint(1, 100)
    vize.append(x)
    j = j + 1
print("Vize notları : ", vize)
while t <= 99:
    e = random.randint(1, 100)
    final.append(e)
    t = t + 1
print("Final notları : ", final)
while w <= 99:
    v = vize[w] * (2/5)
    f = final[w] * (3/5)
    islem = f + v
    ortalama.append(islem)
    w = w + 1
print("Ortalamalar : ", ortalama)
while o <= 99:
    if ortalama[o] > 50:
        durum.append("G")
    else:
        durum.append("K")
    o = o + 1
print("Not durumları : ", durum)

print("Öğrenci Sorgulama")
s1 = int(input("Sorgulamak istediğiniz öğrencinin numarası : "))
if 0 <= s1 <= 99:
    print("{} Numaralı öğrencinin durumu : {}".format(s1, durum[s1]))
else:
    print("Geçersiz öğrenci numarası")
while True:
    s2 = input("Başka öğrenci durumu incelemek ister misiniz ? (E/H) : ")
    if s2 == 'E':
        s1 = int(input("Sorgulamak istediğiniz öğrencinin numarası : "))
        if 0 <= s1 <= 99:
            print("{} Numaralı öğrencinin durumu : {}".format(s1, durum[s1]))
        else:
            print("Geçersiz öğrenci numarası")
    else:
        break
"""