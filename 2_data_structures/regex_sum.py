import re
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1564273.txt"
    # name = "regex_sum_42.txt"
handle = open(name)
sum = 0
for line in handle:
    strnum = re.findall('[0-9]+', line)
    if len(strnum) != 0:
        for n in strnum:
            inum = int(n)
            sum = sum + inum
print("Sum is: ", sum)
