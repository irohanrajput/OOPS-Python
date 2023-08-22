# class variables are the variables that are shared among all the instance in a  

class Employee:
    raise_amount  = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.fname = first #these are instance variables   
        self.lname = last
        self.salary = pay
        self.email = first + "." + last + '@kiet.edu'
        self.fullname = first + ' ' + last

        # to keep track of no of employees, we'll add write the code within init method because the init method runs everytime we create a new employee

        Employee.num_of_emps += 1

    def emp_details(emp_no):
        print (f'Name: {emp_1.fname} {emp_1.lname}')
        print (f'Salary: {emp_1.salary}')


    def apply_raise (self):
        self.salary = int(self.salary * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('Rohan', 'Rajput', 100)

print(Employee.num_of_emps)

emp_2 = Employee('Chaaku', 'Rampuriya', 1000)

print(Employee.num_of_emps)



Employee.emp_details(emp_1)
emp_1.apply_raise()

print ("after increament:")
Employee.emp_details(emp_1)