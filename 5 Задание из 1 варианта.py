def R(n):
    if int(str(n)[0]) % 4 == 0:
        return int('9' + str(n)[1:])
    else:
        if int(str(n)[0]) % 2 == 0:
            return int('3' + str(n)[1:])
        else:
            return n

count = 0
for n in range(1000, 10000):
    if str(R(n))[0] == '9' and R(n) % 8 == 4: # oct(R(n))[-1]=='4':
        count += 1
print(count)
