# my_dict = {
#     "health": 100,
#     "speed": 20,
#     "weight": 48,
#     "name": "Mario"
# }

# print(my_dict.get("health"))


#97 - betdagi amaliyot
#1 - mashq
# otam = {
#     "t_yil": 1979,
#     "ism": "Akram",
#     "yosh": 2025-1979,
#     "t_joy": "Shaxrisabz"
# }

# ukam = {
#     "t_yil": 2010,
#     "ism": "Elnur",
#     "yosh": 2025-2010,
#     "t_joy": "Qarshi Shahri"
# }


# for key in otam:
#     print(f"{key}: {otam[key]}")


# #2 - mashq
# sevimli_taomlar = {
#     "milliy_taom": "osh",
#     "hamirli_taom": "manti",
#     "suyuq_taom": "sho'rva",
#     "nonushta": "tuxum"
# }


# print(sevimli_taomlar["milliy_taom"])
# print(sevimli_taomlar["nonushta"])
# print(sevimli_taomlar["hamirli_taom"])




# #3 - mashq
# python_atamalar = {
#     "if": "shart operatori",
#     "print()": "konsilga chiqarish operatori",
#     "input()": "foydalanuvchidan ma'lumot olish",
#     "int()": "integer data turiga o'tkazadi.",
#     "float()": "float data turiga o'tkazadi.",
#     "str()": "string data turiga o'tkazadi.",
#     "bool()": "boolean data turiga o'tkazadi.",
#     "for": "bir nechta iteratsiyalarni bajaradi"
# }

# lugat = input("lug'at kiriting: ")
# if python_atamalar.get(lugat):
#     print(python_atamalar[lugat])
# else:
#     print("Bunday lug'at yuq")



#--------------------------------------------------------
#104-betdagi amaliyot
#1-mashq
# python_atamalar = {
#     "if": "shart operatori",
#     "print()": "konsilga chiqarish operatori",
#     "input()": "foydalanuvchidan ma'lumot olish",
#     "int()": "integer data turiga o'tkazadi.",
#     "float()": "float data turiga o'tkazadi.",
#     "str()": "string data turiga o'tkazadi.",
#     "bool()": "boolean data turiga o'tkazadi.",
#     "for": "bir nechta iteratsiyalarni bajaradi",
#     "def": "funksiya yaratish mumkin.",
#     "while": "shart True bo'lsa ichidagi buyruqlarni bajaraveradi"
# }

# for key, value in sorted(python_atamalar.items()):
#     print(f"{key}: {value}")


# #2-mashq
# davlatlar_poytaxti = {
#     "Uzbekistan": "Tashkent",
#     "Kazakistan": "Astana",
#     "America": "Washinton",
#     "Russia": "Moscov",
#     "France": "Paris",
#     "Great Britian": "London",
#     "Turkiya": "Instanbul",
#     "Tajikistan": "Dushanbe",
#     "Kirgizistan": "Beshkek"
# }

# for key in sorted(davlatlar_poytaxti):
#     print(key)

# print("\n")
# for value in sorted(davlatlar_poytaxti.values()):
#     print(value)


#3-mashq

# qiymat = input("Davlatni kiriting: ")
# print(davlatlar_poytaxti.get(qiymat, "Bunday davlat yo'q"))


#4-mashq

# taomlar = {
#     "Osh": 25_000,
#     "Somsa": 2_000,
#     "Lag'mon": 13_000,
#     "Manti": 3_000,
#     "Hot Dog": 10_000,
#     "Lavash": 27_000,
#     "Chuchvara": 16_000,
#     "Gamburger": 35_000,
#     "Perashki": 1_500,
#     "Shorva": 20_000
# }

# buyirtmalar_royxati = []
# for i in range(3):
#     buyirtma = input(f"{i+1}-buyirmani kiriting: ")
#     buyirtmalar_royxati.append(buyirtma)

# for buyirtma in buyirtmalar_royxati:
#     if taomlar.get(buyirtma):
#         print(f"{buyirtma}ning narxi {taomlar[buyirtma]} so'm")
#     else:
#         print(f"bizda {buyirtma} taomi yuq")