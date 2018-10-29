l = []
for a in range(2000,3200):
    if a%7 == 0 and a%5 != 0:
        l.append(str(a))
print ','.join(l)

