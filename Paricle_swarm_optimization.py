# -*- coding: utf-8 -*-
"""
Purpose of this program is to find global minima of given function (Rosenbrock function in this case) using
particle swarm optimization. This program also plots the function and the particles.
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    
    '''
    Rosenbrock function
    
    Parameters
    ----------
    x and y : Parameters of the function

    Returns
    -------
    result : Result of the function with given parameters
    '''
    result = (0.5-x)**2 + 1.5*(y-x**2)**2
    return result


if __name__ == "__main__":
    w = 0.8
    sigma = 0.9
    iterations = 50
    particles=5
    location = np.zeros([2,particles]) #matrix that contains all locations of all particles 
                                       #rows are particles, first column = x second column = y
    l_best = np.zeros([2,particles]) #matrix that contains all local bests of all particles
    velocity = np.zeros([2,particles]) #matrix that contains all velocities of all particles
    g_best=[0,0] #position of the global best
    minarea = -2 #limits of the solution space
    maxarea = 2
    x = np.linspace(minarea, maxarea)
    y = np.linspace(minarea, maxarea)
    X, Y = np.meshgrid(x, y)
    Z = f(X,Y)
    fig=plt.figure()
    plt.contour(X, Y, Z, 100, cmap='RdGy');
    plt.xlim(minarea, maxarea)
    plt.ylim(minarea, maxarea)
    i = 0
    #initialize particles
    while i < particles:
        r_loc1 = random.randrange(minarea*100,maxarea*100)/100
        r_loc2 = random.randrange(minarea*100,maxarea*100)/100
        location[0,i]=r_loc1
        location[1,i]=r_loc2
        l_best[0,i]=r_loc1
        l_best[1,i]=r_loc2
        if i==0:
            g_best[0]=l_best[0,i]
            g_best[1]=l_best[1,i]
        else:
            if f(l_best[0,i],l_best[1,i])<f(g_best[0],g_best[1]):
                g_best[0]=l_best[0,i]
                g_best[1]=l_best[1,i]
        velocity[0,i]=0 #starting velocity set to 0
        velocity[1,i]=0
        i=i+1
    j=0
    #Updating particles locations, local bests, velocities and global best to find global minima
    while j < iterations:
        i=0
        while i < particles:
            r_l=random.randrange(0,100)/100
            r_g=random.randrange(0,100)/100
            velocity[0,i] = w*velocity[0,i] + sigma*r_l*(l_best[0,i]-location[0,i])+sigma*r_g*(g_best[0]-location[0,i])
            velocity[1,i] = w*velocity[1,i] + sigma*r_l*(l_best[1,i]-location[1,i])+sigma*r_g*(g_best[1]-location[1,i])
            location[0,i]=location[0,i]+velocity[0,i]
            location[1,i]=location[1,i]+velocity[1,i]
            if f(location[0,i],location[1,i])<f(l_best[0,i],l_best[1,i]):
                l_best[0,i]=location[0,i]
                l_best[1,i]=location[1,i]
                if f(l_best[0,i],l_best[1,i])<f(g_best[0],g_best[1]):
                    g_best[0]=l_best[0,i]
                    g_best[1]=l_best[1,i]
            i=i+1
        j=j+1
    plt.plot(location[0],location[1],'gx')