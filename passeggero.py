class Passeggero:
    def __init__(self, codice_passeggero, nome, cognome):
        self.codice_passeggero = codice_passeggero
        self.nome = nome
        self.cognome = cognome
        self.cabina= None  # inizializzo il fatto che la cabina sia assegnata a None

    def __str__(self):
        if self.cabina:
            cabina_info= f" cabina={self.cabina.codice_cabina}"
        else:
            cabina_info= ""
        return f"{self.codice_passeggero} {self.nome} {self.cognome} {cabina_info}"

    def __repr__(self):
        return f"{type(self).__name__}, codice={self.codice_passeggero} nome={self.nome}, cognome= {self.cognome}"
