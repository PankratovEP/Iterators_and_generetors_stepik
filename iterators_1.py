lst = [1, True, 0, 'ddfg', 12.222, [1,2]]
iterator = iter(lst)
'''print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))'''
my_iter = iterator
while True:
    try:
        i = next(my_iter)
        print(i)
    except StopIteration:
        break
