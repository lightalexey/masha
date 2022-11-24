for a in range(1, 10**9+1):
    sum=0
    for i in range(1, a//2+1):
        if a%i==0:
            sum+=i
            if sum>a:
                break
    if sum==a:
        print(a)