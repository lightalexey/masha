s='0123456789ABC'
a=0
for i in range(len(s)+1):
    if (int('4C'+s[i-1]+'4', 15)+int(s[i-1]+'62A', 13))%121==0:
        print((int('4C'+s[i-1]+'4', 15)+int(s[i-1]+'62A', 13))//121)
        break
# 2
for i in '0123456789ABC':
    if (int('4C'+i+'4', 15)+int(i +'62A', 13))%121==0:
        print((int('4C'+i+'4', 15)+int(i+'62A', 13))//121)
        break