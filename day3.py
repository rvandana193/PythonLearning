class Dog():
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots
my_dog= Dog(breed='Lab',name='Shane',spots='No')
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)


class Circle():
    pi = 3.14 #class-object attribute
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*Circle.pi
    def get_circumference(self):
        return self.radius*Circle.pi*2
my_circle=Circle(30)
print(my_circle.radius)
print(my_circle.get_circumference())
