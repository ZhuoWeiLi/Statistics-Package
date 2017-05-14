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

def test(function, samples, sample_size = 1, intervals = 20):
    global counter
    print()
    print('*'*10+'Simulation '+str(counter)+'*'*10)
    print(samples,'samples with sample size', sample_size)
    print('\nClose the Graph to Continue')
    discrete.simulate(function, samples, sample_size, intervals)
    input('\nPress enter to move on to the next simulation')
    counter+=1

a = createdistribution(discrete.uniform, 0, 2000)
test(a, 200)
test(a, 2000)
test(a, 200, 10)
test(a, 2000, 10)
test(a, 2000, 30, 50)

a = createdistribution(discrete.binomial, 20, 0.5)
test(a, 100)
test(a, 1000)
test(a, 100, 10)
test(a, 1000, 10)
test(a, 1000, 30, 50)

a = createdistribution(discrete.hypergeometric, 80, 30, 30)
test(a, 100)
test(a, 1000)
test(a, 100, 10)
test(a, 1000, 10)
test(a, 1000, 30, 50)

a = createdistribution(discrete.geometric, 0.4)
test(a, 100)
test(a, 1000)
test(a, 100, 10)
test(a, 1000, 10)
test(a, 1000, 30, 50)

a = createdistribution(discrete.negativebinomial, 20, 0.7)
test(a, 100)
test(a, 1000)
test(a, 100, 10)
test(a, 1000, 10)
test(a, 1000, 30, 50)

a = createdistribution(discrete.poisson, 5)
test(a, 100)
test(a, 1000)
test(a, 100, 10)
test(a, 1000, 10)
test(a, 1000, 30, 50)

