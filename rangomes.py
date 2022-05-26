import random
randoms = [[],[],[],[],[],[],[],[],[],[]]
for i in range(10):
	r1 = random.randint(80,99)
	randoms[i].append(r1)
	print(r1)
print("-------------------------------------")
for i in range(10):
	r2 = random.randint(80,105)
	randoms[i].append(r2)
	print(r2)
print("-------------------------------------")
for i in range(10):
	r3 = random.randint(100,140)
	randoms[i].append(r3)
	print(r3)
print(randoms)
##sample = [[88, 82, 140], [92, 88, 127], [90, 104, 129], [91, 82, 119], [86, 103, 110], [89, 96, 114], [90, 84, 101], [97, 95, 140], [80, 87, 124], [86, 88, 132]]
##popsum = 0
##for i in range(len(sample)):
##    pop = sum(sample[i])
##    popsum += pop
##meaned = popsum/30
##sample2 = []
##sample3 = []
##for i in range(len(sample)):
##    for j in range(len(sample[0])):
##        sample2.append(sample[i][j])
##        sample3.append((sample[i][j])**2)
##print(sample2)
##s1 = (sum(sample2)/30)**2
##s2 = sum(sample3)/30
##sDPop = (s2 - s1)**0.5
##print(sDPop)
##sample = [['90', '150', '200'],
##['95', '170', '180'],
##['102', '180', '150'],
##['100', '120', '220'],
##['80', '186', '110'],
##['60', '144', '140'],
##['85', '128', '170'],
##['91', '190', '198'],
##['72', '110', '212'],
##['98', '156', '250']]
##sampled = []
##for i in range(len(sample)):
##    sm = []
##    for j in range(len(sample[0])):
##           s = int(sample[i][j])
##           sm.append(s)
##    sampled.append(sm)
##print(sampled)
