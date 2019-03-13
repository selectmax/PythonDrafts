def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


print(mysum([0, 1, 2]))