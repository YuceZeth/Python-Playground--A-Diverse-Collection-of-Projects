import random

r = int(input("Radius : "))
while True:
    coordinates = []
    while True:
        x = random.randint(-r, r)
        y = random.randint(-r, r)

        if x ** 2 + y ** 2 == r ** 2:
            coordinates.append([x, y])
        else:
            continue

        if len(coordinates) == 3:
            break

    xs = []
    ys = []
    for i in range(len(coordinates)):
        z = coordinates[i]
        for j in range(len(z)):
            if j == 0:
                xs.append((z[j] ** 2))
            else:
                ys.append((z[j] ** 2))

    m1 = ((xs[0] ** 2 - xs[1] ** 2) ** 2) + ((ys[0] ** 2 - ys[1] ** 2) ** 2)
    m2 = ((xs[0] ** 2 - xs[2] ** 2) ** 2) + ((ys[0] ** 2 - ys[2] ** 2) ** 2)
    m3 = ((xs[1] ** 2 - xs[2] ** 2) ** 2) + ((ys[1] ** 2 - ys[2] ** 2) ** 2)

    if abs(m1 + m3) > m2 > abs(m1 - m2):
        print("Coordinates Denoting A Triangle : ", coordinates)
        break
    else:
        continue

