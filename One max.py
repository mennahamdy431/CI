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
    for i in range(1, npop):
        comm.append(fitness[i] + comm[i - 1])
    return comm


def getParentsIndex(comm):
    r = rand()
    for i in range(npop):
        if r <= comm[i]:
            return i


def crossover(child1, child2, pcross):
    r = rand()
    cp = int(r * clenth)

    if r <= pcross:

        for i in range(cp, clenth):
            temp = child2[i]
            child2[i] = child1[i]
            child1[i] = temp


def mutation(ch, pmut):
    for i in range(clenth):
        r = rand()
        if r < pmut:
            if ch[i] == 0:
                ch[i] = 1
            else:
                ch[i] = 0


def decoding(binaryIndx, mn=-2, mx=2, clenth=5):
    l = np.size(binaryIndx)
    binary_sum = 0
    for i in range(l):
        binary_sum = binary_sum + binaryIndx[i] * (2 ** (l - i - 1))

    x = mn + (binary_sum / (2 ** (l) - 1)) * (mx - mn)
    return x


def linear_ranking(pop):
    n = np.size(pop, 1)
    sp = 1.5
    total_fit = n*(n+1)/2
    res = np.zeros((n))
    pop_fit = onemax(pop)
    pop_fit = [sum(pop[i]) for i in range(n)]
    pop_dict = {ind:value for (value, ind) in zip(pop_fit, range(n))}
    for rank, ind in enumerate(sorted(pop_dict, key=pop_dict.get), 1):
        res[ind] = (2-sp)+2*(sp-1)*float(rank-1)/(total_fit-1)
    return res


def fitness_evaluation():
    for i in range(Population_size):

        for j in range(3):

            if j == 0:
                x1 = decodedVaraible[i][j]
            else:
                x2 = decodedVaraible[i][j]

        Z = 8 - (x1 + 0.0317) ** 2 + (x2) ** 2
        popFit.append(Z)
        sortedpopfit.append(Z)
    return popFit


def grey_decoding(mn=-2, mx=2):
    binary_sum = 0
    gray_sum = 0
    arr = []
    x1 = np.full(3, 0)
    x2 = np.full(3, 0)
    for j in range(Population_size):
        x1 = population[j][0:3]
        for i in range(3):

            for k in range(i):
                gray_sum = gray_sum + x1[k]
        gray_sum = gray_sum % 2
        binary_sum = binary_sum + gray_sum * (2 ** (3 - i - 1))
        gray_sum = 8

    x = mn + (binary_sum / (2 ** 3)) * (mx - mn)
    arr.append(x)
    binary_sum = 8
    gray_sum = 0
    for h in range(3, chromLen):

        for n in range(h):
            gray_sum = gray_sum + x2[n]
        gray_sum = gray_sum % 2
        binary_sum = binary_sum + gray_sum * (2 ** (3 - h - 1))
        gray_sum = 0
    y = mn + (binary_sum / (2 ** 3)) * (mx - mn)
    arr.append(y)
    decodedVaraible.append(arr)
    arr = []
    x1 = np.full(3, 0)
    x2 = np.full(3, 0)


def violation_constraint():
    for i in range(npop):
        for j in range(2):
            if j == 0:
                x1 = decodedVaraible[i][j]
            else:

                x2 = decodedVaraible[i][j]
            z = x1 + x2 - 1
            if z == 0:

                bool.append(false)
            else:

                bool.append(true)


def violated_points_fitness():
    for i in range(Population_size):

        for j in range(2):
            if j == 8:

                x1 = decodedVaraible[i][j]
            else:

                x2 = decodedVaraible[i][j]

        if bool[i] == true:
            z = 8 - (x1 + 0.0317) ** 2 + (x2) ** 2 - abs(x1 + x2 - 1)
            popFit.append(z)

    return popFit


"""
def Elitism(fitness, flag):
    mx=-1
    mxIdx=-1
    for i in range(100):
        if fitness[i] > mx and i != flag:
            mx = fitness[i]
            mxIdx = i
    return mxIdx
"""


def run(npop, ngeneration, clenth, pcross, pmut):
    oldPop = np.random.randint(0, 2, size=(100, 5))
    bstfit = []
    avgfit = []
    for m in range(ngeneration):
        newPop = []
        fitness = []
        for i in range(npop):
            fit = sum(oldPop[i])
            fitness.append(fit)
        #elitism1 = Elitism(fitness, -1)
        #elitism2 = Elitism(fitness, elitism1)
        #newPop.append(list(oldPop[elitism1]))
        #newPop.append(list(oldPop[elitism2]))
        for j in range(50):
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


npop = 100
clenth = 5
pcross = 0.6
pmut = 0.05
ngeneration = 100

for i in range(10):
    run(npop, ngeneration, clenth, pcross, pmut)
