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
Reference-style: 
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
Reference-style: 
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
Reference-style: 
![alt text][fit3]

[fit3]: codigo/ejercicio1/fitnessEvolsinrep.png


para este grafico se uso la funcion fit3, que puede encontrarse en el archivo fitnessFunctions en la carpeta ejercicio1. es una funcion un poco mas compleja, pero lo que hace es contar el numero de terminales repetidos y se los resta la distancia entre el numero buscado y la evaluacion de el arbol, ponderado por 2000 (el cual se encontro empiricamente). se puede observar tambien que el grafico es mucho menos inestable y alcanza peores evaluaciones que los anteriores fitness, pero se gana mucho encuanto a memoria de el arbol.

## ejercicio 2

## ejercicio 3

## ejercicio 4

## heatmap
