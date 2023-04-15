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

# Repetition

print('Date{dd-mm-yyyy}', re.search(r'[\d]{2}-[\d]{2}-[\d]{4}', '15-04-2023'))

# Repetition changes.  Consider a scenario where both three digits, as well as four digits, are accepted

print('Three Digit', re.search(r'[\d]{3,4}', '123'))
print('Four Digit', re.search(r'[\d]{3,4}', '1234'))
# Minimum is 3 digit and max is 4 digits
print('Four Digit', re.search(r'[\d]{3,4}', '12'))

# Open ended ranges. We define something called start and no ending, or end and no beginning

print('Open ended range', re.search(r'\d{2,}', '5th Floor, A-118,\
                Sector-100, Bangalore, Kar - 560048'))

print('Open Ended all', re.findall(r'\d+', '5th Floor, A-118,\
                Sector-100, Bangalore, Kar - 560048'))

# Shorthand. Shorthand characters allow you to use + character to specify one or more ({1,})
# and * character to specify zero or more ({0,}

# Below Symbols can be used, only if we need to match characters starting from 0 or 1 to many. Not for 2 matching chars
# to many
print('Shorthand', re.search(r'\d*', '5th Floor, A-118,\
                Sector-100, Bangalore, Kar - 560048'))

print('Shorthand', re.search(r'\d+', '5th Floor, A-118,\
                Sector-100, Bangalore, Kar - 560048'))

# Grouping the expressions
# Return entire match using group()
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})', '15-04-2023')
print(grp)
print('return entire match', grp.group())
print('Return Tuple of matches', grp.groups())
print('Retrieve a single group', grp.group(2))

# Name our groups

grp1 = re.search(r'(?P<dd>\d{2})-(?P<mm>\d{2})-(?P<yyyy>\d{4})', '15-04-2023')
print(grp1)
print('As a dictionary', grp1.groupdict())
print('Retrieve Using group name', grp1.group('mm'))

# LookAhead. In the case of a  negated character class, it won’t match if a character is not present to check against
# the negated character. We can overcome this case by using lookahead; it accepts or rejects a match based on the
# presence or absence of content.

# Below is like, n followed by e should not present. it can match anything like Pythonc, nr, na etc.
# If no character present after the n . then also it won't match anything
print('negation:', re.search(r'n[^e]', 'Python'))

# This one is opposite to the above. If no character present after the n, then also it matches only n
# Suppose if the sting is na it still matches only n. it is like n followed by e should not be present
print('lookahead:', re.search(r'n(?!e)', 'Python'))

# it is like n followed by e should be present. other chars it will give None. Even if there are no chars after n
# present
print('lookahead:', re.search(r'n(?=e)', 'Python'))

# Substitution
# it requires the regular expression, the replacement string, the source string being searched

print(re.sub(r'(\d{4})-(\d{4})-(\d{4})-(\d{4})',r'\1\2\3\4',
             '1111-2222-3333-4444'))

# Compile
# The Python regular expression engine can return a compiled regular expression(RegEx) object using compile function.
# This object has its search method and sub-method, where a developer can reuse it when in need.

regex = re.compile(r'([\d]{2})-([\d]{2})-([\d]{4})')
print('compiled reg expr', regex.search('26-08-2020'))
print(regex.sub(r'\1.\2.\3', '26-08-2020'))