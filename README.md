# genetic-algorithm-equation-solving
Python implementation for a Genetic Algorithm to solve linear equations.
## The equation a+2b+3c+4d = 30 , this implementation will find the value of a,b,c and d using an evolutionary algorithm.
### Steps
#### Initialization: 
randomly initialize the population
#### Compute the fitness function: 
for each vector compute the value of a+2b+3c+4d-30 = 0 
#### Selection: 
choose the 3 best chromosomes.
#### Crossover: 
preform crossover between the best 3 chromosomes to generate the new population. 
#### Mutation: 
preform mutation according to the following probability:
     threshold = (1/population size /chromosome length)

### additional notes:
- the algorithm will run until finding the optimal solution.
- to solve other equations: change line 84 
     ```
     Equation((1,2,3,4),30)
     ```
to whatever coefficients or result you want.
