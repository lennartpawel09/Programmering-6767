import random
nummer = random.randint(1, 3)

svar = int(input("Gissa siffran 1-3"))

while svar != nummer:
    print("Fel, försök igen")
    svar = int(input("Gissa igen: "))

print("Du klarade det!")