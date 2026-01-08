
# my_set = {"Elmurod", 20, "Salom"}
# print(my_set)

# my_list = [55, "salom", "salom", "salom", 2, 3, 4]
# my_set = set(my_list)
# print(my_set)

# ismlar = [ 
#     "Asilbek",
#     "Suhrob",
#     "Daminbek",
#     "Asilbek",
#     "Aziz",
#     "Suhrob",
#     "Aziz",
#     "Elmurod",
#     "Elmurod", 
#     "Ali",
#     "Elmurod"
# ]

# ismlar_lugati = {}
# for ism in ismlar:
#     if ismlar_lugati.get(ism):
#         ismlar_lugati[ism] += 1
#     else:  
#         ismlar_lugati[ism] = 1
# print(ismlar_lugati)




asarlar = {
    "G'afur g'ulom": ["shum bola"]
}

yozuvchi_nomi = input("Yozuvchini ismini kirtiting: ")

if asarlar.get(yozuvchi_nomi):
    asarlar[yozuvchi_nomi].append("Yana bitta qandaydir asar")
else:
    asar = input("yozuvchining asarini kiriting: ")
    asarlar[yozuvchi_nomi] = list([asar])


print(asarlar)



