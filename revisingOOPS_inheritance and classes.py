# https://chat.openai.com/c/e1875737-cf79-40a4-86de-433036db6111


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
    #here 'printname' is a method, a function that is associated to an object.


person1 = Person("Raju", "Yadav")
person1.printname()

#let's talk about inheritance. 

class Student(Person):
    def __init__(self, fname, lname, gradYear):
        super().__init__(fname, lname)
        self.graduationyear = gradYear

        # when we add the __init__() function, the child class will no longer inherit the parent's __init__() function.

        # super() function automatically inherits the methods and properties from its parent.

    def student_info(self):
        print(
            f"The name is {self.firstname} {self.lastname} \nGraduated in the year: {self.graduationyear}."
        )

        # If same name, inheritance of the parent method will be overridden and the one from child class will dominate.

rohan = Student("Rohan", "Rajput", 2026)
rohan.student_info()

print(".....................................................................................")

#polymerphism

