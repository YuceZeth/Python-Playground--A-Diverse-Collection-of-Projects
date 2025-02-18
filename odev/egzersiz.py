"""
1 – Klavyeden girilen sayı için tek-çift kontrolü yapan programı yazınız.

s = int(input("Sayı wer : "))
if s % 2 == 0:
    print("{} Sayısı çifttir...".format(s))
else:
    print("{} Sayısı tektir...".format(s))
"""
"""
2 – Klavyeden girilen 3 sayıdan en büyüğünü ekrana yazan programı yazınız.

s1 = int(input("Sayı wer : "))
s2 = int(input("Sayı wer : "))
s3 = int(input("Sayı wer : "))

if s1 > s2 and s1 > s3:
    print("{} En büyüktür".format(s1))
elif s2 > s1 and s2 > s3:
    print("{} En büyüktür".format(s2))
else:
    print("{} En büyüktür".format(s3))
"""
"""
4 – Kullanıcıdan ikinci derece bir denklem a,b,c değerleri alıp deltaya göre kök bulan programı yazınız.

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
1- 1’den 10’a kadar olan sayıları yazan programı yazınız.

for i in range(1, 11):
    print(i)
"""
"""
2- 1’den kullanıcının girdiği sayıya kadar olan sayıların toplamını bulan programı yazınız.

s = int(input("Sayı wer : "))
t = 0
for i in range(1, s+1):
    t = t + i
print("Toplam : {}".format(t))
"""
"""
3- Girilen sayının faktöriyelini bulan programı yazınız.

x = int(input("Sayı wer : "))
f = 1
for i in range(1, x+1):
    f = f * i
print("{} Sayısının faktoriyeli {} dur...".format(x, f))
"""
"""
4- Girilen sayının rakamları toplamı ve rakamları çarpımını ekrana yazan programı yazınız.

x = input("Sayı wer : ")
rt = 0
rc = 1
for i in x:
    r = int(i)
    rt = rt + r
    rc = rc * r
print("Girilen sayının rakamları toplam {} dur. \nGirilen sayının rakamları çarpımı {} dur.".format(rt, rc))
"""
"""
5- 1’den 100’e kadar olan mükemmel sayıları bulan programı yazınız.

for i in range(1, 101):
    bt = 0
    for j in range(1, i):
        if i % j == 0:
            bt += j
    if i == bt:
        print("{} Sayısı mükemmel sayıdır...".format(i))
"""
"""
6- 2’den 100’e kadar olan asalları yazan programı bulunuz.

for i in range(1, 101):
    at = 0
    for j in range(1, i+1):
        if i % j == 0:
            at = at + j
    if at == i+1:
        print("{} Sayısı asaldır...".format(i))
"""
"""
1- Klavyeden ardı ardına sayı girişi isteyen ve bu sayı 10 ile 15 arasında olmadığı sürece bu işleme devam eden programı yazınız.

while True:
    s = int(input("Sayı wer : "))
    if 10 < s < 15:
        break
"""
"""
2- Kullanıcının girdiği sayıya kadar olan pozitif tek sayıları ekrana yazan programı while ve continue kullanarak yazınız

s = int(input("Sayı wer : "))
i = 0
while i < s:
    i = i + 1
    if i % 2 == 1:
        print("{} Sayısı tektir...".format(i))
"""
"""
3- n sayısı belirli işlemlerle 1’e eşitlenmek istenmektedir. n -> n/2 (n çift ise) n -> 3n + 1 (n tek ise) şeklindedir.
Bu kuralı kullanarak 100 ile 110 arasındaki sayıların kaç adımda 1 e eriştiğini ekrana yazan bir program yazınız.


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
4- Kullanıcının istediği kadar girdiği sayıların aritmetik ortalamasını, geometrik ortalamasını, en büyüğünü, en küçüğünü bulan programı yazınız. 

s = int(input("Kaç sayı girmek istiyorsunuz : "))
i = 1
a = 0
at = 0
g = 1
gt = 0
efe = []

while i <= s:
    z = int(input("Sayı wer : "))
    efe.append(z)
    a = a + z
    g = g * z
    i = i + 1
    
min = efe[1]
maks = efe[1]
for o in efe:
    if o < min:
        min = o
    elif o > maks:
        maks = o

at = a / s
gt = g ** (1/s)
print("Aritmetik ortalaması : {} \nGeometrik ortalaması : {} \nEn büyük sayı : {} \nEn küçük sayı : {}".format(at, gt, maks, min))
"""
"""
k1 = int(input("Birinci  kenarı giriniz  : "))
k2 = int(input("İkinci   kenarı giriniz  : "))
k3 = int(input("Üçüncü   kenarı giriniz  : "))
k4 = int(input("Dördüncü kenarı giriniz  : "))

if k1 == k2 and k1 == k3 and k1 == k4:
    print("Şekil Karedir...")
elif k1 == k3 and k2 == k4:
    print("Şekil Dikdörtgendir...")
else:
    print("Şekil Yamuktur...")
"""
"""
isim = input("İsim : ")
soyisim = input("Soyisim : ")
cinsiyet = input("Cinsiyet : ")
medeni_durum = input("Medeni Durum : ")
x = medeni_durum.upper()
if x == 'EVLI':
    kisim = input("Eşinizin isimi : ")
    kcinsiyet = "Kadın"
    print("Bilgiler...\nİsim : {}\nSoyisim : {}\nCinsiyet : {}\nMedeni durum : {}\nEşinizin Bilgileri...\nİsim : {}\nSoyisim : {}\nCinsiyet : {}\nMedeni Durum : {}".format(isim, soyisim, cinsiyet, medeni_durum, kisim, soyisim, kcinsiyet, medeni_durum))
elif == "BEKAR":
    print("Bilgiler...\nİsim : {}\nSoyisim : {}\nCinsiyet : {}\nMedeni durum : {}".format(isim, soyisim, cinsiyet, medeni_durum))
else:
    print("Geçersiz medeni durum...")
"""
"""
ogrenci = {}
ogrenci["ogrenci no"] = input("Öğrenci numarası : ")
ogrenci["isim"] = input("İsim : ")
ogrenci["ara sınav"] = input("Ara sınav : ")
ogrenci["final"] = input("Final : ")

ort = (int(ogrenci["ara sınav"]) + int(ogrenci["final"])) / 2
if ort > 35:
    print("Geçtiniz...")
else:
    print("Kaldınız...")
"""
"""
ilk_sayac = int(input("İlk sayaç değeri : "))
son_sayac = int(input("Son sayaç değeri : "))
yer = input("Yer : ")
x = yer.upper()
sayac = abs(ilk_sayac - son_sayac)
if x == "YERI":
    fatura = sayac * 2
    print("Faturanız : {} Tl'dir".format(fatura))
elif x == "MESKEN":
    if sayac < 50:
        fatura = sayac * 1
        print("Faturanız : {} Tl'dir".format(fatura))
    elif sayac < 100:
        fatura = 50 * 1 + (sayac-50) * 2
        print("Faturanız : {} Tl'dir".format(fatura))
    else:
        fatura = 50 * 1 + 50 * 2 + (sayac-100) * 3
        print("Faturanız : {} Tl'dir".format(fatura))
"""
"""
sozluk = {"kuş": "bird",
          "masa": "table",
          "saat": "clock"}
print("\n
Kelime eklemek      için 1\n
Kelime silmek       için 2\n
Kelime güncellemek  için 3\n
Kelime görüntülemek için 4\n
")

while True:
    islem = int(input("İşlem seçiniz (Çıkmak için 0): "))
    if islem == 1:
        while True:
            anahtar = input("Anahtar kelimeyi giriniz : ")
            goruntusu = input("Görüntüsünü giriniz : ")
            sozluk[anahtar] = goruntusu
            print(sozluk)
            secim = input("Başka bir kelime girmek ister misiniz (E/H) : ")
            s = secim.upper()
            if s == "E":
                continue
            else:
                break
    elif islem == 2:
        while True:
            print(sozluk)
            secim = input("Silmek istediğiniz kelimeyi giriniz (Anahtar kelimesi): ")
            if secim in sozluk:
                sozluk.pop(secim)
                print(sozluk)
            else:
                print("Kelime bulunamadı...")
            secim2 = input("Başka kelime silmek ister misiniz (E/H) : ")
            s = secim2.upper()
            if s == "E":
                continue
            else:
                break
    elif islem == 3:
        while True:
            print(sozluk)
            secim = input("Güncellemek istediğiniz kelimeyi giriniz (Anahtar kelimesi): ")
            if secim in sozluk:
                sozluk[secim] = input("Yeni görüntüsü : ")
                print(sozluk)
            else:
                print("Kelime bulunamadı...")
            secim2 = input("Başka kelime Güncellemek ister misiniz (E/H) : ")
            s = secim2.upper()
            if s == "E":
                continue
            else:
                break
    elif islem == 4:
        while True:
            secim = input("Görüntülemek istediğiniz kelime (hepsi ise h) : ")
            if secim != "h":
                if secim in sozluk:
                    print(sozluk[secim])
                else:
                    print("Kelime bulunamadı...")
            else:
                print(sozluk)
            secim2 = input("Başka kelime Görüntülemek ister misiniz (E/H) : ")
            s = secim2.upper()
            if s == "E":
                continue
            else:
                break
    elif islem == 0:
        break
    else:
        print("Geçersiz İşlem...")
        continue
"""
"""
s1 = int(input("Birinci sayıyı giriniz : "))
s2 = int(input("İkinci  sayıyı giriniz : "))

st1 = 0
for i in range(1, s1):
    if s1 % i == 0:
        st1 = st1 + i
st2 = 0
for j in range(1, s2):
    if s2 % j == 0:
        st2 = st2 + j

if st2 == s1 and st1 == s2:
    nt1 = 0
    for i in str(s1):
        nt1 = nt1 + int(i)
    nt2 = 0
    for j in str(s2):
        nt2 = nt2 + int(j)

    if s1 % nt1 == 0 and s2 % nt2 == 0:
        print("{} sayısı ve {} sayısı niven arkadaş sayıdır...".format(s1, s2))
    else:
        print("{} sayısı ve {} sayısı arkadaş sayıdır...".format(s1, s2))
"""
"""
birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
yuzler = ["", "Yüz", "İkiyüz", "Üçyüz", "Dörtyüz", "Beşyüz", "Altıyüz", "Yediyüz", "Sekizyüz", "Dokuzyüz"]
binler = ["", "bin", "İkibin", "Üçbin", "Dörtbin", "Beşbin", "Altıbin", "Yedibin", "Sekizbin", "Dokuzbin"]

sayi = input("4 basamaklı bir sayı giriniz : ")

print(binler[int(sayi[0])], yuzler[int(sayi[1])], onlar[int(sayi[2])], birler[int(sayi[3])])
"""
