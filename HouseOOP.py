class Building():
    def __init__(self,owner):
        self.owner = owner
    def Owner(self):
        print(f"{self.owner} Own This House...")

class House(Building):
    def __init__(self,owner,color,floor,stares,ceil):
        self.owner = owner
        self.color = color
        self.floor = floor
        self.stares = stares
        self.ceil = ceil

    def paint_house(self):
        if self.color:
          print(f"{self.owner} House is Painted Fully {self.color}...")
        else:
            print(f"{self.owner} House is not Painted Yet...")
    def house_floor(self):
        if self.floor:
             print(f"{self.owner} House is Fully {self.floor} Floor...")
        else:
             print(f"{self.owner} House is not {self.floor} Furnished Yet...")

    def house_stares(self):
        if self.stares:
            print(f"{self.owner} House Has Beautiful {self.stares}...")
        else:
            print(f"{self.owner} Has not Furnished His House {self.stares} Yet...")
    
    def house_ceil(self):
        if self.ceil:
            print(f"{self.owner} House has Done Beautiful {self.ceil}...")
        else:
            print(f"{self.owner} Has not done {self.ceil}...")

a2=Building("Hamza")
a2.Owner()

a1 = House("Hamza's","White","Furnished","Stares","Ceiling")
a1.paint_house()
a1.house_floor()
a1.house_stares()
a1.house_ceil()