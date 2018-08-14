i=2
s=0
n=2
for i in range(2,101):
    for n in range(2,i):
        if (i%n==0):
            break
    else:
        s+=i
print(s)
