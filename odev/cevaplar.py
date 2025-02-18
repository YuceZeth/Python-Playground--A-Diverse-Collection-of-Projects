"""
Problem 1
s1 = int(input("Birinci Sayıyı Giriniz: "))
s2 = int(input("İkinci Sayıyı Giriniz: "))
s3= int(input("Üçüncü Sayıyı Giriniz: "))
carpım = s1 * s2 * s3
print("Sayıların Çarpımı {}".format(carpım))
"""

"""
#Problem 2
kg = int(input("Kilonuz (Kilogram Cinsinden): "))
boy = float(input("Boyunuz (Metre Cinsinden): "))
ındex = (kg / (boy*boy))
print("Vücut Kitle İndeksiniz: ",ındex)
"""

"""
#Problem 3
a = int(input("1 km'de kaç litre benzin yakıyor: "))
b = int(input("kaç km gittiniz: "))
odenek = (a*b)*7
print("krdsm öde: ",odenek)
"""

"""
#Problem 4
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
numra = input("Numaranız: ")
bilgileriniz = [ad,soyad,numra]
print("Bilgileriniz.... \n Adınız: {}\n Soyadınız: {}\n Numaranız: {}\n".format(bilgileriniz[0],bilgileriniz[1],bilgileriniz[2]))
"""
"""
#Problem 5 
a = input(" birinci sayıyı gir: ")
b = input("ikinci sayıyı gir: ")
a,b = b,a
print("qandırdım za birinci: {} , ikinci: {}".format(a,b))
"""

"""
a = int(input("birinci dik kenar: "))
b = int(input("ikinci dik kenar: "))
hıpo = (a**2+b**2) **0.5
print("hipotenüs: ",hıpo)
"""

"""
boy = float(input("Boyunuz (Metre Cinsinden): "))
kilo = int(input("Kilonuz (Kilogram Cinsinden): "))
vki = kilo / boy**2
if (vki<18.5):
    print("Zayıf")
elif (vki>18.5 and vki<25):
    print("Normal")
elif (vki>25 and vki<30):
    print("Fazla Kilolu")
else:
    print("obez")
"""

"""
vize1 = int(input("Birinci Vizeyi Giriniz: "))
vize2 = int(input("İkinci Vizeyi Giriniz: "))
final = int(input("Finali Giriniz: "))
ort = ((vize1*(3/10))+(vize2*(3/10))+(final*(2/5)))
if (ort>=90):
    print("AA")
elif (ort>=85):
    print("BA")
elif (ort>=80):
    print("BB")
elif (ort>=75):
    print("CB")
elif (ort>=70):
    print("CC")
elif (ort>=65):
    print("CD")
elif (ort>=60):
    print("DC")
elif (ort>=55):
    print("DD")
elif (ort<55):
    print("FF KALDIN AQ")
"""

"""
a = input("Üçgen'mi Dörtgen'mi ?: ")
if(a == 'Dörtgen'):
    dk1 =int(input("Birinci Kenarı Giriniz: "))
    dk2 = int(input("İkinci Kenarı Giriniz: "))
    dk3 = int(input("Üçüncü Kenarı Giriniz: "))
    dk4 = int(input("Dörtüncü Kenarı Giriniz: "))
    if (dk1==dk2 and dk1==dk3 and dk1==dk4):
        print("Kare")
    elif (dk1 == dk3 and dk2 == dk4):
        print("Dikdörtgen")
    else:
        print("Sıradan Bir Dörtgen")
elif (a == 'Üçgen'):
    uk1 = int(input("Birinci Kenarı Giriniz: "))
    uk2 = int(input("İkinci Kenarı Giriniz: "))
    uk3 = int(input("Üçüncü Kenarı Giriniz: "))
    ucgenbelirtme = uk1+uk3>uk2>abs(uk1-uk3)
    if(ucgenbelirtme == False):
        print("Üçgen Belirtmiyor")
    elif(uk1==uk2 and uk1==uk3):
        print("Eşkenar")
    elif(uk1==uk2 or uk1==uk3 or uk2==uk3 ):
        print("İkizkenar")
    else:
        print("Sıradan Bir Üçgen")
else:
    print("Üçgen Veya Dörtgen Girmediniz...")
"""

"""
sayı = int(input("Sayı: "))
toplam = 0

for i in range(1,sayı):
    if(sayı%i==0):
        toplam = toplam + i


if (sayı==toplam):
    print("Müko")
else:
    print("Not Müko")

"""

"""
sayı = int(input("Sayı: "))
toplam = 0

for i in range(1,sayı):
    if(sayı%i==0):
        toplam = toplam + i
if (sayı==toplam):
    print("Müko")
else:
    print("Not Müko")
"""

"""
for i in range(1,101):
    if (i % 3 == 0):
        print(i)
"""

"""
toplam = 0
while True:
    sayı = input("Sayı: ")
    if (sayı == "q"):
        break
    sayı = int(sayı)
    toplam += sayı
print("giriğiniz  sayıların toplamı",toplam)
"""

"""
for i in range(1,11):
    print("************")
    for j in range(1,11):
        print("{} * {} = {} ".format(i,j,i*j))
"""

"""
liste = [x for x in range(1,101) if x % 2 == 0]
print(liste)
"""

"""
def muko(sayı):
    toplama = 0
    for i in range(1,sayı):
        if (sayı % i == 0):
            toplama += i
    if(sayı == toplama):
        print("Mükemmel Sayı: ",toplama)
for i in range(1,1001):
    muko(i)
"""

"""
def ekok(sayı1,sayı2):
    for i in range(1,1001):
        if(i % sayı1 == 0 and i % sayı2 == 0):
            print("Ekokları: ",i)
            break
sayı1 = int(input("Sayı1: "))
sayı2 = int(input("Sayı2: "))
ekok(sayı1,sayı2)
"""

"""
def ebob(sayı1, sayı2):
    i = 2
    ebob = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ebob *= i
            sayı1 //= i
            sayı2 //= i
        else:
            break
    return ebob
sayı1 = int(input("Sayı1: "))
sayı2 = int(input("Sayı2: "))
print("Ebob:", ebob(sayı1, sayı2))
"""
"""
liste = ["345","sadas","324a","14","kemal"]

for i in liste:
    try:
        if(int(i) != str):
            print(i)
    except ValueError:
        pass
"""





























