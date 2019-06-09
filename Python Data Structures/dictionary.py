# Dictionary are best for counting stuff

# A bag of values, each with its own label

# Dictionary allows you to do fast database like operation

# List index their entries based on the position in the List
# Dictionary are like bags, they don't have order
# you store every values with a lookup tage

color = dict()  # {} will also do

color['blue'] = 12
color['india'] = "win"
color['red'] = 36
color['red'] = 36
print(color)
print('\n')

cricket = {'India':358, 'Australia':123}
for team in cricket:
    print(f"Team names : {team} with score {cricket[team]}")

# humans are good when they can see the data, which computers are good when data is not seen

if 'India' in cricket:
    print('True')

# get() method. Both piece of code does the same thing
# 1
counts = dict()
names = ['divya', 'bariya', 'sumit']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# 2
counts = dict()
names = ['divya', 'bariya', 'sumit', 'bariya', 'sumit']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# keys in Dictionary
for key in counts:
    print(f"{key} : {counts[key]}")

# converting dict to list only copies the 'keys' not the 'values'
temp = list(counts)
print(temp)

# prints only keys, values and items seperately
print(counts.keys())
print(counts.values())
print(counts.items())

# accessing keys and values in 'for' look
for key, value in counts.items():   # sequence should not be altered
    print(key, value)
