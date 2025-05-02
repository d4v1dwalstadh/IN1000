"""
Programmet printer ut svar setning basert på brukers svar
på spørsmålet. 
"""

svar = str(input("Har du lyst på brus? "))  # streng variabel for brukers svar

if svar.lower() == "ja":  # sjekker bruker svar opp mot antatte svar
    print("Her har du en brus!")
elif svar.lower() == "nei":
    print("Den er grei.")
else:  # printer feilsetning om bruker skriver noe annet
    print("Det forstod jeg ikke helt.")