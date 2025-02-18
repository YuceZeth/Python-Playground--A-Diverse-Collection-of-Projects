koltuks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    print(koltuks)
    sorgu_sigara = int(input("Sigara içiyor musunuz? : "))
    if sorgu_sigara == 1:
        koltuk_no = int(input("Koltuk numarası giriniz : "))
        if 10 >= koltuk_no >= 5:
            print("koltuk numarası 1-5 arası mq")
        else:
            sayac = 0
            for i in range(0, 5):
                if koltuks[i] == 1:
                    sayac = sayac + 1
            if sayac == 5:
                print("bütün koltukları dolu sigara içilmeyen yerden alıcan mı :")
                secim = input("(E/H) : ")
                secimm = secim.upper()
                if secimm == "E":
                    koltuk_no = int(input("Koltuk numarası giriniz : "))
                    if 10 >= koltuk_no >= 5:
                        print("koltuk numarası 5-10 arası mq")
                    else:
                        if koltuks[koltuk_no] == 1:
                            print("koltuk dolu...")
                        else:
                            koltuks[koltuk_no] = 1
                elif secimm == "H":
                    print("uçuş 3 saat sonra...")

            if koltuks[koltuk_no] == 1:
                print("koltuk dolu...")
            else:
                koltuks[koltuk_no] = 1
    elif sorgu_sigara == 2:
        koltuk_no = int(input("Koltuk numarası giriniz : "))
        if 10 >= koltuk_no >= 5:
            sayac = 0
            for i in range(5, 10):
                if koltuks[i] == 1:
                    sayac = sayac + 1
            if sayac == 5:
                print("bütün koltukları dolu sigara içilen yerden alıcan mı :")
                secim = input("(E/H) : ")
                secimm = secim.upper()
                if secimm == "E":
                    koltuk_no = int(input("Koltuk numarası giriniz : "))
                    if 5 >= koltuk_no >= 0:
                        if koltuks[koltuk_no] == 1:
                            print("koltuk dolu...")
                        else:
                            koltuks[koltuk_no] = 1
                    else:
                        print("koltuk numarası 5-10 arası mq")

                elif secimm == "H":
                    print("uçuş 3 saat sonra...")

            if koltuks[koltuk_no] == 1:
                print("koltuk dolu...")
            else:
                koltuks[koltuk_no] = 1
        else:
            print("koltuk numarası 5-10 arası mq")
    else:
        print("geçersiz işlem....")
        break
