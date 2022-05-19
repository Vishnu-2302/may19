import math
t=int(input())
for q in range(t):
    h=int(input())
    sieve=[True]*h
    s=int(math.sqrt(h))
    sieve[0]=sieve[1]=False
    for i in range(2,s+1):
        if sieve[i]:
            for j in range(i*i,h,i):
                sieve[j]=False
    p=[]
    for i in range(h):
        if sieve[i]:
            p.append(i)
    c=0
    for i in p:
        for j in p:
            if i+j==h:
                c+=1
    if c>0:
        print('Deepa')
    else:
        print('Arjit')