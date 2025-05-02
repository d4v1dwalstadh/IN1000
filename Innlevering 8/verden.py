from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self.rader = rader
        self.kolonner = kolonner
        self._rutenett = Rutenett(rader, kolonner)
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()
        self._generasjonsnummer = 0

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print(f"Generasjonsnummer: {self._generasjonsnummer}, Antall levenede celler: {self._rutenett.antall_levende()}")

    def oppdatering(self):
        for celle in self._rutenett.hent_alle_celler():
            celle.tell_levende_naboer()

        for celle in self._rutenett.hent_alle_celler():
            celle.oppdater_status()
        
        self._generasjonsnummer += 1
            
    