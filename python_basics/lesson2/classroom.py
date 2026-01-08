# yil = input("Nechanchi yilda to'g'ilgansiz: ")
# yosh = 2025 - int(yil)
# print(f"sizning yoshingiz {2025 - int(yil)}")
# print(f"siz 20 yildan keyin {yosh + 20} yoshga to'lasiz.")




# birinchi_son = float(input("Birinchi sonni kiriting: "))
# ikkinchi_son = float(input("ikkinchi sonni kiriting: "))

# print(f"ikki sonning yig'indisi: {birinchi_son + ikkinchi_son} ")
# print(f"ikki sonning ayirmasi: {birinchi_son - ikkinchi_son}")
# print(f"ikki sonning bo'linmasi: {birinchi_son // ikkinchi_son}")
# print(f"Qoldiqli bo'lganda: {birinchi_son % ikkinchi_son}")
# print(f"ikkisonning ko'paytmasi {birinchi_son * ikkinchi_son}")
# print(f"ikki sonning butunli bo'linmasi {birinchi_son / ikkinchi_son}")






aralash_list = [22, 0.23, "olma", True, [-3, -2, 3, 4, 5], False]

aralash_list.append(7)
print(f"listga bitta element qo'shildi: {aralash_list}")

aralash_list.remove("olma")
print(f"listdan element olib tahslandi: {aralash_list}")

aralash_list.insert(2, "yangi")
print(f"2-indexni oldidan yangi element qo'shildi: {aralash_list}")

aralash_list.pop()
print(f"oxirchi element o'chirildi {aralash_list}")

aralash_list.extend([-3, 3, 4])
print(aralash_list)

print(aralash_list.index(True))