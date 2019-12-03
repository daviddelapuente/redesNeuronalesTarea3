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


def fit3(ac,ar,intervalo):
    rate=0
    for i in intervalo:
        d={"x":i}
        rate+=abs(ac.eval(d)-ar.eval(d))
    return -1*rate


def fit4(ac,ar,intervalo):
    rate=0
    for i in intervalo:
        try:
            d={"x":i}
            rate+=abs(ac.eval(d)-ar.eval(d))
        except ZeroDivisionError:
            rate+=999999999
    return -1*rate
