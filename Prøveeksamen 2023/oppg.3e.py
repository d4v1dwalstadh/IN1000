def frekvensanalyse(liste):
    tell_element = {}
    for element in liste:
        if element not in tell_element:
            tell_element[element] = 0
        tell_element[element] += 1
    for element in tell_element:
        print("Antall", element, ":", tell_element[element])


ord = ["F", "E", "R", "S", "K", "E", "N", "B", "R", "U", "S"]
setning = ["Flodhest", "er", "best", "ingen", "protest"]


frekvensanalyse(ord)
frekvensanalyse(setning)