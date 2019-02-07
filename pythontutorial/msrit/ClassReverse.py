# -*- coding: utf-8 -*-
class sentenceR:
    vowels=["a","e","i","o","u"]
    vowelCount=0
    sentence=""
    reverse=""


    def __init__(self,sentence):
        self.sentence=sentence
        self.reversesentence()

    def reversesentence(self):
        self.reverse=" ".join(reversed(self.sentence.split()))
    '''
    def getvowelCount(self):
        self.vowelCount = sum (s in self.vowels in s in self.sentence.lower())
        return self.vowelCount
    ''' 
    def getReverse(self):
        return self.reverse
    
items=[]
    
for i in range(3):
   sentence=input("Enter the phrase:")
   reverser=sentenceR(sentence.strip())
   items.append(reverser)
    
   SortedItems=sorted(items,key =lambda item: item.getvowelCount(),reverse=True)
    
   print("Sorted on vowel count(descending)\n")
    
   for i in range(len(SortedItems)):
       print("Reverse:"+ SortedItems[i].getReverse()+"vowel count:",SortedItems[i].getvowelCount())
