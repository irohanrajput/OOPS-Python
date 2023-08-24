class person:
    def __init__(self, name, city, occupation, yob):
        self.name = name
        self.home = city
        self.job = occupation
        self.yearofbirth = yob
    def speakNow(self):
        print(f'My name is {self.name}, I am from {self.home}. For living, I work as {self.job} and I was born in year {self.yearofbirth}')

        

emp_1007 = person('Rohan', 'California', 'Software Engineer', 2003)


emp_1007.speakNow()

#Output:  My name is Rohan, I am from California. For living, I work as Software Engineer and I was born in year 2003
