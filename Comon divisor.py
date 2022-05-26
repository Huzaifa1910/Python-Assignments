##x=int(input("Enter a number"))
##k=2
##while (k<=x):
##    d=x%k
##    if (d==0):
##        print(k,"is a divisor")
##    k=k+1
##    
##    
##A = int(input("Enter a number: "))
##i = 2
##if (A>1):
##    while (A>3, int(A/2)+1):
##        if(A%i) == 0:
##            print (A,"is not a prime number")
##            break
##        else:
##            print(A,"is a prime number")
##            break       

## Ques of Prime number
##A = int(input("Enter a number: "))
##if (A>1):
##    for i in range(2, int(A/2)+1):
##        if(A%i) == 0:
##            print (A,"is not a prime number")
##            break
##    else:
##         print(A,"is a prime number")
              
## Common Divisor
##A = int(input("ENTER FIRST NUMBER : "))
##B = int(input("ENTER SECOND NUMBER : "))
##D = 0
##print("Common Divisors of",A,"and",B,"are:")
##for i in range(1,min(A,B)+1):
##  if (A%i == B%i == 0):
##    D = i
##    print(D)
##
##
## Largest Divisor
##A = int(input("ENTER FIRST NUMBER : "))
##B = int(input("ENTER SECOND NUMBER : "))
##D = 0
##print("Largest Divisor of",A,"and",B,"is:")
##for i in range(1,min(A,B)+1):
##  if (A%i == B%i == 0):
##    D = i
##print(D)
##



## GCD from given ALGORITHM

##B = int(input("ENTER LARGER NUMBER : "))
##A = int(input("ENTER SMALLER NUMBER : "))
##
##
##R= B%A
##for i in range (1,A+1):
##    if (R==0):
##        print(A, "is Greatest Common Divisor")
##        break
##    else:
##        B=A
##        A=R

