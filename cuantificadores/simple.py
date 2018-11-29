"""
        - Roberto Suárez
        cunatificadores existencial ∃ x, y ...
        Existe al menos un x, y ...
        Existe al menos una x mayor que x**2 en el discurso

"""

dis = [0.5,1,2,5,8]     # discurso

# verifica si n al cuadrado es mayor que n.
def esMayor(n):
        if(n**2 > n):
                print("{} ({}**2) > {} ".format(n**2,n,n))
                return True
        return False

# ∃ x | (x**2 > x)
def ExisteAlmenosUno(D):
    for n in D:
        if(esMayor(n)):
            return True

    return False

print(ExisteAlmenosUno(dis))


