# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    nmbPos = line.find(': ')
    nmbStr = line[nmbPos+2:].rstrip()
    total = total + float(nmbStr)
    avg = float(total) / count
print("Average spam confidence:", avg)