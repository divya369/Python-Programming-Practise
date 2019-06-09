# limited version of list

# String and Tuple are not mutable

# you cannot .append() nor .sort() nor .reverse() on Tuple

tup = tuple()
# print(dir(tup))

# Tuples are simpler and more efficient in terms of memory use and performance than list. Tuples are prefer to make 'temporary variables'

# We can put tuples on left hand side as well. If there is a tuple on left-hand side then it expects tuple on right-hand side as well. Otherwise it
# will give you error.
(a, b) = (99, 88)
print(a,b)

# The comparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the next element, and so on, until
# it finds elements that differ
print(('Divya', 369) > ('Divya', 123))  # prints true

# 'sorted()' is used to sort the dictionary in 'key' order
di = {'a':1, 'c':145, 'b':99}
for k,v in sorted(di.items()):
    print(k,v)
print(di)

# sorting by values instead of keys

temp = list()
for k,v in di.items():
    temp.append((v,k))
print(temp)
temp = sorted(temp)
print(temp)



# Top 5 most common words

fhand = open('temp.txt')
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for val, key in lst[: 10]:
    print(key, val)


# List Comprehension : Creates a 'dyanamic' list.

c = {'a':10, 'b':1, 'c':22}
print(sorted( [ (v,k) for k,v in c.items() ] ))
