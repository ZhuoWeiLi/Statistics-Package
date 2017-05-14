from Distributions import discrete

"""A poisson distribution with lambda parameter equal to the parameters n*p of
a binomial distribution can be used to approximate said binomial distribution
for big n and small p"""

n = 20
p = 0.08
l = n*p
print('Create a binomial distribution with n = {} and p = {}'.format(n,p))
b = discrete.binomial(n,p)
print('Create a poisson distribution with lambda = {}'.format(l))
poisson = discrete.poisson(l)

print('Let\'s see how the probabilities compare at various x values')
for i in range(0, n+1, 2):
    print('The probability of x = {} in the binomial distribution is {}'.format(i, b(i)))
    print('The probability of x = {} in the poisson distribution is {}'.format(i, poisson(i)))
    print()
