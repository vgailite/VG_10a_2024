
import os
os.system('cls')
print("\n")
# 1.uzd

parole = input("ievadi paroli")
print(parole)

burti = parole.isupper()
skaitli = parole.isdigit()


if len(parole) < 9:
    print("parole nav pietiekami gara")
if burti != parole:
    print("nav lielo burtu")
elif burti == parole:
 print("ir lielie burti")
if skaitli != parole:
    print("nav ievadīti skaitļi parole") 
elif burti == parole:
   print("ir skaitli")

# 2.uzd

# import math
# year = int(input("ievadi gadu"))
# if year % 4!=0:
#    return False
# elif year % 100==0:
#    return year % 400 ==0:
# if is_leap_year(year):
#     print("Tas ir garais gads")
# else:
#     print("Tas ir īsais gads")
# if gads // 100:
#    print("gadssimts:")
# 3.uzd
vecums = int(input("Cik tev gadu?"))

if vecums < 7:
   print("Biļete bez maksas")
elif  vecums >= 7 and  vecums <18:
   print("Biļete maksā 5 eiro")
if vecums >=18 and vecums <65:
   print("Biļete maksā 10 eiro")
elif vecums >=65:
   print("Biļete maksā 3 eiro")

# 4.uzd
x = int(input("Ievadi skaitl:"))

if x<0:
   print("skaitlis ir negatīvs")
elif x==0:
   print("skaitlis ir nulle")
if x>0:
   print("skaitlis ir pozitīvs")

if x%2:
   print("skaitlis ir nepāra skaitlis")
else:
   print("Skaitlis ir pāra skaitlis")

#papildus uzdevums

result = 20 + 30 
result = 40 - 10 
result = 40 * 4  
result = 16 / 4  
result = 16 // 4 
result = 25 % 2  
result = 5 ** 3  