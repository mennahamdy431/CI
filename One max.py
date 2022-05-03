import random
import numpy as np
import matplotlib.pyplot as plt


def rand():
    return random.uniform(0, 1)


def selection(fitness):
    total = sum(fitness)
    return fitness / total


def commulative(fitness):
    comm = []
    comm.append(fitness[0])
    for i in range(1, 20):
        comm.append(fitness[i] + comm[i - 1])
    return comm


def getParentsIndex(comm):
    r = rand()
    for i in range(20):
        if r <= comm[i]:
            return i


def crossover(child1, child2, pcross):
    r = rand()
    cp = int(r * 5)

    if r <= pcross:

        for i in range(cp, 5):
            temp = child2[i]
            child2[i] = child1[i]
            child1[i] = temp


def mutation(ch, pmut):
    for i in range(5):
        r = rand()
        if r < pmut:
            if ch[i] == 0:
                ch[i] = 1
            else:
                ch[i] = 0



def Elitism(fitness, flag):
    mx=-1
    mxIdx=-1
    for i in range(20):
        if fitness[i] > mx and i != flag:
            mx = fitness[i]
            mxIdx = i
    return mxIdx


def run(npop, ngeneration, clenth, pcross, pmut):
    oldPop = np.random.randint(0, 2, size=(20, 5))
    bstfit = []
    avgfit = []
    for m in range(ngeneration):
        newPop = []
        fitness = []
        for i in range(npop):
            fit = sum(oldPop[i])
            fitness.append(fit)
        elitism1 = Elitism(fitness, -1)
        elitism2 = Elitism(fitness, elitism1)
        newPop.append(list(oldPop[elitism1]))
        newPop.append(list(oldPop[elitism2]))
        for j in range(10):
            comm = commulative(selection(fitness))

            parent1 = oldPop[getParentsIndex(comm)]
            parent2 = oldPop[getParentsIndex(comm)]

            child1 = []
            child2 = []
            for i in range(clenth):
                child1.append(parent1[i])
                child2.append(parent2[i])
            crossover(child1, child2, pcross)
            mutation(child1, pmut)
            mutation(child2, pmut)
            newPop.append(child1)
            newPop.append(child2)
        oldPop = newPop.copy()
        bstfit.append(max(fitness))
        avgfit.append(sum(fitness)/len(fitness))
    print("Best Fitness is : ")
    print(bstfit)
    print("Average Fitness is : ")
    print(avgfit)
    plt.plot(bstfit)
    plt.title("Best Fitness")
    plt.ylabel("High fitness")
    plt.xlabel('Generations')
    plt.show()
    plt.plot(avgfit)
    plt.title("Average Fitness")
    plt.ylabel("Mean of fitness")
    plt.xlabel('Generations')
    plt.show()


npop = 20
clenth = 5
pcross = 0.6
pmut = 0.05
ngeneration = 100

for i in range(10):
    run(npop, ngeneration, clenth, pcross, pmut)
