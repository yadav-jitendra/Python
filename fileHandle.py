handleName = open('kids','w')
x = 0
while x < 4:
    name = input('enter a world: ')
    handleName.write(name + '\n')
    x +=1
handleName.close()

handlName = open('kids','r')
for line in handlName:
    print(line)

handlName.close()