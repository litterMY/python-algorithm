sortList = [5,4,3,2,1,7,9,8,22,11]

for i in range(1,len(sortList)):
    v=i-1
    temp = sortList[i]
    while v>-1 and sortList[v]>temp:
        sortList[v+1]=sortList[v]
        v-=1
    sortList[v+1]=temp

print(sortList)
    