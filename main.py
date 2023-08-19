class Kalkulacka:
    """
    Nejprve nastavuje pocatecni hodnoty parametru cislo1 a cislo2 na nulu
    """

    cislo1 = None
    cislo2 = None

    def soucet (self):
        """
        Vezme dve cisla cislo1 a cislo2 a provede jejich soucet
        """
        return self.cislo1 + self.cislo2
    
    def rozdil(self):
        """
        Vezme dve cisla cislo1 a cislo2 a provede jejich rozdil
        """
        return self.cislo1 - self.cislo2
    
    def soucin(self):
        """
        Vezme dve cisla cislo1 a cislo2 a provede jejich soucet
        """
        return self.cislo1 * self.cislo2
    
    def podil(self):
        """
        Vezme dve cisla cislo1 a cislo2 a provede jejich podil
        """
        return self.cislo1 / self.cislo2
    
    print ("Hello Worl")
    print ("druhy test")
