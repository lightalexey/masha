a=[13, 47, 3, 4, -10, 9, 0, -5, 17, -7]
print(len(a), a[0], a[-1])
summ=0
summ1=0
count=0
for i in a:
    if i>0:
        summ1+=i
        count+=1
    summ+=i
print(summ, summ1/count)
summ=0
for i in range(len(a)):
    summ+=a[i]
print(summ)
print(sum(a))
mult=1
count0=0
for i in a:
    if i!=0:
        mult*=i
    else:
        count0+=1
print(mult, count0)
print(sum(a)/len(a))
for i in a:
    print(i, end=' ')
print()
print(a)
print(*a)
amax=a[1]
imax=1
s=0
for i in a:
    if i>amax:
        amax=i
        imax=s
    s+=1
print(amax, imax)
amax=a[1]
imax=1
for i in range(len(a)):
    if a[i]>amax:
        amax=a[i]
        imax=i
print(amax, imax)