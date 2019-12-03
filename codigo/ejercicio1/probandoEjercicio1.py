import sys
from encontrarNumero import *
from encontrarNumeroConGrafico import *
from fitnessFunctions import fit1
from fitnessFunctions import fit2
from fitnessFunctions import fit3

F2=[AddNode,SubNode,MultNode,MaxNode]
T2=[25,7,8,100,4,2]

if sys.argv[1]=="singraf":
    if sys.argv[2]=="conrep":
        if sys.argv[3]=="sincast":
            print("busqueda con repeticion sin castigo")
            engineEncontrarNumero1(fit1,int(sys.argv[4]),20,100,10,10,F2,T2)
        elif sys.argv[3]=="concast":
            print("busqueda con repeticion con castigo")
            engineEncontrarNumero1(fit2,int(sys.argv[4]),20,100,10,10,F2,T2)
    elif sys.argv[2]=="sinrep":
        print("busqueda sin repeticion")
        F3=[AddNode,SubNode,MultNode]
        T2=[25,7,8,100,4,2]
        engineEncontrarNumero1(fit3,int(sys.argv[3]),40,200,10,10,F3,T2)

elif sys.argv[1]=="congraf":
    if sys.argv[2]=="conrep":
        if sys.argv[3]=="sincast":
            print("busqueda con graficos con repeticion sin castigo")
            engineEncontrarNumeroConGrafico(fit1,int(sys.argv[4]),20,100,10,10,F2,T2,"fitnessEvolConrep")
        elif sys.argv[3]=="concast":
            print("busqueda con graficos con repeticion con castigo")
            engineEncontrarNumeroConGrafico(fit2,int(sys.argv[4]),20,100,10,10,F2,T2,"fitnessEvolConrepConcast")