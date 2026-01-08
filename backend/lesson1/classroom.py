# OOP object oriented programming


import time

class Car:
    def __init__(self, color, year, price, model, benzin = 100):
        self.color = color
        self.year = year
        self.price = price
        self.model = model
        self.benzin = benzin
        self.is_engine_on = False
        self.qizigan = False

    def start_car(self):
        if self.benzin > 0:
            if not self.is_engine_on:
                self.is_engine_on = True
                return "Mashina yoqildi"
            else:
                return "Mashina allaqachon yoqilgan"
        else:
            return f"Mashinaning benzinini to'ldiring"

    def qizdirish(self, vaqt=10):
        if self.is_engine_on:
            print(f"Mashina {vaqt} ga qizdirishga qo'yildi...")
            time.sleep(vaqt)
            self.qizigan = True
            return f"Mashina {vaqt} qizib bo'ldi"
        else:
            return f"Mashinani avval yoqish kerak."
        

    def haydash(self):
        if self.qizigan:
            print("Mashina haydashni boshladi")
            while True:
                time.sleep(2)
                self.benzin -= 1
                print(f"Mashinaning benzini {self.benzin} qoldi")
                if self.benzin <= 0:
                    return "Mashinaning benzini qolmadi..."
                
        else:
            return "Mashinani avval qizdiring"
                
    def benzinni_toldirish(self, miqdor = 100):
        self.benzin += miqdor

    def __dict__(self):
        
            

car1 = Car("qora", 2005, "128 000 so'm", "Lasetti", 200)

car1.__dict__()