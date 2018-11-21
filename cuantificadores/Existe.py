"""
        -Roberto Suárez
        cunatificadores existencial ∃ x, y ...
        Existe al menos un x, y ...
"""

dis = [0.5,1,2,5,8]     # discurso

def esMayor(n):
        if(n**2 > n):
                print("{} > {} ".format(n**2,n))
                return True
        return False

# ∃ x (x**2 > x)
def ExisteAlmenosUno(D):
    for n in D:
        if(esMayor(n)):
            return True

    return False

#print(ExisteAlmenosUno(dis))


"""
        existe al menos un - para todo
        existe al menos una x en Dx tal que P(x,y) es verdadera para toda "y" en Dy     
"""

def es_divisible(x, y):
    if(x % y == 0):
        return True
    return False

def es_mayor(x,y):
        if (x >= y):
                return True
        return False

def P(dx,dy):
        for x in dx:
                cont = 0
                for y in dy:
                        if not es_divisible(x,y):
                                break
                        else:
                                cont += 1
                                if cont == len(dy):
                                        return True
        return False

d1 = [2,3,5,16]
d2 = [2,4]

print(P(d1, d2))