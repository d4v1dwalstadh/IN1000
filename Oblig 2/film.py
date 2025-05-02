class Film:
    def __init__(self, tittel, år):
        """Konstruktør som initialiserer et Film-objekt med tittel og produksjonsår."""
        self.tittel = tittel
        self.år = år
        self.skuespillere = {}  # Ordbok for å lagre skuespillere (navn: rolle)

    def hent_tittel(self):
        """Returnerer filmens tittel."""
        return self.tittel

    def ny_skuespiller(self, navn, rolle):
        """Legger til skuespiller og rolle, feilmelding hvis du allerede finnes."""
        if navn in self.skuespillere:
            print(f"Feil: {navn} er allerede lagt til med rollen {self.skuespillere[navn]}.")
        else:
            self.skuespillere[navn] = rolle

    def hent_skuespiller_navn(self):
        """Returnerer liste over skuespillernes navn i filmen."""
        return list(self.skuespillere.keys())
    
    def skriv_ut_film(self):
        """Skriver ut all info om filmen i terminal."""
        print(f'{self.tittel}({self.år}). Medvirkende:')
        for navn, rolle in self.skuespillere.items():
            print(f'{ navn} som {rolle}')

    def sjekk_periode(self, år_1, år_2):
        """Returnerer True hvis filmen er produsert mellom år_1 og år_2."""
        return år_1 < self.år < år_2

    def sjekk_tittel(self, tittel_start):
        """Returnerer True hvis tittel_start samsvarer med starten av filmens tittel og ikke er lengre."""
        return self.tittel.startswith(tittel_start)

    def __str__(self):
        """Returnerer en streng med informasjon om filmen."""
        skuespiller_str = ", ".join([f"{navn} som {rolle}" for navn, rolle in self.skuespillere.items()])
        return f"{self.tittel}({self.år}). Medvirkende: {skuespiller_str}"

    def __eq__(self, annen_film):
            """Sammenligner to Film-objekter basert på tittel og år."""
            if not isinstance(annen_film, Film):
                return False  # Hvis annen_film ikke er et Film-objekt
            return self.tittel.lower() == annen_film.tittel.lower() and self.år == annen_film.år
        

