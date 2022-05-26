def mean(liste):
    mean = sum(liste)/len(liste)
    return mean
def median(liste):
    sort = sorted(liste)
    if(len(liste)%2 == 0):
        median = (sort[int(len(liste)/2)]+a[int(len(liste)/2)-1])/2
    if(len(liste)%2 == 1):
        median = (sort[int(len(liste)/2)])
    print("sorted list: ",sort)
    return median
age = int(input("Enter you age:"))
a = []
for i in range(0,10): 
    b = input("Enter Readings: ")
    if(b == ""):
        b = input("Enter Again: ")
    a.append(int(b))
        

print(a)
print("Mean is: ",mean(a))
print("Medain is: ",median(a))

