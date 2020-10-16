#Finding the sum of integers present in regex_sum_957983.txt file using REGEX expression

import re 
handler = open('regex_sum_957983.txt')
numList = list()
for line in handler:
    line = line.rstrip()
    integersList = re.findall('[0-9]+', line)
    #eliminate empty arrays
    if len(integersList) < 1 : continue 
    #extract integers in a new list
    for item in integersList:
        integer = int(item)
        numList.append(integer)
print('ToTal Sum :', sum(numList))