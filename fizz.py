# Write a python generator function which generates fizz buzz tuples infinitely.
# Every successive call to next on the generator should return (index, <content>)
# where index starts from 1 and increases by one every call.
#
# The content should be "fizz" for multiples of 3, "buzz" for multiples of 5 and "fizz", "buzz" for multiples
# of both 3 and 5.
#
# e.g. the first 5 calls to the generator should return (1, None), (2, None), (3, "fizz"), (4, None), (5, "buzz")
# for 15th call the result will be (15, "fizz", "buzz")
def fizz(last):
    first=1
    while(first<=last):
        if(first%3==0 and first%5==0):
            yield(first,'"fizz","buzz"')
        elif(first%3==0):
            yield(first,"fizz")
        elif(first%5==0):
            yield(first,"buzz") 
        else:
            yield(first,"None")           
        first+=1       
first=int(input("Enter first number: "))
last=int(input("Enter last number: "))
for first in fizz(last):
    print(first)            
