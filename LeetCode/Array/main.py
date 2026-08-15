#Type Eas
class Talaba:
    def __init__(self,ism,familya,tyil):
        self.ism=ism
        self.familya=familya
        self.tugilgan_yil=tyil
        self.bosqich=1
    def get_name(self):
        return self.ism
    def get_lastname(self):
        return self.familya
    def get_age(self):
        return self.tugilgan_yil
    def get_info(self):
        return f"{self.ism} {self.bosqich} - bosqich talabasi"
    def set_bosqich(self,yangi_bosqich):
        self.bosqich=yangi_bosqich
    def update_boshqich(self):
        self.bosqich+=1
talaba1=Talaba("Shaxzod","Sadullayev",2005)
print(talaba1.get_info())
talaba1.update_boshqich()
talaba1.update_boshqich()
talaba1.update_boshqich()
print(talaba1.get_info())
    