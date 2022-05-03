import random
import numpy as np
import matplotlib.pyplot as plt


def intial(nPop, x_Min, x_Max, v_Max, dim):
    X = np.zeros((nPop, dim), dtype=float)
    V = np.zeros((nPop, dim), dtype=float)
    for i in range(dim):
        X[:, i] = np.random.uniform(x_Min[i], x_Max[i], (nPop))
        V[:, i] = np.random.uniform((-1*v_Max[i]), v_Max[i], (nPop))
    return X, V


def fitCalc(xi):
  fitness = np.sin(2*xi[0]-(0.5*np.pi)) + 3*np.cos(xi[1]) + (0.5*xi[0])
  return fitness


def updatePid(xi, xfitness, pi, particlebestFit):
    if xfitness > particlebestFit:
        pi = xi
    return pi


def updatePgd(pi, particlebestFit, pg, globalbestFit):
    if particlebestFit > globalbestFit:
        pg = pi
        globalbestFit = particlebestFit
    return pg, globalbestFit


def updateVidXid(pi, pg, xi, vi, cCog, cSoc, dim):

    rcog = np.random.random(dim)
    rsoc = np.random.random(dim)
    vi = np.array(vi) + (cCog * np.multiply(rcog, np.subtract(pi, xi))) + (cSoc * np.multiply(rsoc, np.subtract(pg, xi)))
    xi = np.array(xi) + vi
    return xi, vi


def PSO(i, nPop, x_max, x_min, v_max, dim, cCog, cSoc):
    x, v = intial(nPop, x_max, x_min, v_max, dim)
    p = x[:]
    pg = np.zeros(dim)
    globalbestFit = -100000000000
    for iteration in range(i):
        for j in range(nPop):
            p[j] = updatePid(x[j], fitCalc(x[j]), p[j], fitCalc(p[j]))
            pg, globalbestFit = updatePgd(p[j], fitCalc(p[j]), pg, globalbestFit)
        for j in range(nPop):
            x[j], v[j] = updateVidXid(p[j], pg, x[j], v[j], cCog, cSoc, dim)
            xList.append(x[j][0])
            yList.append(x[j][1])

        plt.scatter(xList, yList)
        plt.show()
        xList.clear()
        yList.clear()

    plt.scatter(pg[0], pg[1], color="Red")
    plt.show()

    return pg, globalbestFit


xList = []
yList = []
x1 = []
y1 = []
i = 200
nPop = 50
x_max = [3, 1]
x_min = [-2, -2]
v_max = [0.1, 0.1]
dim = 2
cCog = 1.7
cSoc = 1.7


for i in range(2):
    pg, globBestFit = PSO(i, nPop, x_max, x_min, v_max, dim, cCog, cSoc)
    print('\n', "_________________________ GENERATION", i + 1, "____________________________", '\n')
    print("pg = ", pg, '\n')
    print("globBestFit = ", globBestFit, "\n")
    print("__________________________________________________________________________________")

