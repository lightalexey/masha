count=0
for i in range(2456900, 2457570):
    s=0
    count+=1
    for a in range(2, i//2+1):
        if i%a==0:
            s+=1
    if s==0:

        print(count, i)