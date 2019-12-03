# redesNeuronalesTarea3

## ejercicio 1 (encontrar un numero)
el ejercicio consiste en encontrar un numero usando solo operaciones aritmeticas basicas.
usando los terminales {25,7,8,100,4,2} y las operaciones {+,−,∗, max(·)} se procede a encontrar el numero 65346.

### con repeticion
el primer experimento es generar un arbol con un numero indeterminado de terminales (se pueden repetir).

para correr el codigo sin graficos:

    debes estar en la carpeta ejercicio1 y correr el siguiente codigo en la terminal
    
            python3 probandoEjercicio1.py singraf conrep sincast  65346

    con esto buscaras el numero 65346 con repeticion de terminales (puedes buscar cualquier numero)
    en la terminal se mostrara el arbol encontrado, el fitness (mientras mas cercano a 0 mejor) y la evaluacion de el arbol.

para correr el codigo con graficos:
    debes estar en el ambiente virtual e instalar los requirements
    luego debes dirigirte a la carpeta ejercicio1 y correr en la terminal

            python3 probandoEjercicio1.py congraf conrep sincast  65346

    con esto buscaras el numero 65346 con repeticion de terminales (puedes buscar cualquier numero)
    en la terminal se mostrara el arbol encontrado, el fitness (mientras mas cercano a 0 mejor) y la evaluacion de el arbol.
    y se creare una imagen llamada fitnessEvolConrep.png en la carpeta ejercicio1.

analisis:
![alt text][fit1]

[fit1]: codigo/ejercicio1/fitnessEvolConrep.png


para este grafico se uso la funcion fit1, que puede encontrarse en el archivo fitnessFunctions en la carpeta ejercicio1. es una funcion bastante simple que lo que hace es calcular que tan lejos esta la evaluacion de el arbol con el numero buscado.
(el grafico es el fitness de los maximos de cada generacion y el maximo que pueden alcanzar es 0).


### con repeticion y castigo por largo de arbol

el siguiente experimento es generar un arbol con un numero indeterminado de terminales (se pueden repetir) pero se castigara si el arbol es muy largo.

para correr el codigo sin graficos:

    debes estar en la carpeta ejercicio1 y correr el siguiente codigo en la terminal
    
            python3 probandoEjercicio1.py singraf conrep concast  65346

    con esto buscaras el numero 65346 con repeticion de terminales (puedes buscar cualquier numero)
    en la terminal se mostrara el arbol encontrado, el fitness (mientras mas cercano a 0 mejor) y la evaluacion de el arbol.

para correr el codigo con graficos:
    debes estar en el ambiente virtual e instalar los requirements
    luego debes dirigirte a la carpeta ejercicio1 y correr en la terminal

            python3 probandoEjercicio1.py congraf conrep concast  65346

    con esto buscaras el numero 65346 con repeticion de terminales (puedes buscar cualquier numero) pero ademas castigaras a los arboles muy largos
    en la terminal se mostrara el arbol encontrado, el fitness (mientras mas cercano a 0 mejor) y la evaluacion de el arbol.
    y se creare una imagen llamada fitnessEvolConrepConcast.png en la carpeta ejercicio1.

analisis:

![alt text][fit2]

[fit2]: codigo/ejercicio1/fitnessEvolConrepConcast.png


para este grafico se uso la funcion fit2, que puede encontrarse en el archivo fitnessFunctions en la carpeta ejercicio1. es una funcion bastante simple que lo que hace es calcular que tan lejos esta la evaluacion de el arbol con el numero buscado, pero ademas se le resta el largo de el arbol/100 (el 100 aparece empiricamente, ya que los tamanos de los arboles pueden ser muy grandes y matan la funcion fitness).
(esta vez el maximo puede no ser 0 pues al restar el largo de el arbol, nos alejamos de el 0). 

### sin repeticion

el siguiente experimento es generar un arbol con un numero fijo de terminales (no se pueden repetir) (no se castiga por largo ya que al castigar por terminales
repetidos se esta castigando por largo) (los terminales se mantienen pero se elimina la funcion max()).

para correr el codigo sin graficos:

    debes estar en la carpeta ejercicio1 y correr el siguiente codigo en la terminal
    
            python3 probandoEjercicio1.py singraf sinrep 65346

    con esto buscaras el numero 65346 sin repeticion de terminales (puedes buscar cualquier numero)
    en la terminal se mostrara el arbol encontrado, el fitness (mientras mas cercano a 0 mejor) y la evaluacion de el arbol.

para correr el codigo con graficos:
    debes estar en el ambiente virtual e instalar los requirements
    luego debes dirigirte a la carpeta ejercicio1 y correr en la terminal

            python3 probandoEjercicio1.py congraf sinrep 65346

    con esto buscaras el numero 65346 sin repeticion de terminales (puedes buscar cualquier numero)
    en la terminal se mostrara el arbol encontrado, el fitness (mientras mas cercano a 0 mejor) y la evaluacion de el arbol.
    y se creare una imagen llamada fitnessEvolsinrep.png en la carpeta ejercicio1.

analisis:

![alt text][fit3]

[fit3]: codigo/ejercicio1/fitnessEvolsinrep.png


para este grafico se uso la funcion fit3, que puede encontrarse en el archivo fitnessFunctions en la carpeta ejercicio1. es una funcion un poco mas compleja, pero lo que hace es contar el numero de terminales repetidos y se los resta la distancia entre el numero buscado y la evaluacion de el arbol, ponderado por 2000 (el cual se encontro empiricamente). se puede observar tambien que el grafico es mucho menos inestable y alcanza peores evaluaciones que los anteriores fitness, pero se gana mucho encuanto a memoria de el arbol.

## ejercicio 2 y 3

como queremos soportar evaluaciones de variables, se agrego un diccionario a la evaluacion de los nodos terminales (en el archivo arboles.py).
para esto, todo nodo no terminal al momento de evaluar recibe un diccionario (con las respectivas llaves y valores numericos), luego evalua a sus hijos con este diccionario, por ultimo en el nodo terminales se pregunta si el valor de el nodo es un string, de ser asi se usa ese valor como llave en el diccionario.

### symbolic regresion

para este ejercicio lo que haremos sera buscar un arbol que represente la funcion (x*x+x-6)=arbolReal. usaremos como terminales [-10,...,10] U {x} y como funciones {+,-,*}.

se hicieron 3 experimentos con 3 funciones fitness distintas (las que se pueden ver en el archivo fitnessFunctions.py de la carpeta ejercicio2y3).
la primera funcion fue bastante basica, y lo que hace es evaluar en el intervalo [-100,...,100] todos los puntos de el arbolReal y las de el arbol que se esta probando y contar cuantos aciertos tiene.
veamos la evolucion de su fitness.

analisis:

![alt text][fit4]

[fit4]: codigo/ejercicio2y3/ecuacionConFit1.png

como podemos observar en el grafico, la mayoria de las veces el fit es de 0, 1 o 2 representando la cantidad de veces que las 2 funciones se tocan (notamos que el mejor caso es 200 cuando se tocan en todos los puntos pero es casi improbable que eso ocurra! almenos con este fit)

es por esto que se cambia la funcion fitness. con la funcion fit2, se hace lo mismo que con fit1 pero se castiga si el largo de el arbol que se esta evaluando es muy distinto de el arbolReal (esto bajo el supuesto de que los arboles deben parecerse en altura)
veamos la evolucion de el nuevo fitness.




![alt text][fit5]

[fit5]: codigo/ejercicio2y3/ecuacionConFit2.png

el nuevo grafico nos muestra un fitness que sube un poquito a lo largo de el tiempo, si bien las funciones siguen siendo muy distintas, el largo de los arboles ya no es tan distinto, por lo que los posibles arboles que se forman al azar, tienen mas probabilidad de parecerse al arbol que buscamos. :)

cambiando un poco el paradigma de como buscar la funcion, esta vez se cambia a una funcion fit3 que lo que hace es por cada punto en [-100,100] calcular la diferencia entre la evaluacion de el arbol real y nuestro arbol, esto nos da mucha mas versatilidad al momento de buscar (pues puedes tener una funcion que toca en 2 puntos a la funcion real, sin embargo esta trasladada), incluso aveces encontramos el arbol buscado!
veamos la evolucion de el nuevo fitness


 
![alt text][fit6]

[fit6]: codigo/ejercicio2y3/ecuacionConFit3.png


![alt text][encontrada]

[encontrada]: codigo/ejercicio2y3/encontrado.png


para correr el codigo sin graficos:

    debes estar en la carpeta ejercicio2y3 y correr el siguiente codigo en la terminal
    
            python3 probandoEjercicio2.py singraf

    con esto buscaras la funcion x*x + x -6 usando la funcion fit3 que es la mejor de las 3
    en la terminal se mostrara el arbol encontrado y el fitness.

para correr el codigo con graficos:
    debes estar en el ambiente virtual e instalar los requirements
    luego debes dirigirte a la carpeta ejercicio2y3 y correr en la terminal

            python3 probandoEjercicio2.py congraf

    con esto buscaras la funcion x*x + x -6 usando la funcion fit3 que es la mejor de las 3
    en la terminal se mostrara el arbol encontrado y el fitness
    y se creare una imagen llamada ecuacionConFit3.png en la carpeta ejercicio2y3. 


## ejercicio 4
en este ejercicio se busca resolver el mismo problema de el ejercicio 2y3, pero se agrega un nodo de division. el cual se puede observar en el archivo arboles.py de la carpeta ejercicio4.

para evitar castigar a los nodos que dividen por 0, se hace una funcion fitness que se comporta como la funcion fit3 de el ejercicio 3, con la diferencia que cuando evalua un nodo de division, si este divide por 0, atrapa la exepcion y castiga fuertemente al arbol (queremos que se muera).

![alt text][fit10]

[fit10]: codigo/ejercicio4/ecuacionConFit4.png


como se puede observar en la imagen, la mayoria de los fitness se mantienen cercano al 0, y cuando aparece una division por 0, el algoritmo la soporta y la erradica.


para correr el codigo sin graficos:

    debes estar en la carpeta ejercicio4 y correr el siguiente codigo en la terminal
    
            python3 probandoEjercicio4.py singgraf

    con esto buscaras la funcion x*x + x -6 usando la funcion fit4 que se puede encontrar en el archivo fitnessFunctions.py de la carpeta ejercicio4
    en la terminal se mostrara el arbol encontrado y el fitness.

para correr el codigo con graficos:
    debes estar en el ambiente virtual e instalar los requirements
    luego debes dirigirte a la carpeta ejercicio4 y correr en la terminal

            python3 probandoEjercicio4.py congraf

    con esto buscaras la funcion x*x + x -6 usando la funcion fit4
    en la terminal se mostrara el arbol encontrado y el fitness
    y se creare una imagen llamada ecuacionConFit4.png en la carpeta ejercicio4.

## heatmap
para hacer el heatmap se eligio el problema 1 de el ejercicio 1 de encontrar el numero 65346, usando la funcion fit1 (la que no castiga y es con repeticion de terminales), se eligio esta funcion porque es la que tiene mas capacidad al momento de encontrar el numero.

![alt text][heat]

[heat]: codigo/ejercicio1/heatmap.png

como se puede observar en el heatmap, se hicieron 100 iteraciones para 10 poblaciones distintas con 10 mutaciones distintas cada una.
en el heatmap se grafica cuanto se demora el motor genetico en encontrar el numero 65346 (los colores frios representan las combinaciones que encuentran mas rapido el numero) y podemos observar que la mitad de abajo es donde mas rapido se encuentra el numero buscado es decir el numero de la poblacion influye mucho mas que las mutaciones. (al menos las mutaciones implementadas segun el enunciado).

para correr el codigo con graficos:
    debes estar en el ambiente virtual e instalar los requirements
    luego debes dirigirte a la carpeta ejercicio1 y correr en la terminal

            python3 heatmap.py 

    con esto buscaras el numero 65346 con la funcion fit1 que se encuentra en el archivo fitnessFunctions.py en la carpeta ejercicio1
    (advertencia el programa se demora como 30 min en correr)