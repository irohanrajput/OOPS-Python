class person:
    def __init__(self, name, city, occupation, pay):
        self.name = name
        self.home = city
        self.job = occupation
        self.salary = pay

    def speakNow(self):
        print(f'My name is {self.name}, I am from {self.home}. For living, I work as {self.job} with a salary of Rs{self.salary}.')

   