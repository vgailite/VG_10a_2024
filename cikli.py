import os
os.system('cls')
print("\n")

# i = 0
# while i != 3:
#     print("Es esmu gudrs")
#     i = i + 1


import random

skaits_6 = 0
metienu_skaits = 0

while metienu_skaits < 50:
    metiens = random.randint(1, 6)
    if metiens == 6:
        skaits_6 += 1
    metienu_skaits += 1   

print(f"Sešinieks uzmests {skaits_6} reizes")    
