import random


def modulo (a, b):
    q = a//b
    r = a - b*q
    r = r + (r < 0) * b
    return r

def ext (a,b):
    if (modulo(a,b) == 0):
        return (b,0,1)
    else:
        (d, xP, yP) = ext(b, modulo(a,b))
        (x,y) = (yP, xP-a//b*yP)
        return (d,x,y)
    
def euclides (a, b):
    if (modulo(a,b) == 0):
	    return b
    else:
	    return euclides(b, modulo(a,b));

def nprimo (a):
    if a < 1:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True      

def inversa (a, n):
    (d,xP,iP) = ext(a,n)
    if d == 1:
        return modulo(xP, n)
    else:
        return a," no tine inversa, mul. modulo ",n
    
def getPrime ():
    nro = random.randint(2,100)
    while(nprimo(nro) == False):
        nro = nro + random.randint(2,100)
    return nro

def expM(a,b, n): #a se refiere (base), b se refiere (exponente) y n se refiere (módulo)
    if b == 1: 
        return modulo(a,n)
    Nb = b//2
    res = expM(a,Nb,n)
    if b % 2: 
        return modulo(res*res*a, n)
    return modulo(res**2, n)

def Generator ():

    print("Ingrese el valor de p: ")
    p = int(input())
    while (nprimo(p) == False):
        print("Ingrese un valor PRIMO para p: ")
        p = int(input())
    
    print("Ingrese el valor de q: ")
    q = int(input())
    while(nprimo(q) == False):
        print("Ingrese un valor PRIMO para q: ")
        q = int(input())
        
    
    
    while (p == q): #verificar si p != q, caso contrario, cambiar valor de p
        print("Ingrese un valor PRIMO para p, diferente de q: ")
        p = int(input())


    print("p: ",p)
    print("q: ",q)
    print("Ingrese un mensaje menor a " ,p*q)
    mensaje = int(input())
    
    return (p,q , mensaje)

def cifrar ():
    
    (p,q , mensaje) = Generator()
    
   
    n = p * q  #Aqui calcularemos n
    print("n: ",n)
    
    if (mensaje > n):
        print("***Por favor ingresar un nuevo mensaje. El mensaje debe ser menor al valor de ", n)
        return 1
    
    phin = (p-1)*(q-1) #Aqui Calculamos phi de n
    print("Phi: ",phin)


    e = getPrime()  #Aqui calcularemos E
    while (e <= 2 or e >= n-1 or euclides(e,phin) != 1): #verificar que: 2<e<n-1
        e = getPrime()
    print("e: ",e)


    d = inversa(e,phin)  #aqui calcularemos D
    print("d: ",d)

    
    m = mensaje

    
    c = expM(m,e,n)



    print("Mensaje a cifrar: ",mensaje)
    print("Mensaje a cifrado: ",c)

    return (n,e,d,c)

def decifrado(n,e,d,c):
    
    m = expM(c,d,n)

    print("Mensaje descifrado: ",m)
    
    return (m)




(N,E,D,Cif) = cifrar()
decifrado(N,E,D,Cif)

