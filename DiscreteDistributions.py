from math import factorial, fabs

#Borrowed from G.Fleischer
def C(n,k):
    if k > n or k < 0:
        return 0
    else:
        if k > n//2:
            k = n-k
        res = 1
        for j in range(k):
            res *= n-j
            res //= j+1
    return res

def calcprobability(L, formula):
    if len(L) == 1:
        start = L[0]
        end = start
    elif len(L) == 2:
        start, end = L[0], L[1]
    else:
        print('Invalid, please only enter 1 or 2 arguments in the function')
        return
    
    res = 0
    for x in range(start, end+1):
        res += formula(x)
    return round(res, 4)

class discrete(object):

    def uniform(c,d):
        def distribution(*x):
            """Returns the probability of a certain x value occuring"""
            def formula(a):
                if c <= a <= d:
                    return 1/fabs((d-c+1))
                else:
                    return 0
            return calcprobability(x, formula)
        return distribution

        
    
    def binomial(n,p):
        if not 0 <= p <= 1:
            print('Invalid, p must be between 0 and 1')
            return
        """Returns a function that models the binomial distribution"""
        def distribution(*x):
            """Returns the probability of a certain x value occuring"""
            def formula(a):
                return C(n,a)*p**a*(1-p)**(n-a)
            return calcprobability(x, formula)
        return distribution

    def hypergeometric(N,n,k):
        if n > N:
            print('Invalid, n must be smaller or equal to N')
            return
        elif k > N:
            print('Invalid, k must be smaller or equal to N')
            return
        def distribution(*x):
            def formula(a):
                return C(k,a)*C(N-k,n-a)/C(N,n)
            return calcprobability(x, formula)
        return distribution

    def geometric(p):
        if not 0 <= p <= 1:
            print('Invalid, p must be between 0 and 1')
            return
        def distribution(*x):
            def formula(a):
                if a == 0:
                    return 0
                return (1-p)**(a-1)*p
            return calcprobability(x, formula)
        return distribution

    def negativebinomial(k,p):
        if not 0 <= p <= 1:
            print('Invalid, p must be between 0 and 1')
            return
        def distribution(*x):
            def formula(a):
                return C(a-1,k-1)*p**k*(1-p)**(a-k)
            return calcprobability(x, formula)
        return distribution

    def poisson(l):
        def distribution(*x):
            def formula(a):
                return l**a*exp(-l)/factorial(a)
            return calcprobability(x, formula)
        return distribution
