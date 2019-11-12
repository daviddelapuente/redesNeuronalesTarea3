from astD import *
from arboles import *

#funcion fit.
def fit1(arbol,n,a):
    return -1*abs(arbol.eval()-n)


def fit2(arbol,n,a):
    return fit1(arbol,n,a)-len(arbol.serialize())/100

     

def getRepetidos(n,terminales,respuesta):
    if isinstance(n,TerminalNode):
        for j in range(len(terminales)):
            if terminales[j]==n.eval():
                respuesta[j]+=1
        return respuesta
    else:
        getRepetidos(n.getArguments()[0],terminales,respuesta)
        getRepetidos(n.getArguments()[1],terminales,respuesta)
        return respuesta

def listSumAll(l):
    c=0
    for i in l:
        c+=i
    return c

def fit3(arbol,number,a):
    terminales=a.getTerminales()
    zeros=[]
    for t in terminales:
        zeros.append(0)
    
    r=getRepetidos(arbol,terminales,zeros)
    return fit2(arbol,number,a)-1*listSumAll(r)*2000



