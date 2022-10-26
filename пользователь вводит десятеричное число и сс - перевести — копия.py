n = int(input())
ss = int(input())
s = ''
#while n % ss != n:
#    s = s + str(n % ss)
#    n = n // ss
#s = s + str(n)
#print(s[::-1])

while n != 0:
    s = str(n % ss) + s
    n = n // ss
print(s)

1 способ - replace
2 способ alphabet = '0123456789ABCDEF'