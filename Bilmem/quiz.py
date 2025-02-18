import m_quiz

m_quiz.Tablo_Admin()
m_quiz.Tablo_Sepet()
m_quiz.Tablo_Kullanici()
m_quiz.Tablo_Menu()
m_quiz.Tablo_Teslimat()
m_quiz.Admin_Ekle()

while True:
    print("Admin Girişi İçin 1\nMüşteri Girişi İçin 2")
    secim = int(input("Seçim : "))
    if secim == 1:
        a_adi = input("Kullanıcı Adı : ")
        a_sifre = input("Şifre : ")
        if m_quiz.A_Kontrol(a_adi, a_sifre):
            print("Giriş Başarılı\n")
            while True:
                print("""
                        Ürün Ekleme         1
                        Ürün Sil            2
                        Ürün Güncelle       3
                        Teslimat Görüntüle  4
                        Çıkmak için         0
                        """)
                secim = int(input("Seçim : "))
                if secim == 1:
                    y_id = int(input("Yemek ID : "))
                    y_ad = input("Yemek Adı : ")
                    y_fiyat = input("Yemek Fiyat : ")
                    y_bilgi = input("Yemek Bilgi : ")
                    if m_quiz.M_Veri_Ekle(y_id, y_ad, y_fiyat, y_bilgi):
                        print("İşlem Gerçekleşti.")
                    else:
                        print("ID Tekrarsız Olmalı...\n")
                elif secim == 2:
                    m_quiz.A_Goster()
                    y_id = int(input("Silinecek Ürünün ID'sini Giriniz : "))
                    if m_quiz.A_Veri_Sil(y_id):
                        print("İşlem Gerçekleşti.\n")
                    else:
                        print("Ürün Mevcut Değil!!!\n")
                elif secim == 3:
                    m_quiz.A_Goster()
                    ID = input("Değiştirilecek Verinin ID'sini Giriniz : ")
                    secim = input("Değiştirilecek Olan Özelliği Giriniz : ")
                    if secim == 'fiyat':
                        yveri = int(input("Yeni Veri : "))
                        if m_quiz.A_Veri_Guncelle(secim, ID, yveri):
                            print("İşlem Gerçekleşti.\n")
                        else:
                            print("Hata!")
                    else:
                        yveri = input("Yeni Veri : ")
                        if m_quiz.A_Veri_Guncelle(secim, ID, yveri):
                            print("İşlem Gerçekleşti.\n")
                        else:
                            print("Hata!\n")
                elif secim == 4:
                    m_quiz.K_Goster()
                    gk_telno = int(input("Teslimatı Gösterilecek Kişinin Telefon Numarası : "))
                    m_quiz.TTeslimat(gk_telno)
                elif secim == 0:
                    break
                else:
                    print("Geçersiz İşlem...")
        else:
            print("Kullanıcı Adı Veya Şifre Yanlış!!!\n")
    elif secim == 2:
        print("Yeni Üye Girişi 1\nÜye Girişi 2\n")
        secim = int(input("Seçim : "))
        if secim == 1:
            k_tel_no = int(input("Telefon No : "))
            k_sifre = input("Şifre : ")
            k_adres = input("Adres : ")
            if m_quiz.K_Veri_Ekle(k_tel_no, k_sifre, k_adres):
                print("Kayıt Tamamlandı...")
                print("""
                
                    HOŞGELDİNİZ!!!
                
                """)
                while True:
                    m_quiz.A_Goster()
                    u_ad = input("Ürün İsmi Giriniz : ")
                    u_Adet = int(input("Adet : "))
                    if m_quiz.M_Kontrol_Sepet(u_ad):
                        print("Ürün Sepete Eklendi...")
                        m_quiz.SSepet(u_ad, u_Adet)
                        print("Alışverişe Devam Etmek İster misiniz? (E/H) : ")
                        secim = input("Secim : ")
                        if secim == 'E':
                            continue
                        elif secim == 'H':
                            m_quiz.S_Goster()
                            print("Kredi Kartı 1\nKapıda Ödeme 2")
                            secim = int(input("Ödeme Yöntemi Seçiniz : "))
                            if secim == 1:
                                odeme_tipi = "Kredi Kartı"
                                kn = input("Kredi Kartı : ")
                                t = input("Son Kullanma Tarihi : ")
                                cvc = input("CVC : ")
                                print("İşlem Yapılıyor...")
                                m_quiz.T_Veri_Ekle(k_tel_no, odeme_tipi)
                                print("Sepet :\n")
                                m_quiz.TT_Goster(k_tel_no)
                                print("Siparişiniz Adresinize Ulaştırılmak Üzere Yola Çıktı.")
                                m_quiz.S_Sifirla()
                                break
                            elif secim == 2:
                                odeme_tipi = "Kapıda Ödeme"
                                m_quiz.T_Veri_Ekle(k_tel_no, odeme_tipi)
                                m_quiz.TT_Goster(k_tel_no)
                                print("Siparişiniz Adresinize Ulaştırılmak Üzere Yola Çıktı. ")
                                m_quiz.S_Sifirla()
                                break
                        else:
                            print("Geçersiz İşlem.")
                    else:
                        print("Ürün Mevcut Değil.")
                else:
                    print("Email Veya Şifre Yanlış...")
            else:
                print("ID Tekrarsız Olmalı...")
        elif secim == 2:
            k_tel_no = int(input("Telefon No : "))
            k_sifre = input("Şifre : ")
            if m_quiz.K_Kontrol(k_tel_no, k_sifre):
                print("""

                    HOŞGELDİNİZ!!!

                """)
                while True:
                    m_quiz.A_Goster()
                    u_ad = input("Ürün İsmi Giriniz : ")
                    u_Adet = int(input("Adet : "))
                    if m_quiz.M_Kontrol_Sepet(u_ad):
                        print("Ürün Sepete Eklendi...")
                        m_quiz.SSepet(u_ad, u_Adet)
                        print("Alışverişe Devam Etmek İster misiniz? (E/H) : ")
                        secim = input("Secim : ")
                        if secim == 'E':
                            continue
                        elif secim == 'H':
                            m_quiz.S_Goster()
                            print("Kredi Kartı 1\nKapıda Ödeme 2")
                            secim = int(input("Ödeme Yöntemi Seçiniz : "))
                            if secim == 1:
                                odeme_tipi = "Kredi Kartı"
                                kn = input("Kredi Kartı : ")
                                t = input("Son Kullanma Tarihi : ")
                                cvc = input("CVC : ")
                                print("İşlem Yapılıyor...")
                                m_quiz.T_Veri_Ekle(k_tel_no, odeme_tipi)
                                print("Sepet :\n")
                                m_quiz.TT_Goster(k_tel_no)
                                print("Siparişiniz Adresinize Ulaştırılmak Üzere Yola Çıktı.")
                                m_quiz.S_Sifirla()
                                break
                            elif secim == 2:
                                odeme_tipi = "Kapıda Ödeme"
                                m_quiz.T_Veri_Ekle(k_tel_no, odeme_tipi)
                                m_quiz.TT_Goster(k_tel_no)
                                print("Siparişiniz Adresinize Ulaştırılmak Üzere Yola Çıktı. ")
                                m_quiz.S_Sifirla()
                                break
                        else:
                            print("Geçersiz İşlem.")
                    else:
                        print("Ürün Mevcut Değil.")
            else:
                print("Email Veya Şifre Yanlış...")
        else:
            print("Geçersiz İşlem...")
    else:
        print("Geçersiz İşlem...")
