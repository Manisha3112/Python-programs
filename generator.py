def topTen():
    first=int(input('Enter first number: '))
    last=int(input('Enter last number: '))
    while first<=last:
        square=first*first
        yield square
        first+=1
value=topTen()
for i in value:
    print(i)