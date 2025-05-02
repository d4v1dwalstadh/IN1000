from film import Film

def test_film():
    # __init__
    # Opprett to film-objekter med tittel og produksjonsår du velger selv
    print("Oppretter to filmer")
    film1 = Film("Spiderman", 2020)
    film2 = Film("Kaptein Sabeltann", 2006)
    
    # hent_tittel
    # Skriv ut tittel på de to filmene
    print("Skriver ut titler på to filmer")
    print(film1.hent_tittel())
    print(film2.hent_tittel())
    print()

    # ny_skuespiller
    # Legg til to skuespillere og deres roller for en av filmene, skriv ut alt om filmen
    print("Legger til to skuespillere")
    film1.ny_skuespiller("Tom Holland", "Peter Parker")
    film1.ny_skuespiller("Zendaya", "Michelle Jones-Watson")
    film1.skriv_ut_film()
    print()

    # Prøv å legge inn en av skuespillerne igjen, med en ny rolle, og sjekk at rollen ikke blir endret
    print("Tester ulovlig innlegging av skuespiller")
    film1.ny_skuespiller("Tom Holland", "Batman")

    # skriv_ut_film
    # Skriv ut all informasjon om begge filmer du har lagt inn
    print("Skriver ut all info om to filmer:")
    film1.skriv_ut_film()
    film2.skriv_ut_film()
    print()

    # hent_alle_skuespiller_navn
    # Skriv ut skuespillernes navn for den filmen som har to
    print("Henter og skriver ut alle skuespillernavn for en film:")
    print(film1.hent_skuespiller_navn())

    # sjekk_periode
    # Sjekk om en film du har lagt inn er i en periode du velger
    # (velg periode som skal gi True og sjekk at dette blir resultatet)
    print ("Sjekker at en film er i oppgitt periode")
    print(film1.sjekk_periode(2004, 2024))

    # Sjekk om en film er i en periode som skal gi False
    # (velg samme årstall til begge argumenter og sjekk resultat er False)
    print ("Sjekker at en film ikke kan være produsert før og etter samme år")
    print(film1.sjekk_periode(2021, 2021))

    # sjekk_tittel
    # Sjekk om en film har en tittel som starter på en streng som du selv velger
    print ("Sjekker om starten på en films tittel kjennes igjen")
    print(film1.sjekk_tittel("Spidermans"))

    
    # __str__
    # Skriv ut film-objekt med print
    print("Skriver ut en film med print (test av __str__)")
    print(film1)
    print()

    
    # test __eq__ (frivillig)
    print ("tester __eq__ med to ulike filmer:")
    print(film1 == film2)
    print("\nTester __eq__ med to like filmer:")
    print(film1 == Film("Spiderman", 2020))


test_film()

  