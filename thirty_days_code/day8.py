# Enter your code here. Read input from STDIN. Print output to STDOUT
"""Read n names+phone numbers, store in a dictionary.  When prompted with a
name, print 'name=PHONENUMBER'"""

total = int(raw_input())
phonebook = {}
for i in range(total):
    person, number = raw_input().split()
    phonebook[person] = number

while True:
    name = raw_input()
    if name in phonebook:
        print "%s=%s" %(name, phonebook[name])
    else:
        print "Not found"