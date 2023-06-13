class Employee:
    raise_amount  = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.salary = pay
        self.email = first + "." + last + '@kiet.edu'
        self.fullname = first + ' ' + last

    def emp_details(emp_no):
        print (f'Name: {emp_1.fname} {emp_1.lname}')
        print (f'Salary: {emp_1.salary}')


    def apply_raise (Employee):
        Employee.salary = int(Employee.salary * Employee.raise_amount)

emp_1 = Employee('Rohan', 'Rajput', 100)
emp_2 = Employee('Chaaku', 'Rampuriya', 1000)




Employee.emp_details(emp_1)