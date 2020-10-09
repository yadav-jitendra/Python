x = int(input('enter a number '))
ans = 0
neg_flag = False
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans += 1
if ans**2 == x:
    print(f'the square root of {x} is {ans}')
else:
    print(f'{x} is not perfect square')
    if neg_flag:
        print(f'just checking ... did u mean {-x}?')

