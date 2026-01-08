#1-uyga vazifa
# Foydalanuvchi 10 ta butun son kiritsin.
# Faqat musbat sonlarni alohida listga yozing
# faqat manfiy 
# o'rtachasini chiqarish, musbat va manfiy o'rtacha.

# musbatlar = []
# manfiylar = []
# for i in range(10):
#     a = int(input("Soningizni kiriring: "))
#     if a > 0:
#         musbatlar.append(a)
#     elif a < 0:
#         manfiylar.append(a)

# summa = sum(musbatlar) + sum(manfiylar)
# jami_sonlar = len(musbatlar) + len(manfiylar)
# print(f"Hamma sonlarning o'rtachasi: {summa/jami_sonlar}")

#------------------------------------------------------------
    
# 1 dan 100 gacha bo'lgan sonlar orasidan 10 ga, 
# 5 va 3 ga bo'lganda qoldiq 2 ga teng bo'lgan
# sonlarni listga chiqariyla
# 3 ta alohida list.

# bolinadigan_10 = []
# bolinadigan_5 = []
# bolinadigan_3 = []

# for i in range(1, 101):
#     if i % 10 == 2:
#         bolinadigan_10.append(i)
#     elif i % 5 == 2:
#         bolinadigan_5.append(i)
#     elif i % 3 == 2:
#         bolinadigan_3.append(i)


# print(f"10 ga bo'lganda qoldiq 2 chiqadigan sonlar: {bolinadigan_10}")
# print("\n")
# print(f"5 ga bo'lganda qoldiq 2 chiqadigan sonlar: {bolinadigan_5}")
# print("\n")
# print(f"3 ga bo'lganda qoldiq 2 chiqadigan sonlar: {bolinadigan_3}")


#-----------------------------------------------------



numbers = "0123456789"
result = ""
level = ""
n = int(input())
count = 1
level_count = ""
for i in range(n):
    if count > 9:
        level = "1"
        count = 0
    result += level + numbers[count]
    count += 1
    
print(result)


