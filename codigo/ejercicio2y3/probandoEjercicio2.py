from encontrarEcuacion import *
from encontrarEcuacionConGrafico import *
from fitnessFunctions import fit
from fitnessFunctions import fit2
from fitnessFunctions import fit3
import sys

arbolReal=SubNode(AddNode(MultNode(TerminalNode("x"),TerminalNode("x")),TerminalNode("x")),TerminalNode(6))
intervalo=range(-100,100)
trys=10
populationLen=100
depth=5
F=[AddNode,SubNode,MultNode]
T=list(range(-10,10))
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
mutability=1
Ncompetitors=10

if sys.argv[1]=="singraf":
    engineEncontrarEcuacion(fit3,arbolReal,intervalo,trys,populationLen,Ncompetitors,depth,F,T,mutability)
elif sys.argv[1]=="congraf":
    engineEncontrarEcuacionConGrafico(fit3,arbolReal,intervalo,trys,populationLen,Ncompetitors,depth,F,T,"ecuacionConFit3",mutability)

