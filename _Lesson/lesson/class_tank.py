class Tank:
    def __init__(self, name, ammo) : # self - return ค่า
        self.name=name # name1-ชื่อtank name2-parameter
        self.ammo=ammo
    def add_ammo(self, ammo):
        if self.ammo+ammo<=10:
            self.ammo+=ammo

    def fire_ammo(self):
        if self.ammo>0:
            self.ammo-=1 