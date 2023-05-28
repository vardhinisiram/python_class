from person import Person


class Student(Person):
    """
        This is a student class
    """
    def __init__(self, n, a, h, w, q, c, g, m) -> None:
        """
            This is a constructor
        """
        super().__init__(n, a, h, w, q, c, g)
        self.marks = m

    def reading(self):
        self.activity = "reading"
        print("Current activity is ", self.activity)

    def get_details(self):
        print(self.name, self.age, self.height, self.weight, self.qualification, self.city, self.activity, self.gender, self.marks)
        if self.activity == "SLEEP":
            print(self.name, " is sleeping on ", self.utility)

if __name__ == "__main__":
    s1 = Student("siva", 21, 5.4, 50, 'Bsc', 'plk', 'M', 100)

    s1.sleeping()
    s1.eating()
    s1.reading()
    s1.get_details()
    print(s1.name)

    print(dir(s1))
    print(s1.__doc__)