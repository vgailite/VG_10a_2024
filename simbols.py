#pirmais uzd
string = input("ievadi simbolu virkni: ")
print(f"simbolu virknes graums: {len(string)}")
#f formatē argumentu izdrukā tikai tekstu neieskaitot iekavas
# string ir mainīgais 
#len funkcijai nosaka garumu mainigajaa vertibai
#otrais uzdevums
divi = input(" ieraksti")
divi = divi.lower()
divi = divi.upper()
print(divi.lower()) 
print(divi.upper())
# otrais variants
print(f"virkne ar lielajiem: {string.upper()}")
print(f"virkne ar mazajiem: {string.lower()}")
# tresais uzdevums
symbol = input("ievadi simbolu,aizvietošanai")
print(f"aizvietottas atstarpes: {string.replace(' ' , symbol)}")
# replace metode aizvietot atstarpes obligati jaliek iekavas ko vajag aizvietot un ar ko jaaizvieto
#ceturtais udevums
word_to_check = " python"
print(f"vai virkne satur vārdu '{word_to_check}'? {'python'in string}")
# chekosana notiek taja in 
#piektais uzdevums

print(f"pirmie pieci: {string[:5]}")
print(f"pedejie tris simboli: {string[-3:]}")
# ar kvadratu iekavam izgriez 
#kols nosaka robežas

#sestais uzdevums

number =  float(input("ievadi skaistli:"))
print(f"skaitlis noapalots lidz diviem cipariem aiz komata:{round(number, 2)}")
#round noapalo lidz skaitlim kas ir atzimets aiz komata
#septitais uzd

integer = int(input("ievadi veselu skaitli: "))
print(f"skaitlis ka decimaldala: {float(integer)}")

# astotais uzd
large_number = int(input("evadi lierlu skaitli:"))
print(f"skaitlis:{large_number:,}".replace(''))

#devitais uzd
print(f"skailtis binaraja{bin(integer)[2:]}")
print(f"skailtis binaraja{oct(integer)[2:]}")
print(f"skailtis binaraja{hex(integer)[2:]}")

#desmitais
negative_number = int(input("ievadi negativu skaitli"))
print(f"absaluta vertiba:{abs(negative_number)}")