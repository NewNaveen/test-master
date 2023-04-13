import re

# Search in re will match only the first match. it skips all other matches
# r in r'portal' stands for raw. not regex.
match = re.search(r'portal', 'GeeksforGeeks: A computer science \
                  portal for geeks')

# print(match)
# print(match.group())
# print('Start Index:', match.start())
# print('End Index:', match.end())

# Search will find only the first matching character or string. Below is called character class
match1 = re.search(r'[Gg]eeks', 'GeeksforGeeks: A computer science \
                  portal for geeks')
print(match1.group())

# This will match if the string is there in beginning of any word
print(re.search(r'\bGe', 'Hello Geeks'))
# this means the word should start and end with the string

print(re.search(r'\bRaju\b', 'Hello Raju'))

# Beginning and end of the string. ^ for beginning and $ for end
# Looks like beginning of the line should have this string
print('Beginning of the String', re.search(r'^Geek', 'Campus Geek of the month'))
print('Beginning of the String', re.search(r'^Geek', 'Geek of the month'))

print('End of the String', re.search(r'Geeks$', 'Compute science portal-GeeksforGeeks'))

# Any char in between or at the . sign
print('Any Character', re.search(r'p.th.n', 'python 3'))

# Optional chars
print('Optional Chars', re.search(r'colou?r', 'color'))
print('Optional Chars', re.search(r'colou?r', 'colour'))
print('Optional Chars', re.search(r'colou?r', 'colouur'))