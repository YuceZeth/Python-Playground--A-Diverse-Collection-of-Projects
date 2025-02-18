"""
family_tree = {'Amca': {'Erkekler': ["Osman Güntekin", "Aykut Güntekin"], 'Kadınlar': ["Fadime Güntekin"]},
               'Hala': {'Erkekler': ["Cabbar Güneş"], 'Kadınlar': ["Azra Güneş", "Ayşe Güneş"]}}

print("Soyağacı :", family_tree)
print("Amca Çocukları :", family_tree['Amca'])
print("Hala Çocukları :", family_tree['Hala'])
"""

"""
bilgiler = []
isim = input("İsim giriniz : ")
soyisim = input("Soyisim giriniz :")
dogum_tarihi = input("Doğum Tarihini Giriniz : ")
tel = input("Tel :")
print("isim : {} soyisim : {} doğum tarihi : {} telefon numarası : {}".format(isim, soyisim, dogum_tarihi, tel))

bilgiler.append(isim)
bilgiler.append(soyisim)
bilgiler.append(dogum_tarihi)
bilgiler.append(tel)

print(bilgiler)
bilgiler.pop()
bilgiler.pop()
bilgiler.pop()
bilgiler.pop()
print(bilgiler)
"""

"""
dizi = [333, 1234.5, 1, 333, -1, 66.25]
dizi.sort()
print(dizi)
"""

"""
bilgiler = {}
kullanıcı_adı = input("Kullanıcı adı giriniz : ")
sifre = input("sifre giriniz : ")
bilgiler["kullanıcı_adı"] = kullanıcı_adı
bilgiler["sifre"] = sifre
print(sozluk)
"""

"""--- 21.12.2020 ---"""
"""
x = 0
ct = 0
tt = 0
while x < 223:
    x = x + 1

    if x % 2 == 0:
        print("Çift :", x)
        ct = ct + x
        if x % 9 == 0:
            print("Çift ve dokuza bölünen sayı :", x)

    if x % 2 == 1:
        print("Tek :", x)
        tt = tt + x
        if x % 7 == 0:
            print("Tek ve yediye bölünen sayı :", x)

    if x % 9 == 0:
        print("Dokuza bölünen sayı :", x)

    if x % 7 == 0:
        print("Yediye bölünen sayı :", x)

print("Çift toplam :", ct)
print("Tek toplam :", tt)
"""
"""
ct = 0
tt = 0
for i in range(0, 223):
    if i % 2 == 0:
        print("Çift sayı :", i)
        ct = ct + i
        if i % 9 == 0:
            print("Çift ve dokuza bölünen sayı :", i)
    if i % 2 == 1:
        print("Tek sayı :", i)
        tt = tt + i
        if i % 7 == 0:
            print("Tek ve yediye bölünen sayı :", i)
    if i % 9 == 0:
        print("Dokuza bölünen sayı :", i)
    if i % 7 == 0:
        print("Yediye bölünen sayı :", i)
print("Çift toplam :", ct)
print("Tek toplam :", tt)
"""
