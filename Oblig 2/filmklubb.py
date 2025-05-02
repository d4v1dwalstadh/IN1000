from film import Film

class Filmklubb:
    def __init__(self):
        """Konstruktør oppretter tom liste til filmer."""
        self.filmer = []

    def les_filmer_fra_fil(self, filnavn):
        """Åpner en fil, leser inn filmer, og legger dem til i filmer-listen."""
        with open(filnavn, "r", encoding="utf-8") as fil:
            for linje in fil:
                linje = linje.strip()  # Fjern linjeskift og mellomrom
                if linje:  # Hvis linjen ikke er tom
                    tittel, år = linje.split(";")
                    film = Film(tittel, int(år))  # Opprett Film-objekt
                    self.filmer.append(film)

    def skriv_ut_alle_filmer(self):
        """Skriver ut alle filmer i filmer-listen."""
        if not self.filmer:
            print("Ingen filmer i filmklubben.")
        else:
            for film in self.filmer:
                print(film)  # Bruker __str__ metoden fra Film

    def registrer_film(self):
        """Registrerer en ny film ved å be bruker om input fra terminalen."""
        tittel = input("Oppgi filmens tittel: ")
        try:
            år = int(input("Oppgi filmens produksjonsår (4 siffer): "))
        except ValueError:
            print("Ugyldig år. Vennligst oppgi et gyldig 4-sifret år.")
            return

        ny_film = Film(tittel, år)
        
        # Sjekk om filmen allerede finnes i klubben
        for film in self.filmer:
            if film == ny_film:  # Hvis __eq__ er implementert
                print("Filmen er allerede registrert i filmklubben.")
                return
        
        self.filmer.append(ny_film)
        print(f"Filmen '{tittel}' fra {år} er lagt til.")
    
    def finn_film_tittel(self, tittel):
        """Returnerer første filmen som matcher eller begynner med den angitte tittelen."""
        for film in self.filmer:
            if film.sjekk_tittel(tittel):  # Bruker sjekk_tittel fra Film-klassen
                return film
        return None

    def legg_til_skuespillere(self, din_film):
        """Legger til skuespillere til en film ved input fra terminalen."""
        for film in self.filmer:
            if din_film == film.tittel:
                while True:
                    navn = input("Oppgi skuespillers navn (eller trykk Enter for å avslutte): ")
                    if not navn:  # Brukeren trykker Enter for å avslutte
                        return
                    rolle = input(f"Oppgi rollen til {navn}: ")
                    film.ny_skuespiller(navn, rolle)  # Bruker metoden fra Film
                    
        print("Ugyldig filmobjekt.")    

    def finn_filmer_periode(self, år_1, år_2):
        """Returnerer en liste med filmer produsert mellom år_1 og år_2."""
        filmer_i_periode = [film for film in self.filmer if film.sjekk_periode(år_1, år_2)]
        return filmer_i_periode
