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

print(ExisteAlmenosUno(dis))