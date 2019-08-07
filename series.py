n=int(raw_input())
even=0
odd=0
if(n%2==0):
    even=1
    index=n/2
else:
    odd=1
    index=n/2+1
listodd=[]
listeven=[]
if(even):
    for i in range(0,index):
        evenvalue=i*6
        listeven.append(evenvalue)
    popvalue=listeven.pop()
    print(popvalue)
else:
    for i in range(0,index):
        oddvalue=i*7
        listodd.append(oddvalue)
    popvalue=listodd.pop()
    print(popvalue)


#this is just a comment
