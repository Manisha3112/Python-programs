class college:
    def __init__(self, student_name, department_name):
      self.student_name = student_name
      self.department_name = department_name

    def print(self):
       print("Hi",self.student_name,"Welcome to ", self.department_name,"department")

x = college("Manisha", "ECE")
x.print()