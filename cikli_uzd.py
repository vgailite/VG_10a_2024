import os
os.system('cls')
print("\n")

#1.uzd

# for n in range(1,10000):
#     summa = 0
#     for i in range(1,n):
#         if n % i ==0:
#             summa = summa + i
#     if summa == n:
#         print(f"{n} ir perfekts skaitlis")

#2.uzd 

n = int(input("ievadi skaitli: "))
rinda = 1
while rinda < n:
    for i in range(1, rinda):
        print(i)
    rinda += 1
