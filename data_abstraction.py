class College:     
   def department(self):   
      pass  

class Ece(College):   
     def department(self):   
      print("Ece department average score is 90%")   
  
class Csc(College):   
   def department(self):   
      print("Csc department average score is 85%")   
  
class It(College):   
   def department(self):   
      print("It department average score is 75%")   
  
class Eee(College):   
   def department(self):   
      print("Eee department average score is 70%")     
ece = Ece()   
ece.department()   
  
eee = Eee()   
eee.department()   
  
csc = Csc()   
csc.department()   
  
it = It()   
it.department()   