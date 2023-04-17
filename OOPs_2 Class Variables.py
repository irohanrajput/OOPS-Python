class Employee:
    raise_amount  = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.salary = pay
        self.email = first + "." + last + '@kiet.edu'
        self.fullname = first + ' ' + last

        Employee.num_of_emps += 1

    def apply_raise (Employee):
        Employee.salary = int(Employee.salary * Employee.raise_amount)

print (f'Initially threre were {Employee.num_of_emps} employes in the organisation. \n')



emp_1 = Employee('Rohan', 'Rajput', 100)
emp_2 = Employee('Chaaku', 'Rampuriya', 1000)


print('The salary before the raise was {} for {}'.format(emp_1.salary, emp_1.fullname))
emp_1.apply_raise()
print('The salary after the raise was {} for {}'.format(emp_1.salary, emp_1.fullname))

print ('\n')
    
print('The salary before the raise was {} for {}'.format(emp_2.salary, emp_2.fullname))
emp_2.apply_raise()
print('The salary after the raise was {} for {} \n'.format(emp_2.salary, emp_2.fullname))



print (f'And now threre are {Employee.num_of_emps} employes in the organisation.')

    