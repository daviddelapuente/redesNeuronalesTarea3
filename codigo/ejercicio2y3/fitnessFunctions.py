from arboles import Node
#funcion fit.
def fit(arbolCandidato,arbolReal,intervalo):
    rate=0
    for i in intervalo:
        d={"x":i}
        if arbolCandidato.eval(d)==arbolReal.eval(d):
            rate+=1
    return rate

def fit2(arbolCandidato,arbolReal,intervalo):

    return fit(arbolCandidato,arbolReal,intervalo)-abs(len(arbolReal.serialize())-len(arbolCandidato.serialize()))*0.2
