Length = int(input("Girilecek Sayı Miktarı : "))
Array = []
for i in range(0, Length):
    Number = int(input("Sayı : "))
    Array.append(Number)

Dividing = int(input("Bölen : "))

for i in range(0, Length):
    print(Array[i], "'nin", Dividing, "'e Bölünmesi : ", f"{Array[i] / Dividing:.4f}")


