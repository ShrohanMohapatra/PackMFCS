size = 200
print('Just entered the matrix dynamic programming ...')
dynamicProg = []
for k in range(size):
    dynamicProg.append([])
    for m in range(size):
        print('Processing Row number',k,'Processing Column number',m)
        dynamicProg[k].append(0)
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
for k in range(4):
    for m in range(5):
        print('DynamicPBacker (',k,',',m,') ->',dynamicProg[k][m])
        print('FunctionBacker (',k,',',m,') ->',ackermannFunction(k,m))
