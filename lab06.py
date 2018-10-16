fp = open( "scores.txt" )

firstlist = []
secondlist = []
for num in fp:
    
    name = num[0:20].strip()
    splitit = num.split()
    examscores = [int(x) for x in splitit[2:]]
    average = sum(examscores)/4
    tup = name, examscores, average
    firstlist.append(tup)
firstlist.sort()

#format from pdf 
print(firstlist)
fp.close()