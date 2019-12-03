import matplotlib.pyplot as plt
from astD import *
from arboles import *

def maximoDeFitness(F):
    max=F[0]
    for f in F:
       if f>=max:
           max=f
    return max

def minimoDeFitness(F):
    min=F[0]
    for f in F:
        if f<=min:
            min=f
    return min

def promedioDeFitness(F):
    mean=0
    for f in F:
        mean+=f
    return mean/len(F)

#inicia una poblacion de largo populationLen, con individuos de profundidad maxima d definidos por el cjto de funciones F y los terminales T.
def initPopulation(populationLen,a,d):
    population=[]
    
    for i in range(populationLen):
        population.append(a.__call__(d))
    return population


#calcula el fitnes para un subconjunto de la poblacion
def fitnessesI(population,n,competitors,fit,a):
    fitness=[]
    for i in range(len(competitors)):
        f=fit(population[competitors[i]],n,a)
        fitness.append(f)
    return fitness




#calcula el fitness para la poblacion
def fitnesses(population,n,fit,a):
    fitness=[]
    for p in population:
        fitness.append(fit(p,n,a))
    return fitness



#devuelve un conjunto al azar de tamano n de indices entre 0 y l-1
def randIndex(l,n):
    r=[]
    for i in range(n):
        r.append(random.randint(0, l - 1))
    return r



def crossOverArbol(n1,n2):
    if random.random()>0.5:
        n1Copia=n1.copy()

        h1=n1Copia.serialize()
        h2=n2.serialize()

        i=random.randint(0,len(h1)-1)

        j=random.randint(0,len(h2)-1)

        h1[i].replace(h2[j])

        return n1Copia
    else:
        n2Copia=n2.copy()
        h2=n2Copia.serialize()
        h1=n2.serialize()
        
        i=random.randint(0,len(h1)-1)
        j=random.randint(0,len(h2)-1)

        h2[j].replace(h1[i])

        return n2Copia

        

def mutarArbol(n1,mutability,a,d):
    h=n1.serialize()
    i=random.randint(0,len(h)-1)
    h[i].replace(a.__call__(max(1,d/3)))
    return n1



#algoritmo genetico que encuentra un arbol que representa un numero, con repeticion de terminales
def engineEncontrarNumeroConGrafico(fitnessFunction,number,trys,populationLen,Ncompetitors,depth,F,T,fileName,mutability=1):
    b=False
    a=AST(F,T,0.5)
    print("buscando arbol para: "+str(number))
    population = initPopulation(populationLen,a,depth)

    maximos=[]
    minimos=[]
    promedios=[]
    

    #como queremos encontrar el mejor arbol, iteramos el numero de trys
    for t in range(trys):

        
        
        #aca se ira guardando la desendencia de la nueva poblacion.
        newPopulation=[]


        #queremos que el largo de la poblacion sea  el mismo siempre, por lo que vamos
        #agregando nuevos valores a newPopulation hasta que sus valores sean iguales.
        while(len(newPopulation)<len(population)):

            #buscamos indices al azar
            competitors=randIndex(len(population),Ncompetitors)

            #ahora los competidores compiten (calcular su fitness)

            fitness=fitnessesI(population,number,competitors,fitnessFunction,a)



            # tournament
            max1 = fitness[0]
            max2 = fitness[0]

            winner1 = 0
            winner2 = 0

            for i in range(len(competitors)):
                
                if fitness[i] > max1:
                    max1=fitness[i]
                    winner1 = competitors[i]

            for i in range(len(competitors)):
                if competitors[i] != winner1 and fitness[i] > max2:
                    max2=fitness[i]
                    winner2 = competitors[i]
            
            son = mutarArbol(crossOverArbol(population[winner1], population[winner2]),mutability,a,depth)

            newPopulation.append(son)

        population=newPopulation

        maxfit=-1
        best=0

        F=fitnesses(population,number,fitnessFunction,a)



        for i in range(len(F)):
            if F[i]>maxfit:
                maxfit=F[i]
                best=i

            if maxfit==0:
               
                print("encontrada!")
                print("en iteracion "+str(t))
                b=True
                break
        
        maximos.append(maximoDeFitness(F))
        minimos.append(minimoDeFitness(F))
        promedios.append(promedioDeFitness(F))

        if b:
            break

    
    print("best is "+str(population[best]))
    print("with fitness "+str(F[best]))
    print("eval is: "+str(population[best].eval()))
    print("----------------------------------------")
    print("ploting")
    f1 = plt.figure(1)
    ax1 = f1.add_subplot(111)
    ax1.set_title("fitnesses")
    ax1.set_xlabel('epochos')
    ax1.set_ylabel('fitness')
    ax1.plot(maximos, c='r')
    f1.savefig(fileName+".png")