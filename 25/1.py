for i in range(17445700, 17450600):
    s=0
    for a in range(2, i//2+1):
        if i%a==0:
            s+=1
            if s > 2:
                break
    if s==2:
        #print(i)
        for k in range(2, i//2+1):
            if i%k==0:
                print(k, end=' ')
        print()