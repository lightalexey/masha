for i in range(10**9, 10**9+1000):
    flag=True
    for a in range (2, int(i**0.5)+1):
        if i%a==0:
            flag=False
            break
    if flag:
        print(i)
