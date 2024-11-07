print('Sveiks, "labo skolēn"!')
print("hello, \"friend\"")
print("Viktorija", "Gailite", sep='?????')
name = input("Kā tevi sauc? ")

name = name.strip().title()

pirmais, otrais = name.split(" ")


print("Sveiks,", name)
print(f"Sveiks, {name}")