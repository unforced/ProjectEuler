stringList = []
with open('euler18.txt') as f:
    for line in f:
        stringList.append(line.rstrip('\n'))

numList = []
for s in stringList:
    numList.append(s.split())

max_sum = 0

def find_max():
    global max_sum
    for x in range(len(numList)-3):
        for y in range(len(numList[x])):
            find_sum(x, y, 0, 0)
    return max_sum

def find_sum(row, num, sum):
    global max_sum
    tempSum = sum
    tempSum += int(numList[row][num])
    if tempSum > max_sum:
        max_sum = tempSum
    if row == len(numList)-1:
        print max_sum
    else:
        find_sum(row+1, num+1, tempSum)
        find_sum(row+1, num, tempSum)
  
    
