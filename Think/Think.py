"""
n = int(input("Sayı : "))

toplam = 0
tcarpim = 1
ctoplam = 0

if n >= 23:
    for i in range(3, n + 1):
        toplam = toplam + i
    for i in range(-23, n + 1):
        if i % 2 == 1:
            tcarpim = tcarpim * i
    for i in range(21, n + 1):
        if i % 2 == 0:
            ctoplam = ctoplam + i
    print("3 ile {} Arasındaki Sayıların Toplamı = {}".format(n, toplam))
    print("-23 ile {} Arasındaki Tek Sayıların Çarpımı = {}".format(n, tcarpim))
    print("21 ile {} Arasındaki Çift Sayıların Aritmetik Ortalaması = {}".format(n, ctoplam/2))
else:
    print("Sayı 23 Den Büyük Olmalı")
"""

i = int(input("İzin : "))
isaniye = i * 7 * 24 * 60 * 60
f = 1

for i in range(1, isaniye):
    f = f * i
    if f == isaniye:
        print("İzin Verilebilir")
        break
if f != isaniye:
    print("İzin Verilemez")
