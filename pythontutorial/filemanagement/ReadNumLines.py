'''
You will often find the with statement for reading and writing files. The advantage is that the file will be automatically closed after the indented block after the with has finished execution: 
'''
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)