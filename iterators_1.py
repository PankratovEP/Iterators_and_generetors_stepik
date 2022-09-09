from random import *
'''lst = [1, True, 0, 'ddfg', 12.222, [1,2]]
iterator = iter(lst)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
my_iter = iterator
while True:
    try:
        i = next(my_iter)
        print(i)
    except StopIteration:
        break
        '''
class RandomIterator:
    def __iter__(self):
        return self

    def  __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
        else: raise StopIteration
        return random()

for x in RandomIterator(6):
    print(x)

class  DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:  raise StopIteration
class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)
for pair in MyList([1,23,7,8]):
    print(pair)



