""" https://github.com/MatBilML/Bilgisayar-Programlama-2-Python/blob/master/ara_imtihan_ornek.pdf """
""" *****SORU 1***** 
kenar1 = input("Birinci Kenar : ")
kenar2 = input("İkinci Kenar : ")
kenar3 = input("Üçüncü Kenar : ")
kenar4 = input("Dördüncü Kenar : ")

if kenar1 == kenar2 and kenar1 == kenar3 and kenar1 == kenar4:
    print("Kare")
elif kenar1 == kenar3 and kenar2 == kenar4:
    print("Dikdörtgen")
else:
    print("Yamuk")"""

""" *****SORU 2***** 
isim = input("İsim : ")
soyisim = input("Soyisim : ")
cinsiyet = input("Cinsiyet : ")
medeni_durum = input("Medeni Durum : ")

if medeni_durum == "Evli" or medeni_durum == "evli":
    e_isim = input("Eş İsim : ")
    e_soyisim = input("Eş Soyisim : ")
    e_cinsiyet = input("Eş Cinsiyet : ")
    e_medeni_durum = input("Eş Medeni Durum : ")
    print("İsim : {}\n Soyisim : {}\n Cinsiyet : {}\n Medeni Durum : {} ".format(isim,soyisim,cinsiyet,medeni_durum))
    print("Eş Bilgileri \n İsim : {}\n Soyisim : {}\n Cinsiyet : {}\n Medeni Durum : {} ".format(e_isim, e_soyisim, e_cinsiyet,e_medeni_durum))
else:
    print("İsim : {}\n Soyisim : {}\n Cinsiyet : {}\n Medeni Durum : {} ".format(isim,soyisim,cinsiyet,medeni_durum))"""

from functools import reduce
from operator import mul


def solve():
    """ Compute the answer to Project Euler's problem #8 """

    # Build a list of the individual digits as integer objects
    series = """
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450
    """
    series = series.replace(" ", "").replace("\n", "")
    integers = [int(character) for character in series]

    # Perform the search through all overlapping m-long subsets
    n = len(integers)
    m = 13
    answer = 0
    for i in range(n - m + 1):
        subset = integers[i:i+m]
        product = reduce(mul, subset, 1)
        answer = max(answer, product)
    return answer

solve()