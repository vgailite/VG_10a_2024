import os
os.system("cls")
print("\n")

# 1.uzd
tekstins = input("ievadi tekstu(vismaz 5 simbolus):")
izvade = tekstins[-5:]
print(izvade)

# 2.uzd
x = int(input("Ievadi skaitli:"))

n = range(x, x+20)
for x in n:
    if not x%3:
        continue
    print(x)

# 3.uzd

x = int(input("Ievadi skaitli"))

n = [
    x,
    x-1,
    x-2,
    x-3,
    x-4,
    x-5,
    x-6,
    x-7,
    x-8,
    x-9,
    x-10,
]
for i in n:
    print(i)

# 4.uzd

dict = {"Annija": 20, "Kristers": 22, "Alekss": 19, "Artūrs": 16, "Markuss": 22, "Ērika": 26}
x = input("Ievadiet kādu vārdu: Annija, Kristers, Alekss, Artūrs, Markuss vai Ērika: ")
print(dict.get (x))

# 5.uzd
import time
import sys


laiks = int(input("Ievadiet lejupskaitīšanas laiku sekundēs: "))
while laiks > 0:
    minutes = laiks // 60 
    sekundes = laiks % 60 
    sys.stdout.write(f"\r{minutes:02}:{sekundes:02}")
    sys.stdout.flush()
    time.sleep(1)
    laiks -= 1
sys.stdout.write("\r Kontroldarbs beidzies! \n")

