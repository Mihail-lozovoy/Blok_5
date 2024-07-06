class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print("Название :", h1.name,"Кол-во этажей :", h1.number_of_floors)
print("Название :", h2.name,"Кол-во этажей :", h2.number_of_floors)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
