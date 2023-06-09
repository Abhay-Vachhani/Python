class Program:
    def code(abhay):
        print('This is method of program class')
    
# program = Program()
# program.code()

class Course(Program):
    def code(dev):
        print('The method of Course class')
        # Call parent method
        super().code()
    
course = Course()
course.code()