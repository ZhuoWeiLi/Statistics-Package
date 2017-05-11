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
    input('Press enter to move on to the next simulation')
    counter+=1

a = createdistribution(discrete.uniform, 0, 20)
test(a, 50)
test(a, 500)
test(a, 50, 10)
test(a, 500, 10)

a = createdistribution(discrete.binomial, 20, 0.5)
test(a, 50)
test(a, 500)
test(a, 50, 10)
test(a, 500, 10)

a = createdistribution(discrete.hypergeometric, 50, 20, 20)
test(a, 50)
test(a, 500)
test(a, 50, 10)
test(a, 500, 10)
