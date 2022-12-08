a=9**8+3**5-9
a1=''
while a>0:
    a1=str(a%3)+a1
    a=a//3
print(a1.count('2'))

a=9**8+3**5-9
count=0
while a>0:
    if a%3==2:
        count+=1
    a=a//3
print(count)
