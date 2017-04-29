"""Read a number of strings from standard input, and for each, print the 
odd indexed characters and then even-indexed characters"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_strs = int(raw_input())
for i in range(num_strs):
    my_str = raw_input()
    odds = ""
    evens = ""
    for index, char in enumerate(my_str):
        if index % 2 == 0:
            evens += char
        else:
            odds += char
    print evens, odds
