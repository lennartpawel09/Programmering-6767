first_name = "Ada"
last_name = "Lovelace"

full_name = first_name + " " + last_name

print(full_name)

age = 16
print("Jag är" + " " + str(age) + " " + "år gammal")

# eller så skriver man

age = 16

text = f"Jag är {age}"
print(text)

# printa en bokstav i ett ord
ord = "Lennart"
ord2 = " Lennart "
print(ord[0])

print(ord[0:3])
print(ord[:2])
print(ord[2:])
print(ord2.strip())