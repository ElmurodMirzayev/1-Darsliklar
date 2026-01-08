class User:
    def __init__(self, ism, familiya, login, t_yil, e_mail):
        self.login = login
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.mail = e_mail

    def get_dict_info(self):
        user_dict_info = {
            "login": self.login,
            "ism": self.ism,
            "familiya": self.familiya,
            "t_yil": self.t_yil,
            "mail": self.mail
        }

        return user_dict_info
    
    def get_info(self):
        return f"{self.familiya} {self.ism} {self.t_yil} da to'g'ilgan.\nE-mail: {self.mail}\nLogin: {self.login}"
    


    
user1 = User("Elmurod", "Mirzayev", "elmurod20050402", "2005", "elmurod20050402@gmail.com")

print(user1.get_info())




class Avto:
    def __init__(self, model, rang, korobka, narx):
        self.model = model
        self.rang = rang
        self.korobka = korobka

        self.narx = narx
        self.kilometr = 0

    def info(self):
        return f"avtomobil modeli: {self.model}\nrangi: {self.rang}\nkorobka: {self.korobka}\nnarxi: {self.narx}\nkilometr: {self.kilometr}"
    
    

    def update_kilometr(self, kilometr):
        self.kilometr = kilometr