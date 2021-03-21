times = 4
# count=0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    testingNumber = a*10000+b*1000+c*100+d*10+e
                    if (a*10000+b*1000+c*100+d*10+e)*times == e*10000+d*1000+c*100+b*10+a:
                        print(str(a)+str(b)+str(c)+str(d)+str(e))
                        print(a+b+c+d+e)
                        # count = count+ 1
                        # print(count)
