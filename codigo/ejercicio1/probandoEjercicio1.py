from encontrarNumero import *
from fitnessFunctions import fit1
from fitnessFunctions import fit2
from fitnessFunctions import fit3

print("busqueda simple")
F=[AddNode,SubNode,MultNode]
T=[2,3,5]
engineEncontrarNumero1(fit1,10,10,6,3,3,F,T)
print("#####################################################################")
print("busqueda fit1")
F2=[AddNode,SubNode,MultNode,MaxNode]
T2=[25,7,8,100,4,2]

engineEncontrarNumero1(fit1,65346,20,100,10,10,F2,T2)

print("#####################################################################")
print("busqueda fit2")
engineEncontrarNumero1(fit2,65346,20,100,10,10,F2,T2)

print("#####################################################################")
print("busqueda fit3")
F3=[AddNode,SubNode,MultNode]
T2=[25,7,8,100,4,2]

engineEncontrarNumero1(fit3,65346,40,200,10,10,F3,T2)
