def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"{func.__name__} only takes numbers as the argument")
    return inner_function
 


@exception_handler
def area_square(length):
    print(length * length)


@exception_handler
def area_circle(radius):
    print(3.14 * radius * radius)


@exception_handler
def area_rectangle(length, breadth):
    print(length * breadth)

length=int(input('Enter length: '))
breadth=int(input('Enter breadth: '))
radius=int(input('Enter radius: '))
area_square(length)
area_circle(radius)
area_rectangle(length, breadth)
area_square("HI")