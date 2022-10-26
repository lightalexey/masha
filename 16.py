n = int(input())
ss = int(input())
s = ''
#while n % ss != n:
#    s = s + str(n % ss)
#    n = n // ss
#s = s + str(n)
#print(s[::-1])

#while n != 0:
#   s = str(n % ss)+'.' + s
#   n = n // ss
#s=s.replace('10', 'A')
#s=s.replace('11', 'B')
#s=s.replace('12', 'C')
#s=s.replace('13', 'D')
#s=s.replace('14', 'E')
#s=s.replace('15', 'F')
#s=s.replace('.', '')
#print(s)

#1 способ - replace
#2 способ alphabet = '0123456789ABCDEF'

alph='0123456789ABCDEF'
while n != 0:
   s =alph[(n % ss)-1] + s
   n = n // ss
print(s)


