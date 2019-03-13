from functools import reduce

items = [2, 1, 2, 3, 4]
sum_all = reduce(lambda x,y: x^y, items)

print(type(sum_all))
print(sum_all)