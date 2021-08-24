class Student1:
    def test1(self):
        print("Student1 scored 90% in test1")
    
    def test2(self):
        print("Student1 scored 80% in test2")

class Student2:

    def test1(self):
        print("Student2 scored 95% in test1")
    
    def test2(self):
        print("Student2 scored 87% in test2")

def test(percentage):
    percentage.test1()
    percentage.test2()
jack = Student1()
jill = Student2()
test(jack)
test(jill)