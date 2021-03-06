"""Zhuo Wei Li
420-LCW-MS Programming Techniques and Applications (Python) Section 01
Friday, May 5th
G, Fleischer, instructor
Final Project."""

from Distributions import discrete

distribution_counter = 0
counter = 1
def createdistribution(distribution, *parameters):
    global distribution_counter
    distribution_counter += 1
    global counter
    counter = 1
    print()
    print(distribution.__name__[0].upper()+distribution.__name__[1:]+" distribution with parameters " + str(parameters) + "*" *30)
    return distribution(*parameters)

def test(function, *values):
    global counter
    print()
    print('*'*10+'Test '+str(counter)+'*'*10)
    print('Values:', values)
    print('Probability:', function(*values))
    counter+=1

if __name__ == "__main__":

    a = createdistribution(discrete.uniform, 2, 9)
    test(a, 0)
    test(a, 1, 5)
    test(a, 5, 3)
    test(a, 2, 10)
    test(a, 8, 10)
    test(a,2)
    test(a, 5,7)
    test(a,5)

    a = createdistribution(discrete.binomial, 5, 9)
    a = createdistribution(discrete.binomial, 5, 0.8)
    test(a, 0, 5)
    test(a, 0)
    test(a, 3, 5)
    test(a, 3)
    test(a, 4)
    test(a, 5)
    test(a, 6)

    a = createdistribution(discrete.hypergeometric, 8, 9, 10)
    a = createdistribution(discrete.hypergeometric, 8, 5, 10)
    a = createdistribution(discrete.hypergeometric, 8, 4, 5)
    test(a, 0, 5)
    test(a, 0)
    test(a, 1,4)
    test(a, 3, 4)
    test(a, 3)
    test(a, 4)
    test(a, 5)

    a = createdistribution(discrete.geometric, 0.7)
    test(a, 0)
    test(a, 1, 100)
    test(a, 1)
    test(a,2)
    test(a,3)
    test(a,6)

    a = createdistribution(discrete.negativebinomial, 4, 0.7)
    test(a, 0)
    test(a, 2)
    test(a,4,100)
    test(a, 4)
    test(a, 7)
    test(a, 10)

    a = createdistribution(discrete.poisson, 3)
    test(a, 0, 100)
    test(a, 0)
    test(a, 2)
    test(a, 3)
    test(a, 4)
    test(a, 5)
    test(a, 100)

