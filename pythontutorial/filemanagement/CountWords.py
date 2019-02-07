fname = input("Enter file name: ")
word = input("Enter word to be searched:")
k = 0

with open(fname, 'r') as f:
    for line in f:
        print(line)
        print(type(line))
        isFound = line.find(word)
        print('is found',isFound)
        if (isFound > -1):
            k = k + 1
        '''
        words = line.split()
        print(words)
        for i in words:
            if (i == word):
                k = k + 1 '''
print("Occurrences of the word:")
print(k)