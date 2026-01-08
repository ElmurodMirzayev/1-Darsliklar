# class Shaxs:
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil


#     def get_info(self):
#         info = f"{self.ism} {self.familiya}."
#         info += f"Passport: {self.passport}, {self.tyil} - yilda tug'ilgan"
#         return info
    
#     def get_age(self, yil):
#         return yil - self.tyil
    

# class Fan:
#     def __init__(self, nomi):
#         self.fan_nomi = nomi

# matimatika = Fan("Matimatika")
# ona_tili = Fan("Ona tili")
# rus_tili = Fan("Rus tili")
# ingliz_tili = Fan("Ingliz tili")



# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil):
#         super().__init__(ism, familiya, passport, tyil)
#         self.fanlar: list[Fan] = []
    
#     def fanga_yozil(self, fan: str):
#         self.fanlar.append(Fan(fan))

#     def remove_fan(self, fan: str):
#         for our_fan in self.fanlar:

#             if our_fan.fan_nomi == fan:
#                 self.fanlar.remove(our_fan)
#                 return

#         print("Siz bu fanga yozilmagansiz")
    



# # t = Talaba("Elmurod", "Mirzayev", "9238u4u", 2005)
# # t.fanga_yozil("Matimatika")
# # t.remove_fan("Matimatika")
# # print(t.fanlar)


# class Professor(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil):
#         super().__init__(ism, familiya, passport, tyil)
#         self.tajriba = "10 yillik"

#     def get_all_info(self):
#         info = f"Professor {self.ism} {self.familiya}\n"
#         info += f"Tajribasi: {self.tajriba}\n"
#         info += f"Passport: {self.passport}\n"
#         return info



# professor1 = Professor("Elmurod", "Mirzayev", "AD123456", 2005)

# print(professor1.get_age(2025))
# print(professor1.get_all_info())



class Inson():
    def __init__(self, ism, yosh, buy, millat):
        self.ism = ism
        self.yosh = yosh
        self.buy = buy
        self.millat = millat

    def get_name(self):
        return self.ism
    

class Foydalanuvchi(Inson):
    def __init__(self, ism, yosh, buy, millat, nick_name, ID):
        super().__init__(ism, yosh, buy, millat)
        self.id = ID
        self.nick_name = nick_name

    def get_nick_name(self):
        return self.nick_name
    
    def get_id(self):
        return self.id
    

class Admin(Foydalanuvchi):
    def __init__(self, ism, yosh, buy, millat, nick_name, ID, type_admin):
        super().__init__(ism, yosh, buy, millat, nick_name, ID)
        self.type_admin = type_admin

    def get_type_admin(self):
        return self.type_admin
    




user1 = Admin("Elmurod", 20, 170, "Uzbek", "@El_Murod20050402", 1355232, "super admin")

print(user1.get_name())




class Cat:
    def __init__(self, name: str, color: str, height_sm: int, weight_kg: int):
        self.name = name
        self.color = color
        self.height_sm = height_sm
        self.weight_kg = weight_kg
        self.is_cat_sleeping = True
        self.is_cat_angry = False

    def call_cat(self):
        if not self.is_cat_sleeping:
            return f"You can't call the {self.name} because cat is sleeping..."
        else:
            return f"{self.name} is coming..."
        
    def pet_cat(self):
        if not self.is_cat_angry:
            return f"The {self.name} is purring..."
        else:
            return f"The {self.name} is scratching you"

    
    




