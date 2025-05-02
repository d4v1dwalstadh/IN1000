def poeng(streng):
    if streng == "lyn":
        return 0
    else:
        return len(streng)
    
def poengsum(strenger_list):
    sum = 0
    for streng in strenger_list:
        sum += poeng(streng)
    return sum

def velg(liste):
    heltall = int(input("Skriv inn heltall: "))
    while heltall >= len(liste):
        heltall = int(input("Skriv inn et lavere heltall: "))
    return liste[heltall]


kort1 = ["hjerte", "lyspære"]
kort2 = ["firklæver", "lyspære"]
kort3 = ["lyn", "lyn"]

kortliste = [kort1, kort2, kort3]

def spill_et_kort(kortlisten):
    return poengsum(velg(kortlisten))

print(spill_et_kort(kortliste))