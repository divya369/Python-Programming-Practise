#  8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#  You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#  Hint: make sure not to include the lines that start with 'From:'.

# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
# try:
#     fh = open(fname)
# except:
#     print("File cannot be opened !!")
#
# count = 0
# for line in fh:
#     line = line.rstrip()
#     if line.startswith('From '):
#         stuffs = line.split()
#         print(stuffs[1])
#         count = count + 1
# print("There were", count, "lines in the file with From as the first word")



# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program
# looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program
# reads through the dictionary using a maximum loop to find the most prolific committer.

# name = input("Enter file:")
name = "/Users/divyapatel/Github/Python-Programming-Practise/Python Data Structures/mbox-short.txt"
# if len(name) < 1 : name = "mbox-short.txt"
# try:
#     handle = open(name)
# except:
#     print("File cannot be opened !!")
#
# emails = dict()
# for line in handle:
#     line = line.rstrip()
#     if line.startswith('From'):
#         words = line.split()
#         emails[words[1]] = emails.get(words[1], 0) + 1
#
# final_email = None
# final_email_count = 0
# for key, value in emails.items():
#     if final_email is None or final_email_count < value:
#         final_email_count = value
#         final_email = key
#
# print("{0} {1}".format(final_email, final_email_count))


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
	handle = open(name)
except:
    print("File cannot be opened !!")

lst = list()
for line in handle:
    line = line.rstrip()
    if line.startswith('From') and len(line) > 40:
        words = line.split()
        word = words[5]
        num = word[:2]
        lst.append(num)

di = dict()
new_list = list()
for item in lst:
    di[item] = di.get(item, 0) + 1

for key, value in di.items():
    temp = (key, value)
    new_list.append(temp)

new_list = sorted(new_list)

for k,v in new_list:
    print(k,v)
