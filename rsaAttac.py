import math

def mod (a, b):
    q = a//b
    r = a - b*q
    r = r + (r < 0) * b
    return r

def euclides (a, b):
    if (mod(a,b) == 0):
	    return b
    else:
	    return euclides(b, mod(a,b));

def extendEu (a,b):
    if (mod(a,b) == 0):
        return (b,0,1)
    else:
        (d, xP, yP) = extendEu(b, mod(a,b))
        (x,y) = (yP, xP-a//b*yP)
        return (d,x,y)

def inverso (a, n):
    (d,xP,iP) = extendEu(a,n)
    if d == 1:
        return mod(xP, n)
    else:
        return a," no tine inv, mul. mod ",n

def expo(a,b, n):
    if b == 1: 
        return mod(a,n)
    Nb = b//2
    res = expo(a,Nb,n)
    if b % 2: 
        return mod(res*res*a, n)
    return mod(res**2, n)

def pot (a,b):
    cont = 0
    res = 1
    while (cont < b):
        res = res * a
        cont = cont +1
    return res


def fact (n):
    for i in range (2, int(math.sqrt(n))):
        while (mod(n,i) == 0):
            n1 = i
            break
    n2 = n//n1
    return (n1,n2)
    
def FirstAttack (c,e,n):
    (p,q) = fact(n)
    phi = (p-1)*(q-1)
    d = inverso(e,phi)

    m = expo(c,d,n)
    return m

def SecondAttack(c1,c2,e1,e2,n):
    
    if (euclides(e1,e2) == 1):
        (d,x,y) = extendEu(e1,e2)
    
        if (euclides(c2,n) == 1):
            cI = inverso(c2,n)
            x = inverso(x,e2);

            if (y<0):
                m = mod(pot(c1,x) * pot(cI,-y),n)
                return m
            else:
                m = mod(pot(c1,-x) * pot(cI,y),n)
                return m
        else:
            return 0
    else:
        return 0

print(fact(999630013489))
print("C -> ",expo(100000000001,65537,999630013489))
print("M -> ",FirstAttack(747120213790,65537,999630013489))
print(SecondAttack(35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544,35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184,7,11,35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667))
