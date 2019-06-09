# List constants are surrounded by [] square brackets and the elements in the list are seperated by comma (,)

# List elements can be any other python OBJECT, even another list or collection

# A list can be empty

# List are mutable ( values in list can be changed ) but strings are not mutable

# Range function returns a 'list'

friends = ['divya', 'shyam', 'Samanvay', 'bhagat']
print(friends)
print(len(friends))
print(range(len(friends)))

for friend in friends:
    print(friend)
print("\n")

# counted loop
for i in range(len(friends)):
    if i%2==0:
        print(friends[i])

# List concatenate
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# slicing in list : remember like string, the second number is "up to but not including"
print(friends[:3])

# print(dir(friends))

# creating an empty List and using 'append' method
# List items stays in 'order' and new elements are added at the end of the list

stuff = list()
stuff.append(369)

# 'in' and 'not in' operator used to check item in List
"divya" in friends

# sorting in list
# Python uses an algorithm called 'Timsort' : Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort
friends.sort()
print(friends)

# 2 approch : Only difference is the use of memory

total = 0
count = 0
while True:
    inp = input("Enter a number : ")
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total/count


numlist = list()
while True:
    inp = input("Enter a number : ")
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)

# 'split' method on string returns a List of strings
abc = "I am gonna complete my masters from IIT Bombay !!"
stuff = abc.split()
print(stuff)

# you can use 'find()' method followed by slicing or 'split()' method to get string data
