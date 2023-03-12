f=open('26_demo.txt')
summ, k = f.readline().split()
summ, k =int(summ), int(k)
a=[]
for i in range(k):
    a.append(int(f.readline()))
a= sorted(a)
summ1=0
count=0
mx=0
for i in range(len(a)):
    summ1+=a[i]
    if summ1>summ:
        break
    count += 1
    mx=a[i]
    #summ1+=a[i]
print(count)
for i in range(count, k):
    if a[i]>mx+summ-summ1-a[count]:
        mx=a[i-1]
print(mx)


