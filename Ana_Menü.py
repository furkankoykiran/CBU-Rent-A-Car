from Araçlar import ArabaKiralama, MotorsikletKiralama, KaravanKiralama
from Müşteriler import NormalMüşteri, SilverMüşteri, GoldMüşteri, PlatinumMüşteri

def GetValidInput(x, y, message):
    while True:
        value = input(message)
        print()
        if value.isdigit() and int(value) >= x and int(value) <= y:
            return int(value)
        else:
            print(f"Lütfen {x} ile {y} arasında bir değer girin.\n")

class AnaMenü:
    """
    Ana menü sınıfı, araç kiralama sisteminin ana menü işlevlerini içerir.
    """

    def __init__(self):
        """
        AnaMenü sınıfının yapıcı metodu. Başlangıç araç ve müşteri listelerini oluşturur.
        """
        self.arabalar = [
            ArabaKiralama("Toyota", "Corolla", 5),
            ArabaKiralama("Honda", "Civic", 7)
        ]
        self.motorsikletler = [
            MotorsikletKiralama("Yamaha", "MT-07", 6),
            MotorsikletKiralama("Kawasaki", "Ninja 400", 7)
        ]
        self.karavanlar = [
            KaravanKiralama("Mercedes", "Sprinter", 9),
            KaravanKiralama("Ford", "Transit", 3)
        ]
        self.müşteriler = []

    def araç_kirala(self):
        """
        Araç kiralama işlemini gerçekleştirir.
        """
        print("1. Araba Kirala")
        print("2. Motorsiklet Kirala")
        print("3. Karavan Kirala")
        seçim = GetValidInput(1, 3, "Seçiminizi yapın: ")

        if seçim == 1:
            self.aracı_kirala(self.arabalar)
        elif seçim == 2:
            self.aracı_kirala(self.motorsikletler)
        elif seçim == 3:
            self.aracı_kirala(self.karavanlar)

    def aracı_kirala(self, araç_listesi):
        """
        Belirli bir araç listesinden araç kiralama işlemini gerçekleştirir.
        """
        for i, araç in enumerate(araç_listesi):
            print(f"{i+1}. {araç.araç_bilgisi()}")
        seçim = GetValidInput(1, len(araç_listesi), "Kiralamak istediğiniz aracı seçin: ")
        araç = araç_listesi[seçim - 1]
        
        print("1. Günlük Kirala")
        print("2. Saatlik Kirala")
        print("3. Haftalık Kirala")
        print("4. Aylık Kirala")
        kiralama_tipi = GetValidInput(1, 4, "Kiralama tipi seçin: ")
        miktar = int(input("Kaç adet kiralamak istiyorsunuz?: "))
        müşteri_isim = input("Müşteri ismi: ")

        # Müşteri kontrolü
        müşteri = next((m for m in self.müşteriler if m.isim == müşteri_isim), None)
        if not müşteri:
            print("Müşteri bulunamadı. Lütfen önce müşteri ekleyin.\n")
            return

        if kiralama_tipi == 1:
            print(araç.günlük_kirala(miktar, müşteri))
        elif kiralama_tipi == 2:
            print(araç.saatlik_kirala(miktar, müşteri))
        elif kiralama_tipi == 3:
            print(araç.haftalık_kirala(miktar, müşteri))
        elif kiralama_tipi == 4:
            print(araç.aylık_kirala(miktar, müşteri))

    def araç_ekle(self):
        """
        Yeni araç ekleme işlemini gerçekleştirir.
        """
        print("1. Araba Ekle")
        print("2. Motorsiklet Ekle")
        print("3. Karavan Ekle")
        seçim = GetValidInput(1, 3, "Seçiminizi yapın: ")

        marka = input("Marka: ")
        model = input("Model: ")
        adet = int(input("Adet: "))

        if seçim == 1:
            self.arabalar.append(ArabaKiralama(marka, model, adet))
        elif seçim == 2:
            self.motorsikletler.append(MotorsikletKiralama(marka, model, adet))
        elif seçim == 3:
            self.karavanlar.append(KaravanKiralama(marka, model, adet))

        print(f"{marka} {model} başarıyla eklendi.\n")

    def müşteri_ekle(self):
        """
        Yeni müşteri ekleme işlemini gerçekleştirir.
        """
        isim = input("İsim: ")
        print("1. Normal Müşteri")
        print("2. Silver Müşteri")
        print("3. Gold Müşteri")
        print("4. Platinum Müşteri")
        seçim = GetValidInput(1, 4, "Seçiminizi yapın: ")

        if seçim == 1:
            self.müşteriler.append(NormalMüşteri(isim))
        elif seçim == 2:
            self.müşteriler.append(SilverMüşteri(isim))
        elif seçim == 3:
            self.müşteriler.append(GoldMüşteri(isim))
        elif seçim == 4:
            self.müşteriler.append(PlatinumMüşteri(isim))

        print(f"{isim} başarıyla eklendi.\n")

    def araç_stok_görüntüle(self):
        """
        Araçların anlık stok bilgilerini görüntüler.
        """
        print("Arabalar:")
        for araba in self.arabalar:
            print(araba.araç_bilgisi(), "Stok:", araba.anlık_stok_görüntüle())

        print("Motorsikletler:")
        for motorsiklet in self.motorsikletler:
            print(motorsiklet.araç_bilgisi(), "Stok:", motorsiklet.anlık_stok_görüntüle())

        print("Karavanlar:")
        for karavan in self.karavanlar:
            print(karavan.araç_bilgisi(), "Stok:", karavan.anlık_stok_görüntüle())

    def kritik_stok_görüntüle(self):
        """
        Araçların kritik stok bilgilerini görüntüler.
        """
        print("Arabalar:")
        for araba in self.arabalar:
            print(araba.araç_bilgisi(), araba.kritik_stok_görüntüle())

        print("Motorsikletler:")
        for motorsiklet in self.motorsikletler:
            print(motorsiklet.araç_bilgisi(), motorsiklet.kritik_stok_görüntüle())

        print("Karavanlar:")
        for karavan in self.karavanlar:
            print(karavan.araç_bilgisi(), karavan.kritik_stok_görüntüle())

        print()

    def araç_geri_al(self):
        """
        Kiralanan araçların geri alım işlemini gerçekleştirir.
        """
        print("1. Araba Geri Al")
        print("2. Motorsiklet Geri Al")
        print("3. Karavan Geri Al")
        seçim = GetValidInput(1, 3, "Seçiminizi yapın: ")

        if seçim == 1:
            araç_listesi = self.arabalar
        elif seçim == 2:
            araç_listesi = self.motorsikletler
        elif seçim == 3:
            araç_listesi = self.karavanlar
        
        for i, araç in enumerate(araç_listesi):
            print(f"{i+1}. {araç.araç_bilgisi()}")
        araç_seçim = GetValidInput(1, len(araç_listesi), "Hangi aracı geri almak istiyorsunuz: ") - 1

        self.kiralama_kayıtları_görüntüle(araç_listesi)
        kiralama_seçim = GetValidInput(1, len(araç_listesi[araç_seçim].kiralama_kayıtları), "Hangi kiralamayı sonlandırmak istiyorsunuz: ") - 1

        print(araç_listesi[araç_seçim].geri_dön(kiralama_seçim))

    def kiralama_kayıtları_görüntüle(self, araç_listesi):
        """
        Belirli bir araç listesinden kiralama kayıtlarını görüntüler.
        """
        for i, araç in enumerate(araç_listesi):
            araç.kiralama_kayıtları_görüntüle()

    def ana_menu(self):
        """
        Ana menüyü gösterir ve kullanıcıdan işlem seçmesini ister.
        """
        while True:
            print(f"""    1. Araç Kirala
    2. Araç Ekle
    3. Müşteri Ekle
    4. Araç Stok Görüntüle
    5. Kritik Stok Görüntüle
    6. Araç Geri Al
    7. Kiralama Kayıtlarını Görüntüle
    8. Çıkış""")
            seçim = GetValidInput(1, 8, "Seçiminizi yapın: ")

            if seçim == 1:
                self.araç_kirala()
            elif seçim == 2:
                self.araç_ekle()
            elif seçim == 3:
                self.müşteri_ekle()
            elif seçim == 4:
                self.araç_stok_görüntüle()
            elif seçim == 5:
                self.kritik_stok_görüntüle()
            elif seçim == 6:
                self.araç_geri_al()
            elif seçim == 7:
                self.kiralama_kayıtları_görüntüle(self.arabalar + self.motorsikletler + self.karavanlar)
            elif seçim == 8:
                print("Çıkış yapılıyor...")
                break

if __name__ == "__main__":
    ana_menü = AnaMenü()
    ana_menü.ana_menu()
