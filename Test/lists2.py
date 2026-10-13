lexikon = ["Micke", "Felix", "William", "Stella", "Jovan"]
lottorad = [12, 23, 2, 5, 34, 14, 9]

for ord in lexikon:
    print(ord)

print(lexikon[3])

for ord in lexikon[1:3]:
    print(ord)

# Strängar är oföränderliga (immutable)
namn = "Lelle"
namn + " Pawel" #ger en ny sträng, som vi måste stoppa in i en variabel om vi vill använda den
print(namn)
namn = namn + " Pawel"
print(namn)

#listor går att förändra (mutable)
lexikon.append("Edgar")
print("Nytt innehåll")
for ord in lexikon:
    print(ord)

# Bygga upp en lista
klassen = []
while True:
    namn = input("Ange ett namn (tomt avslutar): ")
    if namn=="":
        break
    klassen.append(namn)

for elev in klassen:
    print(f"{elev} är bäst")