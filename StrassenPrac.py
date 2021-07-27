from pprint import pprint
def matrixExtend(A):
    n = len(A)
    if n%2 == 0: return
    else:
        for i in range(n): A[i].append(0)
        A.append([])
        for i in range(n+1): A[n].append(0)
        return
def matrixAdd(A,B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C
def matrixSub(A,B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C
def envelopeMatrixStrassen(A,B):
    if len(A) == 1:
        return [[A[0][0]*B[0][0]]]
    matrixExtend(A)
    matrixExtend(B)
    n = len(A)
    A11 = [[A[i][j] for j in range(int(n/2))] for i in range(int(n/2))]
    A12 = [[A[i][j] for j in range(int(n/2),n)] for i in range(int(n/2))]
    A21 = [[A[i][j] for j in range(int(n/2))] for i in range(int(n/2),n)]
    A22 = [[A[i][j] for j in range(int(n/2),n)] for i in range(int(n/2),n)]
    B11 = [[B[i][j] for j in range(int(n/2))] for i in range(int(n/2))]
    B12 = [[B[i][j] for j in range(int(n/2),n)] for i in range(int(n/2))]
    B21 = [[B[i][j] for j in range(int(n/2))] for i in range(int(n/2),n)]
    B22 = [[B[i][j] for j in range(int(n/2),n)] for i in range(int(n/2),n)]
    M1 = envelopeMatrixStrassen(matrixAdd(A11,A22),matrixAdd(B11,B22))
    M2 = envelopeMatrixStrassen(matrixAdd(A21,A22),B11)
    M3 = envelopeMatrixStrassen(A11,matrixSub(B12,B22))
    M4 = envelopeMatrixStrassen(A22,matrixSub(B21,B11))
    M5 = envelopeMatrixStrassen(matrixAdd(A11,A12),B22)
    M6 = envelopeMatrixStrassen(matrixSub(A21,A11),matrixAdd(B11,B12))
    M7 = envelopeMatrixStrassen(matrixSub(A12,A22),matrixAdd(B21,B22))
    C11 = matrixAdd(matrixSub(matrixAdd(M1,M4),M5),M7)
    C12 = matrixAdd(M3,M5)
    C21 = matrixAdd(M2,M4)
    C22 = matrixAdd(matrixAdd(matrixSub(M1,M2),M3),M6)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if 0<=i<int(n/2) and 0<=j<int(n/2): C[i][j] = C11[i][j]
            elif 0<=i<int(n/2) and int(n/2)<=j<n: C[i][j] = C12[i][j-int(n/2)]
            elif int(n/2)<=i<n and 0<=j<int(n/2): C[i][j] = C21[i-int(n/2)][j]
            elif int(n/2)<=i<n and int(n/2)<=j<n: C[i][j] = C22[i-int(n/2)][j-int(n/2)]
    return C
def matrixStrassen(A,B):
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])
    if rowA == colA and rowB == colB and rowA == rowB:
        if rowA%2 == 0:
            return envelopeMatrixStrassen(A, B)
        else:
            C = envelopeMatrixStrassen(A, B)
            n = len(C) - 1
            C1 = [[C[i][j] for j in range(n)] for i in range(n)]
            return C1
    else:
        raise('The matrices do not meet the standards ....')

a = [[1,0,0],[0,5,3],[7,8,9]]
print(a)
pprint(matrixStrassen(a,a))

