from random import randint
from random import random

class Equation:
    def __init__(self, coeff , sol):
        self.c = coeff
        self.sol = sol
        vect =[]
        for i in range(6):
            l = []
            for _ in range(len(self.c)):
                l.append(randint(0,30))
            vect.append(l)
        self.unk = vect
        
    # repr method 
    def __repr__(self):
        return str(list(zip(self.c, ('a','b','c','d')))) + " = " + str(self.sol)

    def getBestResults(self):
        x = []
        for v in self.unk:
            somme = 0
            for i in range( len(self.c)):
                somme+= self.c[i]* v[i] 

            x.append((v, abs(somme - 30)))

        x.sort(key=lambda tup: tup[1])
        
        return x[0:3]
    
    def bestChromo(self):
        return self.getBestResults()[min(range(len(self.getBestResults())), key = lambda i: abs(self.getBestResults()[i][1]-0))] 

    def croissement(self, bestRes):
        newPop = []
        for item in bestRes:
            newPop.append(item[0])

        # flip 0 and 1
        newPop.append((bestRes[0][0][0:2] + bestRes[1][0][2:4]))
        newPop.append((bestRes[1][0][0:2] + bestRes[0][0][2:4]))

        # # flip 0 and 2
        newPop.append(( bestRes[0][0][0:2] + bestRes[2][0][2:4]))    
        # newPop.append(( bestRes[2][0][0:2] + bestRes[0][0][2:4]))

        # # flip 1 and 2
        # newPop.append(( bestRes[1][0][0:2] + bestRes[2][0][2:4]))    
        # newPop.append(( bestRes[2][0][0:2] + bestRes[1][0][2:4]))
        
        self.unk = newPop

    def mutate(self):
        #  threshold = (1/population size /chromosome length)
        threshold = ( 1 / 6 /4) 
        prob = random()
        # print('prob = ' + str(prob))
        if(prob <= threshold):
            indexOfChromosome = randint(0,5)
            indexOfGene = randint(0,3)
            self.unk[indexOfChromosome][indexOfGene] = randint(0,30)

        
    def solve(self):
        print("Initial coefficions are equal to : ")
        print(self.unk)
       

        compt = 0
        while(self.bestChromo()[1] != 0 ):
            compt +=1 
            self.croissement(self.getBestResults())           
            self.mutate()
            self.getBestResults()
    
        
        # error => distance from 30 
        # example : error = 3 => equation result = 33 
        #           error = -4 => result = 26
        print('solution found in ' + str(compt)+ " generations")
        print("solutions is:  [Coefficients , equation solution ]")
        
        return self.bestChromo()

eq = Equation((1,2,3,4),30)

print(eq.solve())