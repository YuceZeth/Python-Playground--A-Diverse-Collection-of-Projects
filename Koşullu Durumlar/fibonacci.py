"""
a = 1
b = 1

fibonacci = [a,b]

for i in range(20):
    a,b = b,a+b

    fibonacci.append(b)

print(fibonacci)
"""

çift = []
tek = []

çift_çarpım = 1
çift_toplam = 0

tek_çarpım = 1
tek_toplam = 0

for i in range(1,33):
    if(i%2==0):
        çift.append(i)
        çift_çarpım *= i
        çift_toplam += i
    else:
        tek.append(i)
        tek_çarpım *= i
        tek_toplam += i

print("Çift Sayılar = ",çift)
print("Tek Sayılar",tek)
print("Çift Sayıların Çarpımı = {} \nÇift Sayıların Toplamı = {} ".format(çift_çarpım,çift_toplam))
print("Tek Sayıların Çarpımı = {} \nTek Sayıların Toplamı = {}".format(tek_çarpım,tek_toplam))

