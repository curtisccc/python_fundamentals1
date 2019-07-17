class Cat:
    # a class representing cats
    
    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.food = preferred_food
        self.time = meal_time

    def __str__(self):
        return f"Name: {self.name} Preferred food: {self.food} Usual meal time: {self.eats_at()}"
    
    def eats_at(self):
        if self.time >= 13:
            return f"{self.time - 12} PM"
        else:
            return f"{self.time}AM"
    
    def meow(self):
        return f"My name is {self.name} and i like to eat {self.food} at {self.eats_at()}"

muca = Cat("Muca", "dry food", 8)
chava = Cat("Chava", "gooey food", 24)

print(muca)
print(muca.meow())
print(chava)
print (chava.meow())
