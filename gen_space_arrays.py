import random
variations=[]

var = 0
while(var!=10):
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
        while(True):
            #print("i:"+str(i))
            fullcard[i]=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
            breaked=False
            #print("A")
            for j in range(3):
                spaces = random.sample(range(0, 9), 4)
                #print("b")
                for k in range(4):
                    fullcard[i][j][spaces[k]]=-1
            #print(fullcard[i])
            for j in range(9):
                #print("j:"+str(j))
                countspaces=0
                for k in range(3):
                    #print("k:"+str(k))
                    if(fullcard[i][k][j]==-1):
                        countspaces+=1
                        #print("countspaces:"+str(countspaces))
                #print(countspaces)
                if(countspaces==3):
                    #print("breaked")
                    breaked=True
                    break
            if(breaked):
                #print("e")
                continue
            else:
                #print("else")
                break
            #print("f")
                

    #print(fullcard)
    for i in range(6):
        for j in range(3):
            for k in range(9):
                if(fullcard[i][j][k]==-1):
                    count[k]+=1

    if(count==[9,8,8,8,8,8,8,8,7]):
        print("added")
        variations.append(fullcard)
        var+=1

print(variations)

