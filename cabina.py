class Cabina:
    def __init__(self, codice_cabina, nletti, ponte, prezzo):
        self.codice_cabina = codice_cabina
        self.nletti = int(nletti)
        self.ponte = ponte
        self.prezzo = float(prezzo)
        self.disponibile= True  # True se non assegnata

    def prezzo_finale(self):
        return self.prezzo  # le cabine standard non hanno sovrapprezzo

    def __lt__(self, other):  # per ordinamento per prezzo
        return self.prezzo_finale() < other.prezzo_finale()

    def __str__(self):
        return f"{self.codice_cabina} {self.nletti} {self.ponte} {self.prezzo_finale()} {self.disponibile}"

    def __repr__(self):
        return (f"{type(self).__name__} codicecabina={self.codice_cabina}, nletti={self.nletti}, ponte={self.ponte}, "
                f"prezzo={self.prezzo_finale()}, disponibile={self.disponibile})")

class Cabina_animali(Cabina):
    def __init__(self, codice_cabina, nletti, ponte, prezzo, nanimali):
        # inizializza gli attributi della classe madre
        super().__init__(codice_cabina, nletti, ponte, prezzo)
        # aggiungi l’attributo specifico della classe figlia
        self.nanimali = int(nanimali)

    def prezzo_finale(self):
        # +10% per ogni animale ammesso
        return self.prezzo * (1 + 0.10 * self.nanimali)

    def __str__(self):
        # riutilizzo __str__ della madre e aggiungo info in più
        return super().__str__() + f" {self.nanimali}"
    def __repr__(self):
        return super().__repr__() + f" nanimali={self.nanimali}"

class Cabina_tipo(Cabina):
    def __init__(self, codice_cabina, nletti, ponte, prezzo,tipo):
        super().__init__(codice_cabina, nletti, ponte, prezzo)
        self.tipo = tipo

    def prezzo_finale(self):
        return self.prezzo * 1.20 # +20%

    def __str__(self):
        return super().__str__() + f" {self.tipo}"
    def __repr__(self):
        return super().__repr__() + f" tipo={self.tipo}"