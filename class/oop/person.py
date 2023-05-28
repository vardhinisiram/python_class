class Person:
    
    def __init__(self, n, a, h, w, q, c, g) -> None: # constructor        
        self.name = n
        self.gender = g
        self.age = a
        self.height = h
        self.weight = w
        self.qualification = q
        self.city = c
        self.activity = None

    def setName(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def sleeping(self):
        self.utility = "bed"
        self.activity = "SLEEP"
        print(self.name, " is sleeping")

    def eating(self):
        self.activity = "eating"
        print(self.name, " is ", self.activity)

    def get_details(self):
        print(self.name, self.age, self.height, self.weight, self.qualification, self.city, self.activity, self.gender)
        if self.activity == "SLEEP":
            print(self.name, " is sleeping on ", self.utility)


if __name__ == "__main__":
    # creating object:
    obj1 = Person("Tom", 20, 5, 16, "Grad", "singapore",'M')
    obj2 = Person("Jerry", 30, 5.5, 80, "Phd", "rentichintala", 'M')
    obj3 = obj1
    obj1.get_details()
    obj3.get_details()

    obj1.setName("batman")

    obj1.get_details()
    obj3.get_details()
    obj2.sleeping()
    obj2.get_details()
    obj1.get_details()
    obj2.eating()
    obj2.get_details()
    obj1_age = obj1.get_age()
    print("Object 1 age is ", obj1_age)
    # This is not at all a good programming practice
    print(obj1.age, obj1.name, obj1.height, obj1.weight, obj1.qualification, obj1.city)
    obj1.height = 98
    obj1.get_details()
