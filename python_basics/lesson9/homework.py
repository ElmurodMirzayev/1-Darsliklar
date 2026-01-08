def yoshini_top(ism, yosh):
    print(f"Assalomu alaykum {ism}!")
    print(f"Siz {2025-yosh} yilda to'g'ilgan ekansiz.")


def kvadrat_kub_hisobla(son):
    print(f"{son} ning kvadrati: {son**2}")
    print(f"{son} ning kubi: {son**3}")


def juft_toq_top(son):
    if son % 2 == 0:
        print("Bu juft son")
    else:
        print("Bu toq son")


def taqqosla(a, b):
    if a > b:
        print(f"{a} soni katta")
    elif a < b:
        print(f"{b} soni katta")
    else:
        print("sonlar teng")


def darajaga_oshir(x, n = 2):
    print(f"{x} ning {n} chi darajasi {x**n} ga teng.")

def bolinadigan_sonlarni_top(son):
    for i in range(2, 11):
        if son % i == 0:
            print(i)


def my_range(boshi, oxiri, qadam=1):
    sonlar = []

    while boshi<oxiri:
        sonlar.append(boshi)
        boshi += qadam

    return sonlar




def user_info(ism, familiya, tugilgan_yil, tugilgan_joy, e_manzil = None, tel_raqam = None):
    tugilgan_yil = int(tugilgan_yil)
    if not e_manzil:
        e_manzil = "Nomalum"
    if not tel_raqam:
        tel_raqam = "Nomalum"

    malumotlar = {"ism": ism,
                  "familiya": familiya,
                  "tugilgan_yil": tugilgan_yil,
                  "yoshi": 2025-tugilgan_yil,
                  "tugilgan_joy": tugilgan_joy,
                  "e_manzil": e_manzil,
                  "tel_raqam": tel_raqam, }
    
    return malumotlar





# users = []
# while True:
#     print("\n")
#     ism = input("ismingizni kiriting: ")
#     familiya = input("familiyangizni kiriting: ")
#     tugilgan_yil = input("tug'ilgan yilingizni kiriting: ")
#     tugilgan_joy = input("tug'ilgan joyingizni kiriting: ")
#     e_manzil = input("elektron manzilni kiriting (Majburiy emas): ")
#     tel_raqam = input("telefon raqamingizni kiriting (Majburiy emas): ")

#     user = user_info(ism, familiya, tugilgan_yil, tugilgan_joy, e_manzil, tel_raqam)
#     users.append(user)
#     print("\n")
#     if input("to'xtatishni hoxlaysizmi ? (ha/yuq): ").lower() == "ha":
#         break

# print("\n")
# print("Userlar ro'yxati: \n")
# for user in users:
#     for key, value in user.items():
#         print(f"{key}: {value}")
#     print("\n")




def kattasini_aniqlash(a, b, c):
    if a >= b and a >= b:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= b and c >= a:
        return c




def circle_info(radius):
    pi = 3.14
    yuzi = pi*radius**2
    deametr = 2*radius
    peremetr = 2*pi*radius
    info = {
        "radius": radius,
        "yuzi": yuzi,
        "deametr": deametr,
        "peremetr": peremetr
    }

    return info



def is_tub_son(son):
    if son <= 1:
        return "Bu tub son emas"
    for i in range(2, son):
        if son % i == 0:
            return "Bu tub son emas"

    return "Bu tub son"


def fibonachi(son):
    first = 1
    empty = 0
    second = 1
    fibo_sonlar = [1, 1]
    while second < son:
        empty = second
        second = first + second
        first = empty
        fibo_sonlar.append(second)

    return fibo_sonlar



yozuvlar = ["salom", "elmurod", "qandaysan?", "qarshi", "hammasi", "yaxshi"]
yozuvlar[0].upper()
def boshini_ozgartirish(royhat: list):
    yozuvlar = royhat[:]
    for i in range(len(yozuvlar)):
        yozuvlar[i] = yozuvlar[i].capitalize()

    return yozuvlar




def bahola(ismlar: list):
    baholar = {}
    ismlar = ismlar[:]
    for i in range(len(ismlar)):
        ism = ismlar[i]
        baho = input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar

talabalar  = ["ali", "vali", "hasan", "husan"]
baholar = bahola(talabalar)
print(baholar)
print(talabalar)