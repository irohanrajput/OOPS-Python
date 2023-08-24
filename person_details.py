class person:
    def __init__(self, name, city, occupation, pay):
        self.name = name
        self.home = city
        self.job = occupation
        self.salary = pay

    def speakNow(self):
        print(f'My name is {self.name}, I am from {self.home}. For living, I work as {self.job} with a salary of Rs{self.salary}.')

    def increment(self, percent):
        self.salary = self.salary + self.salary * percent /100 
   

emp_1007 = person('Rohan', 'California', 'Software Engineer', 100)


emp_1007.speakNow()

#Output:  My name is Rohan, I am from California. For living, I work as Software Engineer with a salary of 100.

emp_1007.increment(30) #30 percent increment in salary

emp_1007.speakNow() 

#output: My name is Rohan, I am from California. For living, I work as Software Engineer with a salary of Rs130.0.
