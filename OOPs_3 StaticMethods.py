class Employee:
    num_of_emps = 0

    def __init__(self, first, last, pay) :
        self.last = last
        self.first = first
        self.email = first + last + '@email.com'
        self.pay = pay 
        
        Employee.num_of_emps += 1
        
    def fullname (self):
            return '{} {}'.format (self.first, self. last)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 6 or day.weekday() == 5:
             return False
        return True
        # else:
        #      return True ... this is wrong, think why

# MONDAY -0 ..... SATURDAY - 5.... SUNDAY - 6


        
import datetime
my_date = datetime.date(2023, 8, 26)

# saturday and sunday isn't working day

print (Employee.is_workday(my_date))
 
    

