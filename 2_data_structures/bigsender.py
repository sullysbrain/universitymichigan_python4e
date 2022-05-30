name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hours = dict()

for line in handle:
    if "From " in line:
        words = line.split()
        time = words[5]
        timeparts = time.split(":")
        hour = timeparts[0]
        hours[hour] = hours.get(hour,0) + 1

sortedhours = sorted( [ (k,v) for k,v in hours.items() ] )
# print(sortedhours)
for k,v in sortedhours:
    print(k, v)
