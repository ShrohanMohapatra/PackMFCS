size = 50
dynamicProg = [[0 for k in range(size)] for m in range(size)]
def ackermannFunction(m, n):
    print('Entering the function with the following parameters->',m,',',n)
    if dynamicProg[m][n] == 0:
        if m == 0: dynamicProg[m][n] = n+1
        elif n == 0: dynamicProg[m][n] = ackermannFunction(m-1,1)
        else:
            dynamicProg[m][n] = ackermannFunction(m-1, 
            ackermannFunction(m,n-1)
            )
    return dynamicProg[m][n]
for k in range(3):
    for m in range(3):
        print('DynamicPBacker (',k,',',m,') ->',dynamicProg[k][m])
        print('FunctionBacker (',k,',',m,') ->',ackermannFunction(k,m))
