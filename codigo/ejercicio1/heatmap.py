import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from encontrarNumeroHeatMap import *
from fitnessFunctions import fit1

def headMap():
    F2=[AddNode,SubNode,MultNode,MaxNode]
    T2=[25,7,8,100,4,2]

    k=0
    print("creando headMap")
    poblaciones=[]
    for i in range(10):
        poblaciones.append(50+50*i)

    mutabilidad=[]

    for i in range(10):
        mutabilidad.append(0+i*0.1)

    mapRows=[]
    for i in range(10):
        mapCols=[]
        for j in range(10):
            print("iteracion: "+str(k))
            k+=1
            populationLen=poblaciones[i]
            mutability=mutabilidad[j]
            mapCols.append(engineEncontrarNumero1(fit1,65346,20,populationLen,10,10,F2,T2,mutability))
        mapRows.append(mapCols)

    h=sns.heatmap(mapRows)
    fig=h.get_figure()
    ax1 = fig.add_subplot(111)
    
    ax1.set_xlabel('mutability')
    ax1.set_ylabel('populationLen')
    fig.savefig("heatmap.png")
    print("fin")

headMap()