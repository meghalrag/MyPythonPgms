class Mark:
    def __init__(self , eng , mal):
        self.english = eng
        self.malayalam = mal


class Student:
    def __init__(self ,name , mark):
        self.name = name
        self.Mark = mark

students = []
mark1 = Mark(10,20)
s1 = Student("s1",mark1)
students.append(s1)

for student in students:
    print student.name
    print student.Mark.english
    print student.Mark.malayalam