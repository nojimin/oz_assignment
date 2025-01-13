class Eagle:
    def __init__(self, name, species, age, weight, wingspan):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight
        self.wingspan = wingspan

    def info(self):
        return f"{self.name}은(는) 종은 {self.species}이고, 나이는 {self.age}세이며, 몸무게는 {self.weight}kg이며, 날개 길이는 {self.wingspan}cm입니다."