class Welcome:
    
    def wish(self, user_name=None):
    
        if user_name is not None:
            print('Hi ' + user_name)
        else:
            print('Hi')

    def product(self,a=None,b=None):
        if a!=None and b!=None:
             print("Product= ",(a*b))
        elif a!=None:
               num=int(input("please enter b value = "))
               print("Product=",(a*num))
        else:
              num1=int(input("please enter a value = "))
              num2=int(input("please enter b value = "))
              print("Product=",(num1*num2))

obj =Welcome()
obj.wish()
obj.wish('Manisha')
obj.product(10,20)        
obj.product()
obj.product(10)
