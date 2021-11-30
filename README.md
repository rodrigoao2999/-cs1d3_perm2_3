# RSA

### Codigo de la tarea => RSA.cpp

1. Pedimos al usuario que ingrese 2 numeros primos.
2. El siguiente paso es calcular n con la formula -> n=p*q.
3. Despues tenemos que calcular phi de n con la formula aprendida en clase -> phi_n=(p-1)*(q-1).
4. Generamos aleatoriamente una e entre 2 y n-1 y se quedara en bucle mientras no se cumpla que el maximo como un divisor entre e y phi_n ==1.
5. Despues de caclcularlo y terminar el bucle tenemos que hallar d aplicando el algoritmo de inversa que ya lo hicimos anteriormente.
6. Y asi tendriamos como resultado los valores de n, e y d.

Todo el desarrollo de este algoritmo lo hice en la funcion main por ende no se requeria un return.

Tabla de contenido de valores del mensaje cifrado y descifrado para los siguientes valores {e,d,n} {11,11,33}.

|Variables|resultados|
|-----------|---------|
|m | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32|
|c|0, 1, 2, 3, 4, 5, 6, 7, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31|
|m|0, 1, 2, 3, 4, 5, 6, 7, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31|


Se repite que m^e mod n =m en los 32 casos.

Observaciones:

1. El programa al parecer presenta fallos con el tipo de variable declarado para realizar los algoritmos y por ello que se observa que para esos datos obtenemos continuamente 31.
