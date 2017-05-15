"""Zhuo Wei Li
420-LCW-MS Programming Techniques and Applications (Python) Section 01
Friday, May 5th
G, Fleischer, instructor
Final Project."""

from math import factorial, fabs, exp, ceil
from random import random, shuffle
import matplotlib.pyplot as plt

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
    """Given an iterable containing 1 or 2 elements and a formula for calculating the probability of an x value,
    return the probability of that x value if there is 1 element in the iterable or the probability of
    that interval of x values if there are 2 elements in the iterable where the first element represents the
    start of the interval and the second element represents the end of the interval, inclusively."""
    if len(L) == 1:
        start = L[0]
        end = start
    elif len(L) == 2:
        start, end = L[0], L[1]
    else:
        print('Invalid, please only enter 1 or 2 arguments in the function')
        return
    
    res = 0
    
    #Calculate the probabilities of all the x values in the interval
    #and add them up, the for loop only executes once if there is 1 x value because start = end
    for x in range(start, end+1): 
        res += formula(x)
        
    return res

class discrete(object):

    def uniform(c,d):
        def pdf(*x):
            """Returns the probability of a certain x or interval of x values occuring"""
            if len(x) == 1:
                if c <= x[0] <= d:
                    return 1/fabs((d-c+1))
                else:
                    return 0
            elif len(x) == 2:
                start, end = x[0], x[1]
                if start < c:
                    start = c
                if end > d:
                    end = d
                if start > end:
                    return 0
                return 1/fabs((d-c+1))*(end-start+1)
        return pdf

        
    
    def binomial(n,p):
        """Returns the probability density function of the given binomial distribution"""
        if not 0 <= p <= 1:
            print('Invalid, p must be between 0 and 1')
            return
        def formula(a):
            return C(n,a)*p**a*(1-p)**(n-a)
        def pdf(*x):
            return calcprobability(x, formula)
        return pdf

    def hypergeometric(N,n,k):
        """Returns the probability density function of the given hypergeometric distribution"""
        if n > N:
            print('Invalid, n must be smaller or equal to N')
            return
        elif k > N:
            print('Invalid, k must be smaller or equal to N')
            return
        def formula(a):
            return C(k,a)*C(N-k,n-a)/C(N,n)
        def pdf(*x):
            """Returns the probability of a certain x or interval of x values occuring"""
            return calcprobability(x, formula)
        return pdf

    def geometric(p):
        """Returns the probability density function of the given geometric distribution"""
        if not 0 <= p <= 1:
            print('Invalid, p must be between 0 and 1')
            return
        def formula(a):
            if a == 0:
                return 0
            return (1-p)**(a-1)*p
        def pdf(*x):
            """Returns the probability of a certain x or interval of x values occuring"""
            return calcprobability(x, formula)
        return pdf

    def negativebinomial(k,p):
        """Returns the probability density function of the given negative binomial distribution"""
        if not 0 <= p <= 1:
            print('Invalid, p must be between 0 and 1')
            return
        def formula(a):
            return C(a-1,k-1)*p**k*(1-p)**(a-k)
        def pdf(*x):
            """Returns the probability of a certain x or interval of x values occuring"""
            return calcprobability(x, formula)
        return pdf

    def poisson(l):
        """Returns the probability density function of the given poisson distribution"""
        def formula(a):
            return l**a*exp(-l)/factorial(a)
        def pdf(*x):
            """Returns the probability of a certain x or interval of x values occuring"""
            return calcprobability(x, formula)
        return pdf

    def generate_data(pdf, num_samples, sample_size = 1):
        """Generate random data by taking random points from a given pdf and storing them into an array returned by the function"""

        #This block of code stores (num_samples * sample_size) random numbers between 0 and 1 into the list random_nums and sorts the list
        random_nums = [] 
        for i in range(num_samples*sample_size):
            random_nums.append(random())
        random_nums.sort()

        #This block of code takes the random numbers and maps them to x values according to the cumulative probabilities of the pdf used
        #Example, if the random numbers were [0.05, 0.1, 0.3, 0.45, 0.5, 0.7, 0.9] and the cumulative probabilities were
        #[0, 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.0] (uniform distribution going from x = 2 to x = 6),
        #the numbers would map to x values of [2, 2, 3, 4, 4, 5, 6] --> these values are stored into the 'points' list.
        cache = [pdf(0)] #Store the cumulative probabiltiies
        x = 0 #Counter for the current x-value of the last element in cache
        points = [] #Store the random x values generated 
        for num in random_nums:
            while num > cache[-1]: #If the biggest cumul probability in cache is smaller than the random num, generate new ones
                x+= 1
                cache.append(cache[-1] + pdf(x))
            points.append(x) #As soon there is a cumulative probability bigger than the current random_number, append the x-value
            #of that cumulative probability to points and move on to the next number

        #This block of code takes random samples of size (sample_size)from the points list and appends them to the samples list
        if sample_size != 1:
            samples = []
            shuffle(points) #If we shuffle the points, we can then just pop from the list to take random samples
            while points:
                sample = []
                for i in range(sample_size):
                    sample.append(points.pop())
                samples.append(sum(sample))
        else: #Else each sample has a sample size of one, so the points list represent samples of sample size 1
            samples = points

        samples.sort()
        return samples

    def histogram(data, num_intervals = 20):
        """Creates a frequency histogram from the data it takes as an argument"""
        #Create the intervals for the histogram and store them into the list bins
        start = min(data)
        end = max(data)
        bins = [start]
        interval = ceil((end - start)/num_intervals)
        for i in range(num_intervals+1): 
            current = bins[-1] + interval
            bins.append(current)
        

        #Setup histogram and show it
        print('Histogram with {} intervals of {} starting at {}'.format(num_intervals, interval, start))
        plt.hist(data, bins, histtype = 'bar')
        plt.show()
        
class continuous(object):
    def uniform(c,d):
        def pdf(start, end):
            if start < c:
                start = c
            if end > d:
                end = d
            if start > end:
                return 0
            return 1/fabs((d-c))*(end-start)
        return pdf

    def exponential(l):
        def pdf(start, end):
            if start < 0:
                start = 0
            if start > end:
                return 0
            return exp(-l*start)-exp(-l*end)
        return pdf
        
        
        
    




        

        
        

