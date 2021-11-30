# cs1d3_perm2_3

### rsa.py
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

### rsaAttac.py

#### Este archivo contiene el ataque y las funciones utilizadas son las siguientes :
##### 1-. factorizator(), que hace factorizaciones mediante prueba y error. Una vez obtenidos los factores de n (p y q), obtenemos Phi de n, y con ello obtenemos d (inversa de e en mod phi) y realizamos la operación m = c^d mod n
##### 2-. Verifica si el gcd de e1 y e2 es 1 (si son coprimos). En caso sea así, procede a verificar que c2 y n sean coprimos para calcular la inversa de c2. Se calcula la inversa de x. Tras esto se calcula m mediante la operación m = (c1^x * c2'^-y) mod n si es que y<0 o m = (c1^-x * c2'^y) mod n si x>0
##### 3-. Las potenciaciones requeridas en attack2 son muy grandes, por lo que se genera un overflow, para evitar dicho problema se creó la función Mypow. Dicha función realiza lo mismo que la función pow convencional, con la excepción de no convertir los valores a tipo float, esto permite evitar dicho overflow.
