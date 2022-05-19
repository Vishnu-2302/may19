import math
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
s=0
for i in p:
    s=i+s
print(s)
