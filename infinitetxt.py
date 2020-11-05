file=open('pass.txt','w+')
i=0
x=0
while True:
    i+=1
    for x in range(100000):
        aux= 'aaaa'
        file.write(aux*x)
        #print(x)
        if i==0:
            x+=1
            aux2=str(x)+'.txt'
            file=open(aux2,'w+')
