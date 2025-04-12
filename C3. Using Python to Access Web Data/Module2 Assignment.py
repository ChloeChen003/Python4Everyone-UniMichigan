#module 2 assignment 
import re 

filename = input('Enter file name: ')
handle = open(filename)
sum = 0
for line in handle:
  numbers = re.findall('[0-9]+',line)
  if not numbers:
    continue
  else:
    for num in numbers:
      sum += int(num)
print(sum)