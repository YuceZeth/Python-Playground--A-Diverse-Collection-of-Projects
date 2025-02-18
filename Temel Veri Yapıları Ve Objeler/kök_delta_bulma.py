print("ax^2+bx+c a , b ve c yi giriniz")

a = int(input("a değeri: "))
b = int(input("b değeri: "))
c = int(input("c değeri: "))

delta = b**2 - 4*a*c
kök1 = (-b + delta ** 0.5) / (2 * a)
kök2 = (-b - delta ** 0.5) / (2 * a)

if (delta<0):
    print("reel kök yok, delta 0 dan küçük delta değeriniz: ",delta)
else:
    print("Delta değeri",delta)
    print("kökleri {} , {}".format(kök1,kök2))



