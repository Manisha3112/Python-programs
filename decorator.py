def div(first,last):
    print(first/last)
def swap(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=swap(div)
first=int(input('Enter first number: '))
last=int(input('Enter last number: '))
div(first,last)