

f = open("P-1000000.txt","r")
myList = []
for line in f:
    myList.append(line)
print(myList[0])
print(myList[1])


for i in myList:
  print i
