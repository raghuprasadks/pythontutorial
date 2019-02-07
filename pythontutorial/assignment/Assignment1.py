# 1. /write a program that prints no of lowercase 'a' snd 'o' ,'L' and 'N'

s = 'Discover,Learning,with,Edureka'
print(' count o ', s.count('o'))
print(' count a ',s.count('a'))

print(' count L ', s.count('L'))
print(' count N ',s.count('N'))


#2. Remove

import string

s='www.edureka.in'
print(s)

print (s.strip('w'))
#print(s.strip(string.ascii_lowercase))
print(s.strip(string.lowercase))
print(s.strip(string.printable))

#3. Type of
num1 = 0X7AE #- Hex constants
num2 = 3+4j #- Complex
num3 = -01234 # - octal constant
num4 = 3.14e-2 #- Floating point numbers


#4. String formatter
#1. Character  - %s
#2. Signed decimal integer - %d
#3. Octal %o
#4. Hexadecimal integer - %X
#5. Floating point real number - %f
#6. Exponential - %e

"My name is %s and my age is %d years" %('Raghu,45')
"My car's number is %o" %('0010')
"My pan card number is %X" %('0XB5')
"My weight is approximately %f" %('73.5')
"Currently my account balance is %e " %('4.5e6')


