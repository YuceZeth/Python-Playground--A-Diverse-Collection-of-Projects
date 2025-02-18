import m_kafi

m_kafi.Tablo_Admin()
m_kafi.Tablo_Baklava()
m_kafi.Tablo_Musteri()
m_kafi.Tablo_Siparis()
m_kafi.Tablo_Sepet()

while True:
    print("Kullanıcı Girişi İçin 1\nAdmin Girişi İçin 2\nÇıkmak için 0")
    secim = int(input("Seçim : "))
    if secim == 1:
        print("Yeni Üye Kayıdı 1\nÜye Girişi 2\n")
        secim = int(input("Seçim : "))
        if secim == 1:
            m_id = int(input("Muşteri ID : "))
            m_email = input("Email : ")
            m_sifre = input("Şifre : ")
            m_adres = input("Adres : ")
            if m_kafi.M_Veri_Ekle(m_id, m_email, m_sifre, m_adres):
                print("Kayıt Tamamlandı...")
            else:
                print("ID Tekrarsız Olmalı...")
        elif secim == 2:
            m_id = int(input("Id : "))
            sifre = input("Şifre : ")
            if m_kafi.M_Kontrol(m_id, sifre):
                print("""

                    Kafî-Baklava'ya HOŞGELDİNİZ!!!

                """)
                while True:
                    m_kafi.B_Goster_M()
                    secim_ad = input("Ürün İsmi Giriniz : ")
                    secim_kilo = int(input("Kilo : "))
                    sncp = m_kafi.M_Siparis(secim_ad, secim_kilo)
                    if sncp == 1:
                        print("Ürün Sepete Eklendi...")
                        m_kafi.S_Veri_Ekle(secim_ad, secim_kilo)
                        print("Alışverişe Devam Etmek İster misiniz? (E/H) : ")
                        secim = input("Secim : ")
                        if secim == 'E':
                            continue
                        elif secim == 'H':
                            m_kafi.SSepet()
                            print("Kredi Kartı 1\nKapıda Ödeme 2")
                            secim = int(input("Ödeme Yöntemi Seçiniz : "))
                            if secim == 1:
                                kn = input("Kredi Kartı : ")
                                t = input("Son Kullanma Tarihi : ")
                                cvc = input("CVC : ")
                                print("İşlem Yapılıyor...")
                                print("Siparişiniz {} Adresinize Ulaştırılmak Üzere Yola Çıktı. "
                                      .format(m_kafi.Teslimat(id)))
                                m_kafi.S_Sifirla()
                                break
                            elif secim == 2:
                                print("Siparişiniz {} Adresinize Ulaştırılmak Üzere Yola Çıktı. "
                                      .format(m_kafi.Teslimat(id)))
                                m_kafi.S_Sifirla()
                                break
                        else:
                            print("Geçersiz İşlem.")
                    elif sncp == 2:
                        print("Üründen Yeteri Kadar Bulunmamaktadır.")
                    elif sncp == 3:
                        print("Ürün Mevcut Değil.")
            else:
                print("Email Veya Şifre Yanlış...")
        else:
            print("Geçersiz İşlem...")
    elif secim == 2:
        k_adi = input("Kullanıcı Adı : ")
        k_sifre = input("Şifre : ")
        if m_kafi.A_Kontrol(k_adi, k_sifre):
            print("Giriş Başarılı\n")
            while True:
                print("""
                Ürün Ekleme     1
                Ürün Sil        2
                Ürün Güncelle   3
                Çıkmak için     0
                """)
                secim = int(input("Seçim : "))
                if secim == 1:
                    b_id = int(input("Baklava ID : "))
                    b_ad = input("Baklava Adı : ")
                    b_kilo = int(input("Baklava Kilo : "))
                    b_bilgi = input("Baklava Bilgi : ")
                    b_fiyat = input("Baklava Fiyat : ")
                    if m_kafi.B_Veri_Ekle(b_id, b_ad, b_kilo, b_bilgi, b_fiyat):
                        print("İşlem Gerçekleşti.")
                    else:
                        print("ID Tekrarsız Olmalı...\n")
                elif secim == 2:
                    m_kafi.B_Goster()
                    b_id = int(input("Silinecek Ürünün ID'sini Giriniz : "))
                    if m_kafi.B_Veri_Sil(b_id):
                        print("İşlem Gerçekleşti.\n")
                    else:
                        print("Ürün Mevcut Değil!!!\n")
                elif secim == 3:
                    m_kafi.B_Goster()
                    ID = input("Değiştirilecek Verinin ID'sini Giriniz : ")
                    secim = input("Değiştirilecek Olan Özelliği Giriniz : ")
                    if secim == 'fiyat' or secim == 'kilo':
                        yveri = int(input("Yeni Veri : "))
                        if m_kafi.B_Veri_Guncelle(secim, ID, yveri):
                            print("İşlem Gerçekleşti.\n")
                        else:
                            print("Hata!")
                    else:
                        yveri = input("Yeni Veri : ")
                        if m_kafi.B_Veri_Guncelle(secim, ID, yveri):
                            print("İşlem Gerçekleşti.\n")
                        else:
                            print("Hata!\n")
                elif secim == 0:
                    break
                else:
                    print("Geçersiz İşlem...")
        else:
            print("Kullanıcı Adı Veya Şifre Yanlış!!!\n")
    elif secim == 0:
        break
    else:
        print("Geçersiz İşlem...\n")
