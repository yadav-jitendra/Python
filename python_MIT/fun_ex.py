def multi_recursion(x,y):
    if y == 1:
        return x
    else:
        return x + multi_recursion(x, y-1)

print(multi_recursion(2,10))