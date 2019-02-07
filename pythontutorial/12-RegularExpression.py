#Regular expression

#\d
#Matches any decimal digit; this is equivalent to the class [0-9].
#\D
#Matches any non-digit character; this is equivalent to the class [^0-9].
#\s
#Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
#\S
#Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
#\w
#Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
#\W
#Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].


#"^": This expression matches the start of a string
#"w+": This expression matches the alphanumeric character in the string
'''
import re
xx = "India is a great country.India got independance in 1947.Current $ value is INR 68." \
     "It become republic in 1956"
#xx="2012 Kaushalya skill upskill and reskill 2017"
r1 = re.findall(r"^\w+",xx)
r2 = re.findall(r"\W+",xx)
r3 = re.findall(r"\d+",xx)
r4 = re.findall("India",xx)
print("Regular Expression 1",r1)
print("Regular Expression 2 ",r2)
print("Regular Expression 3 ",r3)
print("Regular Expression 4 ",r4)

#Split
import re
xx = "Kaushalya,education is fun"
r1 = re.findall(r"^\w+", xx)
print('reg expression ',r1)
print (re.split(r'\s','we are splitting the words'))
print (re.split(r's','split the words'))


# Search

import re

list = ["guru99 get guru", "guru99 give", "guru Selenium"]
for element in list:
    z = re.match("(g\w*)\W(g\w*)", element)
    if z:
        print('match ',(z.groups()))



import re
patterns = ['software testing', 'guru99']
text = 'software testing is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text))
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')


import re
abc = 'guru-99@google.com, careerguru99hotmail.com, users@yahoomail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:
    print(email)

'''
#Flags
import re
xx = """guru99 
careerguru99	
selenium"""
k1 = re.findall(r"^\w+", xx)
k2 = re.findall(r"^\w+", xx, re.MULTILINE)
print(k1)
print(k2)
