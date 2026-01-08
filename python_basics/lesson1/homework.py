#print funksiyasiga 50 ta misol

print("\n\n\n\n\n")
print("print chop etish vazifasini.")
print("""Konsolda hello world yozuvini ko'rgan bo'lsangiz, tabriklaymiz!""")
print("Syntax Error")
print("Mening ismim Elmurod")
print('soat 10:00 da dars bor')
print("Hammaga salom.")
print("Arifmetik ammallar", "qo'shish, ayrish, ko'paytirish, bo'lish")
print("ASUS Vivobook")

print((3+3)*2)
print(4**2)
print(20-10)
print(7/3+20)
print(66-9+2+10)
print(-100 + 80)
print(22//20)
print(40/10)
print(99-99)
print(100%3)


print("Yaxshi otga bir qamchi, \nYomon otga ming qamchi")
print('Men "ASUS" markali \nnoutbuk sotib oldim')
print("Mening 'reks' ismli itim bor!")
print("Python dasturlash tilida izohlar # shu belgi orqali \nOrqali qo'yiladi.")
print("Pythonda darajaga oshirish uchun ** dan foydalansa bo'ladi.")
print("Dasturlash muhitida \nbir nechta tiplar bor")
print("O'zgaruvchilar ingliz tilida variable deb ataladi.")
print('Kompyuter ingliz tilidagi "compute" - hisoblash so\'zidan olingan')
print("Python o'rganishda tez va qulay hisoblanadi.")


#---------------------------------------------------------------------

print("\n\n\n\n\n")
#input funksiyasiga misol.
ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
yosh = input("Yoshingizni kiriting: ")
jins = input("Jinsingizni kiriting: ")
qiziqish = input("Qiziqishlaringiz haqida yozing: ")
print(f"{ism} {familiya} assalomu alaykum!")
print(f"sizning qiziqishlaringiz {qiziqish}")
print(f"sizning yoshingiz {yosh}")

#------------------------------------------------------------------
print("\n\n\n\n\n")

#Amaliyot
#24-betdagi.
print("Assalomu alaykum")
print("Xayrli tong!")
print(2+4*2)
print(19/2)
print(2**4)

print("Birinchi amaliyot qilindi")
print("Hammaga salom!")
print(2**4**2)
print("19%2 = ", + 19%2)
print("K", "o", "m", "p", "y", "u", "t", "e", "r")
print("K" + "o" + "m" + "p" + "y" + "u" + "t" + "e" + "r")

#--------------------------------------------------------------------


print("\n\n\n\n\n")

#Kitobdagi amaliyotlarni bajarish
#30-betdagi amaliyot

print("30-betdagi amaliyot")
#1
print('"Next", "Tico", \'Damas\' ko\'rganlar qilar havas.')
#5 ning 4 chi darajasini toping
print(f"5 ning 4 darajasi {5**4} ga teng")

#22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print(f"22 ni 4 ga bo'lganda {22%4} qoldiq qoladi")

#Tomonlari 125 ga teng bo'lgan kvadratning yuzi va perimetrini toping 
print(f"Tomonlari 125 ga teng bo'lgan kvadratning yuzi {125**2} ga teng \n{125*4} bu kvadratning perimetri")

#Diametri 12 ga teng bo'lgan doiraning yuzasini toping (pi = 3.14).
print(f"Diametri 12 ga teng bo'lgan doiraning yuzi {2*3.14*(12/2)**2}")

#Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakningning gipotenuzasini toping
print(f"Katetlari 6 va 7 ga teng bo'lgan uchburchakning gipotenuzasi {(6**2+7**2)**(1/2)} ga teng.")


#-------------------------------------------------------------------


print("\n\n\n\n\n")

#33 betdagi amaliyot
a = "Hello Wordl!"
print(a)

xabar = "2025-12-30"
print(xabar)
xabar = "2026-01-01"
print(xabar)


radius = 5
pi = 3.14159
yuza = pi * radius**2
print("Radiusi", radius, "ga teng doira yuzi=", yuza)



#---------------------------------------------------------------------

print("\n\n\n\n\n")

#strip, rstrip, lstrip metodlari
narx = "    2000       "
print("Olmaning narxi " + narx.strip() + " so'm turadi.")
#---------------------------------------------------------------------

print("\n\n\n\n\n")

#41 betdagi amaliyot
kocha = "Bog'bon"
mahalla = "sag'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"


print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

kocha = input("Ko'changizni kiriting: ")
mahalla = input("Mahallangizni kiriting: ")
tuman = input("Tumaningizni kiriting: ")
viloyat = input("Viloyatingizni kiriting: ")

print(f"{kocha},\n{mahalla},\n{tuman},\n{viloyat}\n")


manzil = f"ko'cha: {kocha}, mahalla: {mahalla}, tuman: {tuman}, viloyat: {viloyat}"

print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())

# --------------------------------------------------------------------