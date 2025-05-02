"""
Programmet sjekker brukers svar opp mot en rekke valg på menyen. Her er menyen hard kodet.
Det printes så setninger basert på brukers kombinasjoner og valg.
"""

print("Hovedretter: biff, torsk, salat \nTilbehør: gulrøtter, bernaise")

hovedrett = str(input("Velg en hovedrett "))  # streng variabler for brukers valg
tilbehør = str(input("Velg en tilbehør "))

if hovedrett.lower() == "biff" or hovedrett.lower() == "torsk":  # sjekker om animalske retter er valgt, og opp mot gitte kombinasjoner
    if tilbehør.lower() == "gulrøtter":
        print(f'Du har valgt {hovedrett} med {tilbehør}')
    elif tilbehør.lower() == "bernaise":
        print("Du spiser ikke nok grønnsaker!")
    else:  # feilsetning dersom andre retter er valgt
        print("Du har valgt tilbehør som ikke er på menyen")
        
elif hovedrett.lower() == "salat":  # sjekker på samme måte opp mot veggisrettene
    if tilbehør.lower() == "gulrøtter":
        print("Du har valgt et vegetarmåltid")
    elif tilbehør.lower() == "bernaise":
        print(f'Du har valgt {hovedrett} med {tilbehør}')
    else: 
        print("Du har valgt tilbehør som ikke er på menyen")
        
else:  # feilsetning dersom bruker velger en eller to ting som ikker er på meny
    print("Du har valgt hovedrett som ikke er på menyen", end=" ")
    if tilbehør.lower() != "gulrøtter" or tilbehør.lower() != "bernaise":
        print("og du har heller ikke valgt tilbehør på menyen")
