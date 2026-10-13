import random

print("Hej", "Lelle")

# svar = input("Fråga? ")

# tal = int("12")
# sträng = str(3.14)

# randint är en funktion i modulen random
for slag in range(5):
    tärningsslag = random.randint(1,6)
    print(f"Du slog {tärningsslag}")

# Randrange väljer ett slumpmässigt tal från en range (typ)
udda_tal = random.randrange(5,100,25)
print(udda_tal)

antal_sexor = 0
antal_slag = 600
for _ in range(antal_slag):
    tärningsslag = random.randint(1,6)
    if tärningsslag==6:
        antal_sexor += 1
print(f"Antalet sexor var {antal_sexor}")