class TopTen:
    def __init__(self):
      self.first=int(input('Enter first number: '))
      self.last=int(input('Enter last number: '))

    def __iter__(self):
       return self

    def __next__(self):
       if self.first<=self.last:
          square=self.first*self.first
          self.first += 1
          return square
       else:
           raise StopIteration
values=TopTen()
for i in values:
    print(i)