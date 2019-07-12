def gcd(a,n):
    if (a>n): return gcd(n,a)
    else:
        while True:
            r = n % a
            if r == 0: return a
            n = a
            a = r
def dioph(a,n):
    if gcd(a,n)!=1: return None
    elif a > n: return dioph(n,a)
    else:
        c,d = n,a
        c1,d1,c2,d2 = 1,0,0,1
        while d!=0:
            q,r = int(c/d),c%d
            r1 = c1 - q*d1
            r2 = c2 - q*d2
            c  = d; c1 = d1; c2 = d2
            d  = r; d1 = r1; d2 = r2
        return c2 % n
def driver():
    M = int(input('Enter the number ...'))
    for i in range(1,M):
        N = dioph(i,M)
        if N is None: print(i,N)
        else:
            print(i,i*N,'=',i,'*',N,'=',M,'*',int((i*N)/M),'+',(i*N)%M)
driver()