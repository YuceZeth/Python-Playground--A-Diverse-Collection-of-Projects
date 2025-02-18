print("***********\nHOŞGELDİNİZ\n***********")

kıtalar = ["Kuzey Amerika", "Avrupa", "Asya"]
print("\n", kıtalar)

while True:
    kıta_secim = input("\nKıta Seçiniz: ")

    if (kıta_secim == "Kuzey Amerika"):
        ülkeler1 = ("Amerika Birleşik Devletleri", "Meksika")
        print("\n", ülkeler1)
        while True:
            ülkeler1_secim = input("\nÜlke Seçiniz: ")
            if (ülkeler1_secim == "Amerika Birleşik Devletleri"):
                eyaletler1 = ("Florida", "Washington")
                print("\n", eyaletler1)
                while True:
                    eyaletler1_secim = input("\nEyalet Seçiniz: ")
                    if (eyaletler1_secim == "Florida"):
                        sehirler1 = ("Miami", "Orlando")
                        print("\n", sehirler1)
                        while True:
                            sehirler1_secim = input("\nŞehir Seçiniz: ")
                            if (sehirler1_secim == "Miami"):

                                anne_is = ["Doktor", "Öğretmen"]
                                print("\n", anne_is)
                                anne_is_secim = input("Anne İşini Seçiniz: ")
                                baba_is = ["Polis", "Doktor"]
                                print("\n", baba_is)
                                baba_is_secim = input("Baba İşini Seçiniz: ")
                                gelir = 0
                                harclık = 0

                                if (anne_is_secim == "Doktor" and baba_is_secim == "Doktor"):
                                    gelir = 50000
                                    harclık = 1000
                                    print("Günlük Harçlık = 1000 $\n Gün Geçirmek İçin 'q' Basınız ")




                                elif (anne_is_secim == "Doktor" and baba_is_secim == "Polis"):
                                    gelir = 30000
                                    harclık = 750
                                    print("Günlük Harçlık = 750$\n Gün Geçirmek İçin 'q' Basınız ")


                                elif (anne_is_secim == "Öğretmen" and baba_is_secim == "Polis"):
                                    gelir == 10000
                                    harclık = 250
                                    print("Günlük Harçlık = 250$\n Gün Geçirmek İçin 'q' Basınız")


                                elif (anne_is_secim == "Öğretmen" and baba_is_secim == "Doktor"):
                                    gelir = 20000
                                    harclık = 500
                                    print("Günlük Harçlık 500$\n Gün Geçirmek İçin 'q' Basınız")















                            elif (sehirler1_secim == "Orlando"):
                                anne_is = ["Doktor", "Öğretmen"]
                                print("\n", anne_is)
                                anne_is_secim = input("Anne İşini Seçiniz: ")
                                baba_is = ["Polis", "Doktor"]
                                print("\n", baba_is)
                                baba_is_secim = input("Baba İşini Seçiniz: ")







                            else:
                                print("Geçersiz İşlem...")











                    elif (eyaletler1_secim == "Washington"):
                        sehirler2 = ("Seattle", "Spokane")
                        print("\n", sehirler2)
                        sehirler2_secim = input("\nŞehir Seçiniz: ")
                    else:
                        print("\nGeçersiz İşlem...")































            elif (ülkeler1_secim == "Meksika"):
                eyaletler2 = ("Sinaloa", "Oaxaca")
                print("\n", eyaletler2)
                while True:
                    eyaletler2_secim = input("\nEyalet Seçiniz: ")
                    if (eyaletler2_secim == "Sinaloa"):
                        sehirler1 = ("Mazatlan", "Los Mıchis")
                        print("\n", sehirler1)
                        sehirler1_secim = input("\nŞehir Seçiniz: ")
                    elif (eyaletler2_secim == "Oaxaca"):
                        sehirler2 = ("Santo Domingo", "Monte Alban")
                        print("\n", sehirler2)
                        sehirler2_secim = input("\nSehir Seçiniz: ")
                    else:
                        print("\nGeçersiz İşlem...")

            else:
                print("\nGeçersiz İşlem...")













    elif (kıta_secim == "Avrupa"):
        ülkeler2 = ("İngiltere", "İtalya")
        print("\n", ülkeler2)
        while True:
            ülkeler2_secim = input("\nÜlke Seçiniz: ")
            if (ülkeler2_secim == "İngiltere"):
                sehirler1 = ("Londra", "Manchester")
                print("\n", sehirler1)
                sehirler1_secim = input("\nŞehir Seçiniz: ")
            elif (ülkeler2_secim == "İtalya"):
                sehirler2 = ("Roma", "Floransa")
                print("\n", sehirler2)
                sehirler2_secim = input("\nŞehir Seçiniz: ")
            else:
                print("\nGeçersiz İşlem...")



    elif (kıta_secim == "Asya"):
        ülkeler3 = ("Çin", "Türkiye")
        print("\n", ülkeler3)
        while True:
            ülkeler3_secim = input("\nÜlke Seçiniz: ")
            if (ülkeler3_secim == "Çin"):
                sehirler3 = ("Pekin", "Vuhan")
                print("\n", sehirler3)
                sehirler3_secim = input("\nŞehir Seçiniz: ")
            elif (ülkeler3_secim == "Türkiye"):
                sehirler4 = ("İstanbul", "İzmir")
                print("\n", sehirler4)
                sehirler4_secim = input("\nŞehir Seçiniz: ")
            else:
                print("\nGeçersiz İşlem...")


    else:
        print("\nGeçersiz İşlem...")
