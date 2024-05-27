class Müşteri:
    """
    Müşteri sınıfı, müşterilerin temel bilgilerini ve türlerini tutar.
    """

    def __init__(self, isim, müşteri_türü):
        """
        Müşteri sınıfının yapıcı metodu. İsim ve müşteri türü bilgilerini alır.
        """
        self.isim = isim
        self.müşteri_türü = müşteri_türü

    def müşteri_bilgisi(self):
        """
        Müşteri bilgilerini döndürür.
        """
        return f"İsim: {self.isim}, Müşteri Türü: {self.müşteri_türü}"

class NormalMüşteri(Müşteri):
    """
    Normal müşteri türü için Müşteri sınıfından türetilmiş alt sınıf.
    """

    def __init__(self, isim):
        """
        NormalMüşteri sınıfının yapıcı metodu. Üst sınıftan miras alınan yapıcı metodu çağırır.
        """
        super().__init__(isim, "Normal")

class SilverMüşteri(Müşteri):
    """
    Silver müşteri türü için Müşteri sınıfından türetilmiş alt sınıf.
    """

    def __init__(self, isim):
        """
        SilverMüşteri sınıfının yapıcı metodu. Üst sınıftan miras alınan yapıcı metodu çağırır.
        """
        super().__init__(isim, "Silver")

class GoldMüşteri(Müşteri):
    """
    Gold müşteri türü için Müşteri sınıfından türetilmiş alt sınıf.
    """

    def __init__(self, isim):
        """
        GoldMüşteri sınıfının yapıcı metodu. Üst sınıftan miras alınan yapıcı metodu çağırır.
        """
        super().__init__(isim, "Gold")

class PlatinumMüşteri(Müşteri):
    """
    Platinum müşteri türü için Müşteri sınıfından türetilmiş alt sınıf.
    """

    def __init__(self, isim):
        """
        PlatinumMüşteri sınıfının yapıcı metodu. Üst sınıftan miras alınan yapıcı metodu çağırır.
        """
        super().__init__(isim, "Platinum")
