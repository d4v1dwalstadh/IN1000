# from film import Film
from filmklubb import Filmklubb

def testprogram():
    # __init__
    # Opprett Filmklubb-objekt
    print("oppretter Filmklubb-objekt")
    filmklubb1 = Filmklubb()

    # les_filmer_fra_fil
    # Les inn filmer fra filen filmer.txt
    print("Leser filmer fra fil")
    filmklubb1.les_filmer_fra_fil("filmer.txt")
    print()

    # skriv_ut_alle_filmer
    # Skriv ut all info om alle filmer, sjekk at alt er lest fra fil
    filmklubb1.skriv_ut_alle_filmer()
    print()

    # registrer_film
    print("Registrerer ny film")
    # Legg inn en ny film med tittel og produksjonsår som leses fra terminal
    filmklubb1.registrer_film()
    print()
    # Skriv ut all info om alle filmer og sjekk at ny film ble registrert
    filmklubb1.skriv_ut_alle_filmer()
    print()
    
    # Hvis _eq_ er implementert i Film og testes i registrer_film:
    print("Prøver å registrere film som allerede finnes")
    filmklubb1.registrer_film()
    print()    


    # finn_film_tittel
    print("Leter etter film med (start på) usannsynlig tittel")
    # Kall på metoden med et argument som ingen titler starter med
    # Bruk print eller assert for å sjekke at resultatet er som forventet
    print(filmklubb1.finn_film_tittel("lgf"))
    print()

    print("Leter etter film med (start på) tittel 'Hidden '")
    # Kall på metoden med argument "Hidden "
    # Bruk print eller assert for å sjekke at resultatet er som forventet
    funnet = filmklubb1.finn_film_tittel("Hidden ")
    print(funnet.hent_tittel())
    print()

    # legg_til_skuespillere
    print("Legg til skuespillere for en film" )
    # kall metoden på film-objektet du fikk returnert fra finn_film_tittel
    # (navn og rolle for to skuespillere du velger selv leses fra terminal)
    filmklubb1.legg_til_skuespillere(funnet.tittel)
    print()
    # SKriv ut all info om alle filmer og sjekk at resultatet er som forventet
    filmklubb1.skriv_ut_alle_filmer()
    print()

    # finn_film_periode
    # Kall på metoden med argumentene etter=2000 og før=2024
    print("Leter ett filmer produsert etter 2000 og før 2024:")
    # Skriv ut titlene på filmer som returneres (bruk hent_tittel).
    # Kontroller at resultatene er som forventet
    for movie in (filmklubb1.finn_filmer_periode(2000, 2024)):
        print(movie.hent_tittel())
    print()

    # Kall på finn_film_periode med argumentene etter=2020 og før=2020
    print("Leter etter filmer produsert etter 2020 og før 2020:")
    # Kontroller at resultatet er som forventet (tom liste) med assert (evt skriv ut)
    print(filmklubb1.finn_filmer_periode(2020, 2020))


    # SKriv ut all info om alle filmer og sjekk at resultatet er som forventet
    filmklubb1.skriv_ut_alle_filmer()

testprogram()