try:
    a = int(input('enter a number: '))
    b = int(input('enter another number: '))
    print('a/b = ', a / b)
    print('a+b = ', a + b)
    print('done calculations')
except ValueError:
    print('cannot convert to number')
except ZeroDivisionError:
    print('division by zero')
except:
    print('something went wrong')
