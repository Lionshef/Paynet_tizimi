from datetime import time
# a = "Sardor" #3
# b = "aeuio"
# x = 0
# for i in a:
#     if i in b:
#         x = x+1
#
# print(f"{a} soida {x} ta unli xarf bor {len(a)-x} undosh harflar soni")

data = time()
a = input("Telefon raqamni kiriting:")
b = input("Pul miqdorini kiriting:")
p = int(b)
k = p/100*1
k1 = p-k
if a[0] == "+":
    if a[1:4] and len(a) == 13 and a[1:12]==int():
        print(f"Nomeringi togri pul tushdi \n"
              f"Chekingi ni tekshiring:"
              f"Vaqt:{data}"
              f"Pul miqdori:{k1}")
    else:
        print(False)
else:
    print(False)

