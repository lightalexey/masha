f = open('17.txt')
s = f.read().split()
for i in range(len(s)):
    s[i] = int(s[i])
print(sum(s))
f.close()
# ------------------------------------ 2 способ ------------------------
f = open('17.txt')
a = []
for i in range(5000):
    s = int(f.readline())
    a.append(s)
print(sum(a))
f.close()
# ------------------------------------ 3 способ ------------------------
# f = open('17.txt')
a = [int(i) for i in open('17.txt')]
print(sum(a))
# close() ???