x = 0
f = 0
c = 0

for z in range (999,0,-1):
    for y in range (999,0,-1):
        if y < f:
            break
        if z*y > x:
            c = 0
            for a in range (0,len(str(z)),1):
                if str(z*y)[a] == str(z*y)[len(str(z*y))-a-1]:
                    c += 1
                    #x = z*y
                    #f = y
                    #break
                else:
                    break
            if c == len(str(z)):
                x = z*y
                f = y

    if z < f:
        break
print (str(x))