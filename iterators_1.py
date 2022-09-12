from random import *
lst = [1, True, 0, 'ddfg', 12.222, [1,2]]
my_iter = iter(lst)
def prohod():
    while True:
        try:
            i = next(my_iter)
            print(i)
        except StopIteration:
            break
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


class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            return True
    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1 :
            return True
    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            pos, neg = 0, 0
            for funcsia in self.funcs:
                if funcsia(i):
                    pos += 1
                else: neg +=1
            if self.judge(pos, neg):
                yield i



