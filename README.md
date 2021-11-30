# cs1d3_perm2_3

## rsa.py
#### Este archivo realiza el cifrado de enteros y a continuacion explicare los metodos implementados: 

##### 1-. Importandos la libreria random
##### 2-. funcion modulo la cual calcula el modulo entre a y b
##### 3-. La funcion euclides realiza el max comun divisor entre a y b
##### 4-. Con la funcion ext retornamos valores de a, x, b, y, d = mcd entre a y b, en la expresión lineal ax + by = d
##### 5-. La funcion inversa como su nombre lo dice nos retornara la inversa multiplicativa del entero a en módulo n
##### 6-. En la funcion n primo lo unico que realizo es verificar si el numero es primo o no
##### 7-. getPrime con esta función random generará un entero y con la funcion nprimo se verificara si este numero es primo en caso no fuese primo, se genera un número nuevamente y se suma al número anterior, así hasta que la suma sea un número primo
##### 8-. Con la funcion expM lo que haremos sera calcular la exponenciación modular de a elevado a b en mod n
##### 9-. En la funcion generador lo que nos ayudara sera pedir al usuario que ingrese los valores de p y q , con lo cual se verificaran si estos son primos y si son iguales se pedira que se ingrese p otra vez.
##### 10-. la funcion cifrar lo que hara es que con los valores de p y q que el usuario ingreso, calcularemos n con la formula aprendida, n=p*q, phin = (p-1)*(q-1), e (un número random entre 2 a n-1), d (inversa de e en mod phin). Y se cifra el mensaje con la operación de exponenciación modular c = m^e mod n. Y se retornan lo valores de n,e,d,c
##### 11-. la funcion decifrado hara que los valores obtenidos de la función cifrado se descifra el mensaje c, mediante la operación m = c^d mod n 

## rsaAttac.py

#### Este archivo contiene el ataque y las funciones utilizadas son las siguientes :
##### 1-.FirstAttack es la funcion con la cual si queremos tener m tendremos que tener los factores de ny esto lo vamos a tener con la funcion factorizador(), lo que hara sera realizar factorizaciones por el metodo de prueba y error y cuando los factores de n (p y q), obtenemos Phi de n, y con ello obtenemos d (inversa de e en mod phi) y realizamos la operación m = c^d mod n
##### 2-. SecondAttack si el MCD de e1 y e2 es 1 (si son coprimos). Si pasa eso entonces se verifica que n y c2 sean coprimos y asi podamos calcular la inversa de c2. Se calcula la inversa de x y realizado eso se calcula m mediante la operación m = (c1^x * c2'^-y) mod n si es que y<0 o m = (c1^-x * c2'^y) mod n si x>0
##### 3-. Cuando queremos hacer potenciacion en SecondAttack los valores son muy extensos y eso nos da un overflow, y para no tener ese pproblema hice la funcion pot y esta funcion lo que hace es o mismo que  la funcion pow que todos conocemos pero  no convierte los valores en float y aasi no se dara el overflow. 
