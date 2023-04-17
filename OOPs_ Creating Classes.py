class employee:
    def __init__(self, first, last, pay): #self is instance jo btata hai kiske baare me baat ho rhi
         
        self.fname = first  #we're creating a variable 'self.first' and assigning it the value of 'first'
        self.lname = last
        self.salary = pay
        self.email = first + '.' + last + '@kiet.edu'
      # self.fullname = first + ' ' + last , but we'll use different method

    def fullname(self):  # *one argurment is given 
        return '{} {}'.format(self.fname, self.lname)

emp_1  = employee('Rohan', 'Rajput', 120000)
emp_2  = employee('chaaku', 'rampuriya', 125000)

print(emp_1.fullname()) # * no arguement is given but emp_1 itself gives one arguement 'self' to the func fullname

emp_1.fullname()  #we don't need to give an arguemetn, it already knows that we're talking about 'self'

employee.fullname(emp_1) #here we need to give the arguement

