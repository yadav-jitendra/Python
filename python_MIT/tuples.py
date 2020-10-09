def quo_rem(x, y):
    q = x // y
    r = x % y
    return (q, r)


(qu, rem) = quo_rem(5,2)
print((qu+1,rem+1))
