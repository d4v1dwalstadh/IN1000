"""
Programmet skriver ut beskjeder basert på bruker navn.
I tillegg gjøres enkel regning basert på faste tall.
"""

print("Hei Student!")

navn = str(input("Skriv ditt navn "))  # streng variabel for navnet bruker oppgir
print("Hei", navn)

tall1 = 3
tall2 = 5
print(f'{tall1} \n{tall2}')  # printer oppgitte tall der \n lager linjeskifte

diff = tall1 - tall2
print("Diffferanse:", diff) 

navn2 = str(input("Skriv nytt navn "))
sammen = navn + navn2  # legger sammen to strenger, variablene kommer etter hverandre
print(sammen)
sammen = navn + " og " + navn2  # endrer variablen, legger på "og" mellom navnene
print(sammen)
