import csv
import math
with open("sdhw.csv", newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
data=[]
for b in filedata:
    data.append(b[1])
def mean(data):
    n=len(data)
    total=0
    for x in data:
        print(x)
        total=float(total)+float(x)
    mean=total/float(n)
    print(mean)
    return mean

sqlist=[]
for mark in data:
    a=float(mark)-float(mean(data))
    a=a**2
    sqlist.append(a)

sum=0
for i in sqlist:
    sum=sum+i

print(sum)

result=float(sum/len(data)-1)
sd=math.sqrt(result)
print(sd)