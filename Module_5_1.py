class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor

    def go_to(self, new_floor):
        print(self.name)
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Университетский', 5)
h2 = House('ЖК Победа', 10)
h1.go_to(5)
h2.go_to(11)
