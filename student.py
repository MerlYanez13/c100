class student (object):
    def __init__(self,age,level, name ,grade=None):
        self.name=name
        self.age=age
        self.level=level
        self.grade=grade or {}
    def setgrade(self,course, grade):
        self.grade[course]=grade
    def getGrade(self,course):
        return self.grade[course]

s1=student(14, 9,"Merl", {"science":9})
s2=student(12, 7,"Bob", {"Math":7})

print (s1.getGrade("science"))