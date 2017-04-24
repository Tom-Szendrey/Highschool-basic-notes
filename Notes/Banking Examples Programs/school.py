#mr t
#jan 1 2000
# this program proves that I know what I am doing

class Person(object):
    #the class methods variables and code goes here.

    def __init__(self, initial):
        self.name= initial
        self.birthdate=""
        self.height=0

    def set_dob(self,date):
        self.birthdate=date
        
    def set_height(self,h):
        self.height=h

class Student(Person):
    

    def init(self):
        self.uniformInfraction=0
        self.grade=0

    
    def set_grade(self,g):
        self.grade=g
        
    def nonUniform(self):
        self.uniformInfraction+=1
        
class Teacher(Person):
    
    yearExp=0
    
    def expIncrease(self):
        self.yearExp+=1
        
    def setOffice(self,o):
        self.office=o
        
