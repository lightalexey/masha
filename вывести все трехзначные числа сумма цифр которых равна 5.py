c = 0
for i in range(100, 1000):
    if i // 100 + i % 10 + i // 10 % 10 == 5:
        c += 1
        print(i, end=' ')
print()
print(c)
