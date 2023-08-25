class workers():

    def __init__(self, name, idnumber, salary):
        self.name = name
        self.idnumber = idnumber
        self.salary = salary


    
    def speakNow(self):
        print(f'My name is {self.name} and my ID Number is : {self.idnumber}')
    
class TopGuys(workers):
    def __init__(self, name, idnumber, salary, post, in_charge):
        self.post = post
        self.charge = in_charge
        
        super().__init__(name, idnumber, salary)

    
    def speakNow(self):
        print(f"I am {self.name} and my ID Number doesn't matter but for the record, it is : {self.idnumber}. I am the {self.post} here and the area I handle is {self.charge}")
        

emp1 = workers("abdul", 221, 100)
emp2 = workers("mahesh", 223, 120)

tpg1 = TopGuys("Rohan", 21, 1000, "founder", "everything") 


tpg1.speakNow()


