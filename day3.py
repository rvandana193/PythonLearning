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


class Animal():
    def __init__(self):
        print('ANIMAL CREATED')
    def who_am_i(self):
        print('Iam an animal')
    def eat(self):
        print('Iam eating')
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
my_dog=Dog()
my_dog.eat()


class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
b=Book('Python Learning','John','200')
print(b) #len(b)


def ask_for_int():
    try:
        result = int(input("Please provide no:"))
    except:
        print("Whoops!That is not a number")
    finally:
        print("End of try, except and finally")
ask_for_int()