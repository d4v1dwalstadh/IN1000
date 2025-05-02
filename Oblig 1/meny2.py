"""
Programmet sjekker brukers svar opp mot en rekke valg på menyen. 
Her er menyen lagt i et objekt som gjør den fleksibel og lett å legge til flere alternativer.
Det printes så setninger basert på brukers kombinasjoner og valg.
"""

meny = {  # menyen er oppdelt for lettere sjekk av de oppgitte kombiansjonene
    "hovedretter": {
         "animalsk": ["biff", "torsk"],
         "veggis": ["salat", "tomatsuppe"]
    },
    "tilbehør": {
        "grønnsaker": ["gulrøtter", "brokkoli"],
        "sauser": ["bernaise", "peppersaus"]
    }
}

print("Menyen")
for key, value in meny.items():
    print(f'{key}: {value}')


hovedrett = str(input("Velg hovedrett "))  # streng variabler for brukers valg av retter
tilbehør = str(input("Velg tilbehør "))


if hovedrett in meny["hovedretter"]["animalsk"] and tilbehør in meny["tilbehør"]["sauser"]:  # sjekker om valg er animalsk med saus
    print("Du må spise mere grønnsaker")
elif hovedrett in meny["hovedretter"]["veggis"] and tilbehør in meny["tilbehør"]["grønnsaker"]:  # sjekker om valg er helt veggis
    print("Du har valgt et vegetarmåltid")
elif hovedrett in meny["hovedretter"]["animalsk"] and tilbehør in meny["tilbehør"]["grønnsaker"] or hovedrett in meny["hovedretter"]["veggis"] and tilbehør in meny["tilbehør"]["sauser"]:
    print(f'Du har valgt {hovedrett} med {tilbehør}')  # her er valget en kombinasjonen og valgte retter blir skrevet ut
else:  # hvis ingen av mulighetene over går igjennom så har bruker valgt noe utenfor menyen og får dermed feilmelding
    print("Du har valgt noe utenfor menyen")