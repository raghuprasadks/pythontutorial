try:
    print(1/0)
except ZeroDivisionError:
    print("You can't divide by zero, you're silly.")


import sys
print ("Lets fix the previous code with exception handling")
try:
    number = int(input("Enter a number between 1 - 10"))
except ValueError:
    print("Err.. numbers only")
    sys.exit()
print ("you entered number", number)

import sys
randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)

try:
	a = int(input("Enter a positive integer: "))
	if a <= 0:
		raise ValueError("That is not a positive number!")
except ValueError as ve:
		print(ve)

try:
	file2 = open("test.txt",encoding = 'utf-8')
	line=file2.readline()
	while(line!=""):
    	print(line)
    	line=file2.readline()
   # perform file operations
except:
	print("Error in reading a file")	    
finally:
	print("Closing the file")
	file2.close()