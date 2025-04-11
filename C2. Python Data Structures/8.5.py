filename = input('Enter the file name: ')
try: 
  fh = open(filename)
except:
  print('File cannot be opened:', filename)
  quit()

count = 0 
for line in fh:
  line = line.rstrip()
  if line.startswith('From:'):
    splitline = line.split()
    print(splitline[1])
    count += 1
print('There were', count, 'lines in the file with From as the first word.')