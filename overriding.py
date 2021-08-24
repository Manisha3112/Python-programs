class Mark:
    
	def test1(self):
		print('He scored 90% in test1')
		
	def test2(self):
		print('He scored 80% in test2')
	

class Modified(Mark):
	
	def test2(self):
		print('OOPS!! He scored 85% in test2')
		
	def test3(self):
    		print('He scored 95% in test3')
		

obj =Modified()
obj.test1()
obj.test2()
obj.test3()
