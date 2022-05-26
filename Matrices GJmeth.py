def displayMatrix(M):
    Nr = len(M)
    Nc = len(M[0])
    for r in range(Nr):
        for c in range(Nc):
            print("%10.6f" % (M[r][c]) ,end = "\t")
        print()
    print("--------------------------------")
    return(M)
Nr = int(input("Enter Number of rows:- "))
Nc = int(input("Enter Number of columns:- "))
M = []
for r in range(Nr):
    R = []
    for c in range(Nc):
            Element = float(input("Enter MAtrix element:- "))
            R.append(Element)
    M.append(R)
displayMatrix(M)
Pr = int(input("Enter row number of pivot element:- "))
Pc = int(input("Enter column number of pivot element:- "))
Pr -= 1
Pc -= 1
while (Pr>= 0 or Pc >= 0):
    PivotElement = M[Pr][Pc]
    for c in range(Nc):
        M[Pr][c] = M[Pr][c]/PivotElement
    displayMatrix(M)
    for r in range(Nr):
        if(r==Pr):
            continue
        PivotValue = M[r][Pc]
        for c in range(Nc):
            M[r][c] = M[r][c]-M[Pr][c]*PivotValue
    displayMatrix(M)
    Pr = int(input("Enter row number of pivot element:- "))
    Pc = int(input("Enter column number of pivot element:- "))
    Pr -= 1
    Pc -= 1
