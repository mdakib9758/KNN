import math
import operator
f=open(r"C:\Users\akkii\Desktop\knn.txt","r")
dataset=list(f)
for i in range(len(dataset)):
    dataset[i]=dataset[i].split()
    for j in range(len(dataset[i])-1):
        dataset[i][j]=float(dataset[i][j])

train=dataset[:(len(dataset)//10)*6]
check=dataset[(len(dataset)//10)*6:]
dist=[]
d=0
for k in range(len(check)):
    for i in range(len(train)):
        for j in range(len(train[i])-2):
            d=d+pow((train[i][j]-check[k][j]),2)
        d=math.sqrt(d)
        dist.append((train[i],d))
    dist.sort(key=operator.itemgetter(1))
    diab=0
    ndiab=0
    d=0
    for l in range(3):
        a=dist[l][0]
        if(a[4]=="0"):
            diab=diab+1;
        else:
            ndiab=ndiab+1
    if(diab>ndiab):
        check[k].append("0");
    else:
        check[k].append("1");
t=0     
for i in range(len(check)):
    if(check[i][len(check[i])-1]==check[i][len(check[i])-2]):
        t=t+1
    else:
        print("No")
t=(t/len(check))*100
print(train)
print("accuracy",t,'%')
print(check)
print("accuracy",t,'%\n')
print(dist)

