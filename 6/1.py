count = 0
for x in range(1, 10):
    for y in range(1, 10):
        if -3 ** (-0.5) * x + 10 > y > 3 ** (-0.5) * x:
            count += 1
print(count)
