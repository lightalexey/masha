a='polygn'
count=0
for i in a:
    for b in a:
        for c in 'oy':
            for d in a:
                for e in a:
                    if i+b==e+d: # and c in 'oy': #(c==a[1] or c==a[3]):
                        count+=1
print(count)