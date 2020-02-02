import random
variations=[]

var = 0
while(var!=30):
    fullcard=[]

    for i in range(6):
        b=[]
        for j in range(3):
            a=[]
            for k in range(9):
                a.append(0)
            b.append(a)
        fullcard.append(b)
    
    count=[0,0,0,0,0,0,0,0,0]
    for i in range(6):
        for j in range(3):
            spaces = random.sample(range(0, 9), 4)
            for k in range(4):
                fullcard[i][j][spaces[k]]=-1
    #print(fullcard)
    for i in range(6):
        for j in range(3):
            for k in range(9):
                if(fullcard[i][j][k]==-1):
                    count[k]+=1
    
    if(count==[9,8,8,8,8,8,8,8,7]):
        variations.append(fullcard)
        var+=1

print(variations)

