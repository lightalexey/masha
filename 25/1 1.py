for i in range(174457, 174506):
    s=0
    for a in range(2, i//2+1):
        if i%a==0:
            s+=1
            if s==1:
                del1=a
            if s > 2:
                break
    if s==2:
        #print(i)
        print(del1, i // del1)