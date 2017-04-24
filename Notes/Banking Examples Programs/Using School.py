#mr t
#jan 1 2000
# this program proves that I know what I am doing

import school

student=[]

student.append(school.Student("Mishael Yearwood"))
student.append(school.Student("Mike Lescisin"))
student.append(school.Student("Kayleigh Brownhill"))

for i in range (len(student)):
    student[i].init()

student[1].set_dob("Jan 19 1995")
student[1].set_height(160)
student[1].set_grade(11)


student[2].set_dob("Aug 21 1994")
student[2].set_height(165)
student[2].set_grade(12)

mrT=school.Teacher("Mr. Tacchino")
mrT.set_dob("June 21 1978")
mrT.set_height(200)
mrT.yearExp=9

for i in range (len(student)):
    print student[i].name
    print student[i].birthdate
    print student[i].height
    print student[i].grade
    student[i].nonUniform()
    print student[i].uniformInfraction
