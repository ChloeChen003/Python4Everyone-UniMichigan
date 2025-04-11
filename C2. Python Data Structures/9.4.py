name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}
for line in handle:
    if line.startswith('From '):
                       words = line.split()
                       sender = words[1]
                       counts[sender]=counts.get(sender, 0) +1
MPC = None
max_count = 0
for sender, count in counts.items():
    if count > max_count:
        max_count = count
        MPC = sender
    
print(MPC, max_count)
