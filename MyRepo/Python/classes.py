class Pet:
    def __init__(self,name, breed, color):
        self.name = "Malachi"
        self.breed = "great pyrneese"
        self.color = "black and white"

dog = Pet("Malachi","great pyrneese","black and white")
cat = Pet("Esper","bangle","orange with brown spots")
print(f"{dog.name} is a {dog.breed} and is {dog.color}")
print(f"{cat.name} is a {cat.breed} and is {cat.color}")


