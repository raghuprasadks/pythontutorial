fname = input("Enter file name: ")
l = input("Enter letter to be searched:")
k = 0

with open(fname, 'r') as f: # f = open(fname,'r')
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter == l):
                    k = k + 1
print("Occurrences of the letter:")
print(k)