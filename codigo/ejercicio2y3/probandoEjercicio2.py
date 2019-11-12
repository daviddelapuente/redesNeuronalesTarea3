from encontrarEcuacion import *
from fitnessFunctions import fit
from fitnessFunctions import fit2

arbolReal=SubNode(AddNode(MultNode(TerminalNode("x"),TerminalNode("x")),TerminalNode("x")),TerminalNode(6))
intervalo=range(-100,100)
trys=20
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

engineEncontrarEcuacion(fit2,arbolReal,intervalo,trys,populationLen,Ncompetitors,depth,F,T,mutability)
