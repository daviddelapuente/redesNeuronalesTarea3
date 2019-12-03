import sys
from encontrarNumero import *
from encontrarNumeroConGrafico import *
from fitnessFunctions import fit1
from fitnessFunctions import fit2
from fitnessFunctions import fit3

if sys.argv[1]=="singraf":
    if sys.argv[2]=="conrep":
        print("busqueda con repeticion")
        F2=[AddNode,SubNode,MultNode,MaxNode]
        T2=[25,7,8,100,4,2]
        engineEncontrarNumero1(fit1,int(sys.argv[3]),20,100,10,10,F2,T2)
        #print("#####################################################################")
        #print("busqueda fit2")
        #engineEncontrarNumero1(fit2,65346,20,100,10,10,F2,T2)

        #print("#####################################################################")
        #print("busqueda fit3")
        #F3=[AddNode,SubNode,MultNode]
        #T2=[25,7,8,100,4,2]

        #engineEncontrarNumero1(fit3,65346,40,200,10,10,F3,T2)

elif sys.argv[1]=="congraf":
        print("busqueda con repeticion")
        F2=[AddNode,SubNode,MultNode,MaxNode]
        T2=[25,7,8,100,4,2]
        engineEncontrarNumeroConGrafico(fit1,int(sys.argv[3]),20,100,10,10,F2,T2,"fitnessEvolConrep")