import random

ran27 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

for i in range(0,3):
    spaces = random.sample(range(0, 9), 4)
    for j in range(0, 4):
        ran27[i][spaces[j]] =-1

print(ran27)

for i in range(0,9):
    print("i"+str(i))
    count = 0
    for j in range(0,3):
        print("j"+str(j))
        if(ran27[j][i]==0):
            count = count+1
    if(i==0):
        col = random.sample(range(1,10), count)
    elif(i==8):
        col = random.sample(range(80,91), count)
    else:
        col = random.sample(range(i*10,i*10+10 ), count)
    col.sort()
    print(col)
    k=0
    skip=0
    while(k!=len(col)):
        #print(k)
        #print("skip"+str(skip))
        if(ran27[k+skip][i]==0):
            print("GGG")
            ran27[k+skip][i]=col[k]
            k=k+1
            print(ran27)
        else:
            skip=skip+1
            #print("skip"+str(skip))

print(ran27)
