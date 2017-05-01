from DiscreteDistributions import discrete

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

def test(function, samples, sample_size = 1):
    global counter
    print()
    print('*'*10+'Simulation '+str(counter)+'*'*10)
    print(samples,'samples with sample size', sample_size)
    print('\nClose the Graph to Continue')
    discrete.simulate(function, samples, sample_size)
    input('Press Enter to Continue')
    counter+=1

a = createdistribution(discrete.uniform, 0, 50)
test(a, 25)
test(a, 100)
test(a, 25, 10)
test(a, 100, 10)

a = createdistribution(discrete.binomial, 10, 0.7)
test(a, 10)
test(a, 100)
test(a, 10, 5)
test(a, 100, 5)

a = createdistribution(discrete.hypergeometric, 10, 3, 4)
test(a, 20)
test(a, 100)
test(a, 20, 5)
test(a, 100, 5)
