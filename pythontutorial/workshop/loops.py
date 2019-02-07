#while loop

num = 5

while(num>0):
    print('numer is', num)
    num-= 1

#For
for  letter in 'python':
    print("Letter ",letter)

#For loop with else

for  letter in 'python':
    if(letter=='k'):
        print("K found ",letter)
else:
    print('Cound not find k')

#
for  letter in 'python':
    if(letter=='o'):
        print("o found ",letter)
else:
    print('Loop exhausted')


# break

for i in range(1,5):
    print('Usage of break ',i)
    if(i==4):
        break

# continue

for i in range(1,5):
    print('Usage of continue ',i)
    if(i==4):
        continue

#pass
x = 1
while x<=3:
    if (x==1):
        print('python is a scripting language')

    elif (x==2):
        pass
    else:
        print('Fun to learn python')
    x+=1
    