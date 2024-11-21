import os
os.system('cls')
print("\n")

x= int(input("Kāds ir x?"))
y = int(input("Kāds ir y?"))

if x != y:
    print("x nav vienāds ar y")
else:
    print("x ir vienāds ar y")

punkti= int(input("Punkti:"))

if punkti >= 90 and punkti <= 100:
    print("Vērtejums: 10")
elif punkti >= 80 and punkti < 90:
    print("Vērtejums: 9")
elif punkti >= 70 and punkti < 80:
    print("Vērtejums: 8")
elif punkti >= 60 and punkti < 70:
    print("Vērtejums: 7")
else:
    print("Vērtējums: n/v")


import math

a = int(input("koeficents a:"))
b = int(input("koeficents b:"))
c = int(input("koeficents c:"))

D = b**2-4*a*c
print(D)
if D < 0:
    print("Sakņu nav")
elif D == 0:
    print("Viena sakne")
else:
    print("Divas saknes")
