decimal = int(input('Enter a decimal value: '))
num = decimal
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
if isNeg:
    result = '-' + result
print(f'Binary repres. of {decimal} is {result}')
