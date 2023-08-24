class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay) :
        self.last = last
        self.first = first
        self.email = first + last + '@email.com'
        self.pay = pay 
        
        Employee.num_of_emps += 1
        
    def fullname (self):
            return '{} {}'.format (self.first, self. last)
        
    def apply_raise (self):
            self.pay = int (self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
            cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

          
            
emp_1 = Employee ('Rohan','Rajput', 50000)
emp_2 = Employee ("Test","Employee", 60000)

emp_str_1 = 'Paarth-Banaudha-100'
emp_str_2 = 'Tanishka-Agarwal-200'
emp_str_3 = 'Tushar-Singh-300'

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)
emp_5 = Employee.from_string(emp_str_3)



Employee .set_raise_amt(1.2)

print(emp_2.pay)
Employee.apply_raise(emp_2)
print (emp_2.pay)

print(Employee.num_of_emps)