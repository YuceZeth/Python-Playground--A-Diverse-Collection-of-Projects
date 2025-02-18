"""
1 –

s = int(input("Sayı giriniz : "))
if s % 2 == 0:
    print("{} Sayısı çifttir...".format(s))
else:
    print("{} Sayısı tektir...".format(s))
"""
"""
2 –

s1 = int(input("Sayı giriniz : "))
s2 = int(input("Sayı giriniz : "))
s3 = int(input("Sayı giriniz : "))
if s1 > s2 and s1 > s3:
    print("{} En büyüktür".format(s1))
elif s2 > s1 and s2 > s3:
    print("{} En büyüktür".format(s2))
else:
    print("{} En büyüktür".format(s3))
"""
"""
3 –

n = int(input("Not giriniz"))
if 0 < n < 49:
    print("Başarısız")
elif 50 < n < 64:
    print("Orta")
elif 65 < n < 84:
    print("İyi")
elif 85 < n < 100:
    print("Başarılı")
else:
    print("Geçersiz not")
"""
"""
4 –

print("ax^2 + bx + c")
a = int(input("a değeri : "))
b = int(input("b değeri : "))
c = int(input("c değeri : "))
delta = b ** 2 - 4 * a * c
if delta > 0:
    print("İki reel kök vardır...")
    k1 = (-b + delta ** 0.5) / (2 * a)
    k2 = (-b - delta ** 0.5) / (2 * a)
    print("denklemin kökleri {} ve {} dur...".format(k1, k2))
elif delta == 0:
    print("Çift katlı kökü vardır...")
    k1 = (-b + delta ** 0.5) / (2 * a)
    print("Denklemin kökü {} dur...".format(k1))
else:
    print("Kök yoktur...")
"""
"""
5 –

m = int(input("Maaş : "))
c = int(input("Çocuk sayısı : "))
p = int(input("Parça sayısı :"))
ay = 0
up = 0
if c == 1:
    ay = m * (1/20)
elif c == 2:
    ay = m * (1/10)
elif c >= 3:
    ay = m * (3/20)
else:
    print("Geçersiz çocuk sayısı...")
if 50 < p <= 100:
    up = m * (1/10)
elif 100 < p <= 150:
    up = m * (3/20)
elif 150 < p <= 200:
    up = m * (1/5)
ym = m + ay + up
print("Yeni maaş : ", ym)
"""
"""
6 -

g = int(input('Yıllık Gelir = '))
if g <= 150000:
    v = g * 0.25
elif g <= 300000:
    v = 150000 * 0.25 + (g - 150000) * 0.3
elif g <= 600000:
    v = 150000 * 0.25 + 150000 * 0.3 + (g - 300000) * 0.35
elif g <= 1200000:
    v = 150000 * 0.25 + 150000 * 0.3 + 300000 * 0.35 + (g - 600000) * 0.4
else:
    v = 150000 * 0.25 + 150000 * 0.3 + 300000 * 0.35 + 600000 * 0.4 + (g - 1200000) * 0.5
print("Vergi = ", v)
"""