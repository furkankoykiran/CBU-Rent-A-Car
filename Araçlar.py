class AraçKiralama:
    """
    Araç kiralama sisteminin ana sınıfı. Bu sınıf, araç kiralama işlemlerinin temel özelliklerini tanımlar.
    """

    def __init__(self, marka, model, adet):
        """
        AraçKiralama sınıfının yapıcı metodu. Marka, model ve adet bilgilerini alır.
        """
        self.__marka = marka
        self.__model = model
        self.__adet = adet
        self.kiralama_kayıtları = []

    def araç_bilgisi(self):
        """
        Aracın marka, model ve adet bilgilerini döndürür.
        """
        return f"Marka: {self.__marka}, Model: {self.__model}, Adet: {self.__adet}"

    def kirala(self, müşteri, süre, ücret):
        """
        Araç kiralama işlemi. Adet bir azaltılır ve kiralama kaydı eklenir.
        """
        if self.__adet > 0:
            self.__adet -= 1
            self.kiralama_kayıtları.append((müşteri, süre, ücret))
            return True
        else:
            return False

    def geri_dön(self, kayıt_index):
        """
        Kiralanan aracın geri dönüş işlemi. Adet bir artırılır ve kiralama kaydı silinir.
        """
        if 0 <= kayıt_index < len(self.kiralama_kayıtları):
            müşteri, süre, ücret = self.kiralama_kayıtları.pop(kayıt_index)
            self.__adet += 1
            return f"{müşteri.isim} adlı müşterinin kiralaması sonlandırıldı."
        return "Geçersiz kayıt indexi."

    def anlık_stok_görüntüle(self):
        """
        Araç stoğunu gösterir.
        """
        return self.__adet

    def kritik_stok_görüntüle(self):
        """
        Araç kritik stoğunu gösterir. Stok 25'in altına düştüğünde uyarı verir.
        """
        if self.__adet < 5:
            return f"Kritik stok: {self.__adet} adet kaldı."
        return f"Stok: {self.__adet} adet."

    def günlük_kirala(self, kiralanan_araç_sayısı, müşteri):
        """
        Günlük araç kiralama işlemi.
        """
        ücret = 100
        toplam_ücret = self.ücret_hesapla(ücret, kiralanan_araç_sayısı, müşteri)
        if self.__adet >= kiralanan_araç_sayısı:
            for _ in range(kiralanan_araç_sayısı):
                self.kirala(müşteri, "günlük", toplam_ücret)
            return f"{kiralanan_araç_sayısı} araç günlük kiralandı. Toplam ücret: {toplam_ücret} TL"
        else:
            return "Yeterli araç stoğu yok."

    def saatlik_kirala(self, kiralanan_araç_sayısı, müşteri):
        """
        Saatlik araç kiralama işlemi.
        """
        ücret = 15
        toplam_ücret = self.ücret_hesapla(ücret, kiralanan_araç_sayısı, müşteri)
        if self.__adet >= kiralanan_araç_sayısı:
            for _ in range(kiralanan_araç_sayısı):
                self.kirala(müşteri, "saatlik", toplam_ücret)
            return f"{kiralanan_araç_sayısı} araç saatlik kiralandı. Toplam ücret: {toplam_ücret} TL"
        else:
            return "Yeterli araç stoğu yok."

    def haftalık_kirala(self, kiralanan_araç_sayısı, müşteri):
        """
        Haftalık araç kiralama işlemi.
        """
        ücret = 500
        toplam_ücret = self.ücret_hesapla(ücret, kiralanan_araç_sayısı, müşteri)
        if self.__adet >= kiralanan_araç_sayısı:
            for _ in range(kiralanan_araç_sayısı):
                self.kirala(müşteri, "haftalık", toplam_ücret)
            return f"{kiralanan_araç_sayısı} araç haftalık kiralandı. Toplam ücret: {toplam_ücret} TL"
        else:
            return "Yeterli araç stoğu yok."

    def aylık_kirala(self, kiralanan_araç_sayısı, müşteri):
        """
        Aylık araç kiralama işlemi.
        """
        ücret = 1500
        toplam_ücret = self.ücret_hesapla(ücret, kiralanan_araç_sayısı, müşteri)
        if self.__adet >= kiralanan_araç_sayısı:
            for _ in range(kiralanan_araç_sayısı):
                self.kirala(müşteri, "aylık", toplam_ücret)
            return f"{kiralanan_araç_sayısı} araç aylık kiralandı. Toplam ücret: {toplam_ücret} TL"
        else:
            return "Yeterli araç stoğu yok."

    def ücret_hesapla(self, ücret, kiralanan_araç_sayısı, müşteri):
        """
        Kiralama ücretini hesaplar ve müşteri türüne göre indirim uygular.
        """
        toplam_ücret = ücret * kiralanan_araç_sayısı
        if müşteri.müşteri_türü == "Silver":
            toplam_ücret *= 0.95
        elif müşteri.müşteri_türü == "Gold":
            toplam_ücret *= 0.90
        elif müşteri.müşteri_türü == "Platinum":
            toplam_ücret *= 0.80
        return toplam_ücret

    def kiralama_kayıtları_görüntüle(self):
        """
        Kiralama kayıtlarını görüntüler.
        """
        for i, kayıt in enumerate(self.kiralama_kayıtları):
            müşteri, süre, ücret = kayıt
            print(f"{i+1}. Müşteri: {müşteri.isim}, Süre: {süre}, Ücret: {ücret} TL")

class ArabaKiralama(AraçKiralama):
    """
    Araba kiralama işlemleri için AraçKiralama sınıfından türetilmiş alt sınıf.
    """

    def __init__(self, marka, model, adet):
        """
        ArabaKiralama sınıfının yapıcı metodu. Üst sınıftan miras alınan yapıcı metodu çağırır.
        """
        super().__init__(marka, model, adet)

class MotorsikletKiralama(AraçKiralama):
    """
    Motorsiklet kiralama işlemleri için AraçKiralama sınıfından türetilmiş alt sınıf.
    """

    def __init__(self, marka, model, adet):
        """
        MotorsikletKiralama sınıfının yapıcı metodu. Üst sınıftan miras alınan yapıcı metodu çağırır.
        """
        super().__init__(marka, model, adet)

class KaravanKiralama(AraçKiralama):
    """
    Karavan kiralama işlemleri için AraçKiralama sınıfından türetilmiş alt sınıf.
    """

    def __init__(self, marka, model, adet):
        """
        KaravanKiralama sınıfının yapıcı metodu. Üst sınıftan miras alınan yapıcı metodu çağırır.
        """
        super().__init__(marka, model, adet)
