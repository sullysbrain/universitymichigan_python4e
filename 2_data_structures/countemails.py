fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
emailList = list()

for lines in fh :
    if "From: " in lines :
        words = lines.split()
        email = words[1]
        emailList.append(email)
        print(email)
        count = count + 1
    else :
        continue
print("There were", count, "lines in the file with From as the first word")
