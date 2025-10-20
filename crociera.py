from passeggero import Passeggero
from cabina import Cabina, Cabina_animali, Cabina_tipo
import csv
from operator import attrgetter

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.passeggeri=[]
        self.cabine=[]

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f"nome:{self._nome}"

    def __repr__(self):
        return f"{type(self).__name__}, nome={self._nome}"

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for riga in reader:
                    codice = riga[0]

                    # CABINE
                    if codice.startswith("CAB"):
                        if len(riga) == 4:
                            # Cabina standard
                            cabina = Cabina(riga[0], riga[1], riga[2], riga[3])
                        elif len(riga) == 5:
                            extra = riga[4]
                            if extra.isdigit():
                                cabina = Cabina_animali(riga[0], riga[1], riga[2], riga[3], extra)
                            else:
                                cabina = Cabina_tipo(riga[0], riga[1], riga[2], riga[3], extra)
                        self.cabine.append(cabina)

                    # PASSEGGERI
                    elif codice.startswith("P"):
                        passeggero = Passeggero(riga[0], riga[1], riga[2])
                        self.passeggeri.append(passeggero)

        except FileNotFoundError:
            raise FileNotFoundError("File non trovato.")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        cabina_trovata = None
        for cabina in self.cabine:
            if cabina.codice_cabina == codice_cabina:
                cabina_trovata = cabina
                break
        if cabina_trovata is None:
            raise ValueError(f"Nessuna cabina trovata con codice {codice_cabina}")

        passeggero_trovato= None
        for passeggero in self.passeggeri:
            if passeggero.codice_passeggero == codice_passeggero:
                passeggero_trovato = passeggero
                break
        if passeggero_trovato is None:
            raise ValueError (f"Nessun passeggero trovato con codice {codice_passeggero}")
        # Assegna la cabina al passeggero
        passeggero_trovato.cabina = cabina_trovata

        #  segna la cabina come occupata
        cabina_trovata.disponibile = False


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self.cabine, key=lambda c: c.prezzo_finale())


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passeggero in self.passeggeri:
            print(passeggero)
