# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:13:11 2019

@author: miru
"""

# suppose we have 10 people
# each person tosses a coin
# 1 dollar for heads (move to te right)
import numpy as np
import matplotlib.pyplot as plt

'''
pass initialPoint as whatever you would like, make sure however it is between
brokeAt and M for M finite and brokeAt < M.
'''

def randomWalk(initialPoint, winAt):
    # initialize number of flips
    numFlips = 0
    # initialize container for initial point as we progress
    points = []
    points.append(initialPoint)
    numFlips += 1
    # as long as we have not lost all the $$$
    while initialPoint != winAt and initialPoint != 0:
        # random.random is a uniform random variable ~[0,1]
        flip = np.random.random()
        if flip < 0.5:
            initialPoint -= 1
            points.append(initialPoint)
        elif flip > 0.5:
            initialPoint += 1
            points.append(initialPoint)
        # update number of Flips
        numFlips += 1
    return numFlips, points, initialPoint

'''
simulate the walk. Parameter takes in number of runs desired for the simulation
'''
def simulate(numRuns):
    sims = []
    for i in range(numRuns):
        # you pass different arguments here. Just make sure the first argument is smaller than the second argument
        # and bigger than 0
        numFlips, points, initialPoint = randomWalk(50, 100)
        plt.plot(np.arange(0, numFlips), points, 'b', np.arange(0, numFlips), [0 for j in range(numFlips)], 'r', np.arange(0, numFlips), [initialPoint for j in range(numFlips)], 'r')
        plt.xlabel('Number of Flips or people')
        plt.ylabel('State')
        plt.savefig("simulation" + str(i))
        plt.show()
        sims.append(numFlips)
    return sims

def main():
    # pass in different arguments here as desired.
    result = simulate(10)
    print(result)
    mean = computeMean(result)
    print(mean)

'''
computes mean number of flips for our game to end
'''
def computeMean(result):
    return np.mean(result)

    
main()
        