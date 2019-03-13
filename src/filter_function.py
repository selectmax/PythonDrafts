nums = [11, 22, 33, 44, 55]
res = filter(lambda x: x % 2 == 0, nums)

print(type(res))
print(res)

print(type(list(res)))
print(list(res))