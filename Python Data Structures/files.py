# Newline is one character not 2 character

# stuff = 'X\nY'
# print(stuff)
#
# print(len(stuff))

# 'file_handle' is not data, its a way to get the data
# A file handle open for read can be treated as a 'sequence' of strings where each line in the file is a string in the sequence
# we can use 'For' loop to iterate through 'sequence'
# Remember : a 'sequence' is an 'ordered set'

# read all the lines
file_handle = open('/Users/divyapatel/Github/Python-Programming-Practise/Python Data Structures/test.txt')
count = 0
for line in file_handle:
    count = count + 1
print(f"Total lines : {count}")


# read all the character
file_handle.seek(0)
inp = file_handle.read()
print(f"Length of character : {len(inp)}")
print(f"Few characters : {inp[102:138]}")

# print statement adds a 'newline' to each lines
for line in file_handle:
    line = line.rstrip()
    if line.startswith('Call'):
        print(line)



fname = input("Enter the file name : ")
try:
    fhand = open(fname)
except:
    print("File '{0}' cannot be open !!".format(fname))
    quit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('Call'):
        continue
    print(line)

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be opened !!")
    quit()

num = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    num = num + float(line[20:26])
    count = count + 1
final = num / count
print("Average spam confidence: {0:.12f}".format(final))
