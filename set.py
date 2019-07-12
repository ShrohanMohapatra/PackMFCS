def new_set():
    A,p = [],1
    while p!=0:
        p = int(input('Want to enter a new element? '))
        if p == 0: break
        x = int(input('Enter a new element. '))
        if x not in A: A.append(x)
    return A
def union_set(A,B):
    C = []
    for i in range(len(A)): C.append(A[i])
    for i in range(len(B)):
        if B[i] not in C: C.append(B[i])
    return C
def intersect_set(A,B):
    C = []
    for i in range(len(A)):
        if A[i] in B: C.append(A[i])
    return C
def difference(A,B):
    C = []
    for i in range(len(A)):
        if A[i] not in B: C.append(A[i])
    return C
def symm_diff(A,B): return union_set(difference(A,B),difference(B,A))
def equality(A,B):
    flag = True
    flag = flag and len(A) == len(B)
    if not flag: return flag
    for i in range(len(A)): flag = flag and A[i] in B
    return flag
def power_set(A):
    B = []
    for i in range(2**len(A)):
        k,C,D = i,[],[]
        for j in range(len(A)):
            C.append(k%2)
            k = k / 2
        for j in range(len(A)):
            if C[j] == 1: D.append(A[j])
        B.append(D)
    return B
def cross_product(A,B):
    C = []
    for i in A:
        for j in B: C.append([i,j])
    return C
def equivalence(A,R):
    # A = [0,1,2,3,4]
    # R = {0:[0,3,4],1:[1],2:[2],3:[0,3,4],4:[0,3,4]}
    flag = True
    for x in A: flag = flag and (x in R[x])
    if not flag: return flag
    for x in A:
        for y in R[x]: flag = flag and (x in R[y])
    if not flag: return flag
    for x in A:
        for y in R[x]:
            for z in R[y]: flag = flag and (z in R[x])
    return flag
def main():
    print(None)
def contradiction_function():
    def f(x): return x+1
    def g(x): return x**2
    for x in range(40):
        print(f(g(x)) ,x**2 + 1, g(f(x)), (x+1)**2)
main()