for i in range(1,10):
    for j in range(1,i+1):
        print(j,'x',i,'=',i*j,end=' ')
        if i==j:
            print(' ')#这里是为了输出换行的
        
