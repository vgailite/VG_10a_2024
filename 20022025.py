import os
os.system("cls")
print("\n")

f = open("bakstitajs.txt", "a", encoding="utf-8")
f.write("Žirafei ir garš kakls")
f.close()

with open("bakstitajs.txt", "w", encoding="utf-8") as ieraksts:
    ieraksts.write("Pīlknābis dzīvo Austrālijā")
