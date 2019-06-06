# there are 2 things you can do in String
# 1. Iteration using 'For loop'

text = 'divya'
for character in text:
    print(character)

# 2. Slicing using colon (:) operator

text[1:3]
text[1:]    # till last character
text[:3]    # from starting character
text[2:50]  # This will not give error even if the word is small and you are slicing till 50 character

# Input function accepts user data into 'String'
# so you have to explicitly convert to other data-type

# 'in' operator is very important operator
# It returns True / False
if 'v' in text:
    print("V is present in Divya")

new = text.lower() # This does not change the value of the original variable
new = text.upper()

dir(text)   # list downs all the function available to a data-type

pos = text.find('v',1)  # returns the index, returns '-1' if not found

text.lstrip()   # removes 'spaces' from the string
text.rstrip()
text.strip()    # from both side

text.startwith(text)    # returns True / False

# in Python3, strings and unicode are same
