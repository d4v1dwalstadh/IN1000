from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()
        

    def _lag_tomt_rutenett(self):
        return [self._lag_tom_rad() for i in range(self._ant_rader)]  

    def _lag_tom_rad(self):
         return [None for i in range(self._ant_kolonner)]   
            
    def fyll_med_tilfeldige_celler(self):
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                celle = self.lag_celle(i, j)
                
                if randint(0, 2) == 1:
                    celle.sett_levende()

    def lag_celle(self, rad, kol):
        celle = self._rutenett[rad][kol] = Celle()
        return celle
        
    def hent_celle(self, rad, kol):
        if 0 <= rad < self._ant_rader and 0 <= kol < self._ant_kolonner: 
            return self._rutenett[rad][kol]
        return None

    def tegn_rutenett(self):
        # for i in range(10):
        #     print()
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                print(self._rutenett[i][j].hent_status_tegn(), end="")
            print()     # sørger for linjeskift
            
    def _sett_naboer(self, rad, kol):
           celle = self.hent_celle(rad, kol)
           
           if celle is None:
               return 
           
           nabo_posisjoner = [
            (-1, -1), (-1, 0), (-1, 1),  # Rad over
            (0, -1),          (0, 1),   # Samme rad
            (1, -1), (1, 0), (1, 1)     # Rad under
            ]   
           
           for d_rad, d_kol in nabo_posisjoner:
               nabo = self.hent_celle(rad + d_rad, kol + d_kol)  # Hent nabo
               if nabo is not None:  # Legg til kun gyldige celler
                    celle.legg_til_nabo(nabo)

    def koble_celler(self):
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                self._sett_naboer(i, j)                   

    def hent_alle_celler(self):
        return [celle for rad in self._rutenett for celle in rad]

    def antall_levende(self):
        return sum(1 for celle in self.hent_alle_celler() if celle.er_levende())
