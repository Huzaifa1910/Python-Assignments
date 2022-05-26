##x = [3,4,100,34,45]
##for i in range(len(x) - 1):
##    if (x[i] > x[i + 1]):
##        x[i + 1], x[i] = x[i], x[i + 1]
##print (x)


## 2 people for 5000 rps
## 3 people for 6000 rps
## 4 people for 7000 rps
## 5 or more people 1500 per person


a = int(input("Kitnay admi hain: ?"))

if (a==2):
    r = 0
    for i in range(a):
        nme = str(input("naam batao: "))
        age = int(input("age b batao: "))
        if (age >=60):
            rn= 1250
        else:
            rn = 2500
        r = rn +r   
    
if (a==3):
    r = 0
    for i in range(a):
        nme = str(input("naam batao: "))
        age = int(input("age b batao: "))
        if (age >=60):
            rn= 1000
        else:
            rn = 2000
        r = rn +r   

if (a==4):
    r = 0
    for i in range(a):
        nme = str(input("naam batao: "))
        age = int(input("age b batao: "))
        if (age >=60):
            rn= 1750/2
        else:
            rn = 1750
        r = rn +r   

if (a>=5):
    r = 0
    for i in range(a):
        nme = str(input("naam batao: "))
        age = int(input("age b batao: "))
        if (age >=60):
            rn= 750
        else:
            rn = 1500
        r = rn +r   

print (r)
    
##    nme1 = str(input("Pehle ka naam batao: "))
##    age1 = int(input("Age b batao: "))
##    nme2 = str(input("doosray ka naam batao: "))
##    age2 = int(input("Age b batao: "))
##    nme3 = str(input("teesray ka naam batao: "))
##    age3 = int(input("Age b batao: "))
##    nme4 = str(input("chothay ka naam batao: "))
##    age4 = int(input("Age b batao: "))
##    r1 = 1750
##    r2 = 1750
##    r3 = 1750
##    r4 = 1750
##    if (age1 >= 60):
##        r1 = r1/2
##    if (age2 >= 60):
##        r2 = r2/2
##    if (age3 >= 60):
##        r3 = r3/2
##    if (age4 >= 60):
##        r4 = r4/2
##    r = r1 + r2 + r3 + r4
