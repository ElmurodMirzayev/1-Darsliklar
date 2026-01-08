#1-uyga vazifa 
# bolinadigan_10 = []
# bolinadigan_5_3 = []
# for i in range(1, 100):

#     if i % 10 == 0:
#         bolinadigan_10.append(i)
#     elif i % 5 == 0 and i % 3 == 0:
#         bolinadigan_5_3.append(i)

# print(f"10 ga bo'linadigan sonlar: \n{bolinadigan_10}")
# print("\n")
# print(f"5 va 3 ga bo'linadigan sonlar: \n{bolinadigan_5_3}")

#---------------------------------------

#2-uyga vazifa
# musbat_sonlar = []
# for i in range(10):
#     son = int(input("Soningizni kiriting: "))
#     if son > 0:
#         musbat_sonlar.append(i)

# print(f"Musbat sonlar: {musbat_sonlar}")

#---------------------------------------


#3-uyga vazifa
# royxat = []
# n = int(input("n: "))
# for i in range(n):
#     son = int(input("Son kiriring: "))
#     royxat.append(son*2)

# print(royxat)

#---------------------------------------


#4-uyga vazifa
yigindi = 0
for i in range(7):
    son = float(input("Son: "))
    yigindi += son

ortacha = yigindi/7
print(f"ortacha: {ortacha}")

if ortacha < 60:
    print("Fail")
elif ortacha >= 65 and ortacha < 71:
    print("o'rtacha")
elif ortacha >= 71 and ortacha < 86:
    print("yaxshi")
elif ortacha >= 86:
    print("alo")


#--------------------------------------------



#5-uyga vazifa tuplesga misol
# a = (1, 2)
# b = ("Kordinata", "O'qlari")
# c = (2.002, 98.2, 34.88, 76.28)
# d = ("Hi", "Good morning", 20, 3.3)
# h = ((23, 75), (61, 99), (0, 88), (111, 73))
# j = tuple([999])

# a = a + (2,4)
# print(a)
#--------------------------------------------


#6-uyga vazifa Tuple bilan Listning farqi.
"""
Tuplening elementiga o'zgartirish kiritib bo'lmaydi.
Tuple bu immutable data turiga kiradi.

"""

#---------------------------------------------

#Sinfda yechilgan masalalar

# yosh = int(input("yoshingizni kiriting: "))

# if yosh <= 0:
#     print("To'g'ri yosh kiriting")

# elif yosh <= 7:
#     print("Sizga chipta bepul")

# elif yosh <= 18:
#     print("Sizga chipta 10 000 so'm ")

# elif yosh <= 65:
#     print("sizga chipta 20 000 so'm")

# elif yosh <= 100:
#     print("Sizga chipta bepul")

# else:
#     print("To'gri yoshni kiriting")


#------------------------------------

#ismlar = []
# for i in range(5):
#     ismlar.append(input("Ism kiriting: ").upper())
    

# print(ismlar)

#------------------------------------


# yosh = int(input("yoshingizni kiriting: "))

# if yosh <= 0:
#     print("To'g'ri yosh kiriting")

# elif yosh <= 7:
#     print("Sizga chipta bepul")

# elif yosh <= 18:
#     print("Sizga chipta 10 000 so'm ")

# elif yosh <= 65:
#     print("sizga chipta 20 000 so'm")

# elif yosh <= 100:
#     print("Sizga chipta bepul")

# else:
#     print("To'gri yoshni kiriting")


#---------------------------------------------


# i = int(input("Son kiriting: "))
# if i % 15 == 0:
#     print("FizzBuzz")
# elif i % 5 == 0:
#     print("Buzz")
# elif i % 3 == 0:
#     print("Fizz")

#---------------------------------------------


# toys = ("bear", "car")
# toys = list(toys) 


#63 - betdagi amaliyot bajarish.
# davlatlar = ["Amerika", "Rossiya", "Uzbekiston", "Koreya", "Germaniya", "Yaponiya", "Xitoy"]
# print(davlatlar)
# print("\n")
# print(f"Ro'yxatning uzunligi: {len(davlatlar)}")
# print("\n")
# print(f"Tartibga solish: {sorted(davlatlar)}")
# print("\n")
# print(f"Teskari tartibga solish: {sorted(davlatlar, reverse=True)}")
# print("\n")
# print(davlatlar)
# print("\n")
# davlatlar.reverse()
# print(davlatlar)
# print("\n")
# davlatlar.sort()
# print(davlatlar)
# print("\n")
# davlatlar.sort(reverse=True)
# print(davlatlar)
# print("\n")


# juft_sonlar = []
# for i in range(120, 1200):
#     if i % 2 == 0:
#         juft_sonlar.append(i)
    
# # Yig'indini hisoblash jarayoni
# yigindi = 0
# for i in juft_sonlar:
#     yigindi += i

# print(f"yig'indi: {yigindi}")

# # Eng katta va eng kichik sonning ayirmasi.
# print(f"Eng katta va eng kichik sonning ayirmasi: {max(juft_sonlar)-min(juft_sonlar)}")

# # Ro'yxatdagi elementlar sonini hisoblash.
# print(f"Ro'yxatdagi elementlar soni: {len(juft_sonlar)}")

# # Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni chiqarish.
# # Boshi uchun
# print(f"boshidagi 20 ta qiymat: {juft_sonlar[:20]}")
# print("\n")

# # O'rtasi uchun 
# orta_index = (len(juft_sonlar)-1)//2
# orta_elementlar = juft_sonlar[orta_index - 10 : orta_index + 10]
# print(f"o'rtasidagi 20 ta qiymat: {orta_elementlar}")
# print(len(orta_elementlar))
# print("\n")

# # Oxiri uchun
# oxirgi_index = len(juft_sonlar)
# oxirgi_elementlar = juft_sonlar[oxirgi_index-20:]
# print(f"oxirgi 20 ta: {oxirgi_elementlar}")
# print(len(oxirgi_elementlar))
# print("\n")



# #Taomlar ro'yxatini yaratish
# taomlar = ["Osh", "Chuchvara", "Sho'rva", "Shashlik", "Lag'mon"]
# nonushta = taomlar.copy()
# nonushta.remove("Osh")
# nonushta.remove("Sho'rva")
# nonushta.append("Tuxum")
# nonushta.append("Saryog'")

# print(taomlar)
# print(nonushta)

# nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"


# --------------------------------------------------

# 70 - Betdagi amaliyot
#1.
# ismlar = ["Sardor", "Damin", "Behruz", "Suhrob", "Samandar"]
# for ism in ismlar:
#     print(f"Salom {ism}")

# print(f"Kod {len(ismlar)} marta takrorlandi.")

#2.
# toq_sonlar = []
# for i in range(10, 1000):
#     if i % 2 == 1:
#         toq_sonlar.append(i)

# for toq_son in toq_sonlar:
#     print(toq_son**3)


#3
# sevimli_kinolar = []
# for i in range(5):
#     kino = input("Sevimli kino: ")
#     sevimli_kinolar.append(kino)

# print(f"Sevimli kinolar: {sevimli_kinolar}")


#4.
# n = int(input("Nechta odamlar bilan suhbatlashdingiz: "))
# odamlar = []
# for i in range(n):
#     odam = input(f"{i+1}-odamni ismni kiriting: ")
#     odamlar.append(odam)

# print(odamlar)


# musbatlar=[]

# for i in range(10):
#     butun_son = int(input(f"{i+1} - butun son kiriting: "))
#     if butun_son > 0:
#         musbatlar.append(butun_son)
    
#     musbatlar.append(i)
# print("musbat sonlar", musbatlar)