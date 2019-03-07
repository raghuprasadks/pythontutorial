# https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial
# match
import re
pattern = "Cookie"
sequence = "Cookie is a Cookie"
if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")
# r raw string literal
import re
pattern = r"Cookie"
sequence = "Cookie"
print(re.match(pattern, sequence))

#Wild Card Characters: Special Characters
# .- A period. Matches any single character except newline character.
#The group() function returns the string matched by the re.

print(re.search(r'Co.k.e', 'Cookie').group())
# 'Cookie'
# \w - Lowercase w. Matches any single letter, digit or underscore.
print(re.search(r'Co\wk\we', 'Cookie').group())
# 'Cookie'
# \W - Uppercase w. Matches any character not part of \w (lowercase w).
print(re.search(r'C\Wke', 'C@ke').group())

#print(re.search(r'C\Wke', 'C@ke').group())
# 'C@ke'
# \s - Lowercase s. Matches a single whitespace 
#character like:space, newline, tab, return.

print(re.search(r'Eat\scake', 'Eat cake').group())

# 'Eat cake'
# \S - Uppercase s. Matches any character not part of \s (lowercase s).

print(re.search(r'Cook\Se', 'Cookie').group())
# \t - Lowercase t. Matches tab.
# 'Cookie'
print(re.search(r'Eat\tcake', 'Eat  cake'))
# 'Eat\tcake'
#\n - Lowercase n. Matches newline.
#\r - Lowercase r. Matches return.
#\d - Lowercase d. Matches decimal digit 0-9.

re.search(r'c\d\dkie', 'c00kie').group()

#'c00kie'
#^ - Caret. Matches a pattern at the start of the string.
re.search(r'^Eat', 'Eat Eat cake').group()
#'Eat'
#$ - Matches a pattern at the end of string.

print(re.search(r'cake$', 'Eat cake').group())
#'cake'
#[abc] - Matches a or b or c.
#[a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).
# Characters that are not within a range can be matched by complementing the set.
# If the first character of the set is ^,
# all the characters that are not in the set will be matched.
print(re.search(r'Number: [0-6]', 'Number: 5').group())
# 'Number: 5'
# Matches any character except 5
print(re.search(r'Number: [^5]', 'Number: 0').group())

#'Number: 0'
#\A - Uppercase a. Matches only at the start of the string. 
#Works across multiple lines as well.

print(re.search(r'\A[A-E]ookie', 'Cookie').group())
#'Cookie'
#\b - Lowercase b. Matches only the beginning 
#or end of the word.
print(re.search(r'\b[A-E]ookie', 'Cookie').group())
#'Cookie'
#\ - Backslash. If the character 
# following the backslash is a
# recognized escape character,
# then the special meaning of the term is taken.
# For example, \n is considered as newline.
# However, if the character following the \ is not a recognized
# escape character, then the \ is treated like any other character
# and passed through.

# This checks for '\' in the string instead of '\t' due to the '\' used
print(re.search(r'Back\\stail', 'Back\stail').group())
#'Back\\stail'
# This treats '\s' as an escape character because it lacks '\' at the start of '\s'
print(re.search(r'Back\stail', 'Back tail').group())
#'Back lash'
#Repetitions
#It becomes quite tedious if you are looking to find long patterns in a sequence.
# Fortunately, the re module handles repetitions using the following
#  special characters:

#+ - Checks for one or more characters to its left.

print(re.search(r'Co+kie', 'Cooookie').group())
#'Cooookie'

#* - Checks for zero or more characters to its left.

print(re.search(r'Ca*o*kie', 'Caokie').group())

#'Caokie'

#? - Checks for exactly zero or one character to its left.

# Checks for exactly zero or one occurrence of a or o or both in the given sequence
print(re.search(r'Colou?r', 'Color').group())

#'Color'

# check for exact number of sequence repetition

#For example, checking the validity of a phone number in an application.

# {x} - Repeat exactly x number of times.

# {x,} - Repeat at least x times or more.

# {x, y} - Repeat at least x times but no more than y times.

print(re.search(r'\d{9,10}', '0987654321').group())

#Groups and Grouping using Regular Expressions

email_address = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', email_address)
if match:
  print(match.group()) # The whole matched text
  print(match.group(1)) # The username (group 1)
  print(match.group(2)) # The host (group 2)


#support@datacamp.com
#support
#datacamp.com

# Greedy vs Non-Greedy Matching

# When a special character matches as much of the search sequence (string)
# as possible, it is said to be a "Greedy Match".
# It is the normal behavior of a regular expression
# but sometimes this behavior is not desired:

heading  = r'<h1>TITLE</h1>'
re.match(r'<.*>', heading).group()
#'<h1>TITLE</h1>'

heading  = r'<h1>TITLE</h1>'
re.match(r'<.*?>', heading).group()

#'<h1>'

# search() versus match()
#The match() function checks for a match only at the beginning of the string
# (by default)
# whereas the search() function checks for a match anywhere in the string.

#findall(pattern, string, flags=0)
#Finds all the possible matches in the entire sequence and
# returns them as a list of strings. Each returned string represents one match.

email_address = "Please contact us at: support@datacamp.com, xyz@datacamp.com"

#'addresses' is a list that stores all the possible match
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)
for address in addresses:
    print(address)

# support@datacamp.com
# xyz@datacamp.com
'''
sub(pattern, repl, string, count=0, flags=0)
This is the substitute function. 
It returns the string obtained by replacing or substituting the 
leftmost non-overlapping occurrences of pattern in string by the 
replacement repl. If the pattern is not found then the string is returned 
unchanged.
'''

email_address = "Please contact us at: xyz@datacamp.com"
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'support@datacamp.com', email_address)
print(new_email_address)

#Please contact us at: support@datacamp.com

'''
compile(pattern, flags=0)
Compiles a regular expression pattern into a regular expression object. 
When you need to use an expression several times in a single program, using the compile() function to save the resulting regular expression object for reuse is more efficient. 
This is because the compiled versions of the most recent patterns passed to compile() and the module-level matching functions are cached.
'''

pattern = re.compile(r"cookie")
sequence = "Cake and cookie"
pattern.search(sequence).group()
#'cookie'
'''
# This is equivalent to:
re.search(pattern, sequence).group()
'''