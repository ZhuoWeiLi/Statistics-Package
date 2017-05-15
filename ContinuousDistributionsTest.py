"""Zhuo Wei Li
420-LCW-MS Programming Techniques and Applications (Python) Section 01
Friday, May 5th
G, Fleischer, instructor
Final Project."""

from Distributions import continuous
from DiscreteDistributionsTest import createdistribution, test

a = createdistribution(continuous.uniform, 0, 8)
test(a, -3, -1)
test(a, 0, 8)
test(a, -2, 3)
test(a, 5.5, 7)
test(a, 7, 12)
test(a, 8, 10)

a = createdistribution(continuous.exponential, 0.2)
test(a, 0, 100)
test(a, 2.5, 6)
test(a, 2.5, 4)
test(a, 4, 6)
test(a, 7, 12)
test(a, 5, 3)
test(a, 4, 4)
