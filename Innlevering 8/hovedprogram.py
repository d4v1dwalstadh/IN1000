from verden import Verden

def hovedprogram():
    rader = int(input("Oppgi antall rader: "))
    kolonnen = int(input("Oppgi antall kolonner: "))
    verden = Verden(rader, kolonnen)
    
    while True:
        verden.tegn()
        
        inp = input("Enter for å fortsette, q for å avslutte: ")
        if inp == "q":
            break
 
        verden.oppdatering()

        
        

# starte hovedprogrammet
hovedprogram()
