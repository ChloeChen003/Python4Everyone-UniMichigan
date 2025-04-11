name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}
for line in handle:
    if line.startswith('From '):
        words = line.split()
        time_str = words[5]
        hour = time_str.split(':')[0]
        counts[hour] = counts.get(hour,0)+1
sortedhours = sorted(counts.keys())
for hour in sortedhours:
    print(hour, counts[hour])