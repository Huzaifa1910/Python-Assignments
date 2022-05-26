a = [3,5,1,2,4]
for i in range(len(a)):
    for j in range(len(a)):
        if(a[i]>a[j]):
            x=a[i]
            a[i]=a[j]
            a[j]=x
print(a)
