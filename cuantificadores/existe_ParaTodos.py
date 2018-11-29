"""
		existe - para todo
        existe al menos un - para todo
        existe al menos una x en Dx tal que P(x,y) es verdadera para toda "y" en Dy 
        ∃x, ∀y | x % y == 0    
"""

# func que verifica si x es divible para y.
def es_divisible(x, y):
    if(x % y == 0):
        return True
    return False

def P(dx,dy):
        for x in dx: # listamo el discurso dx
                cont = 0
                for y in dy:	# listamo el discruso dy
                        if not es_divisible(x,y):	# si no es divisble entonces que se salte esta iteración
                                break
                        else:	# si es dibisible entoces 
                                cont += 1	# agregamos 1 al contador
                                if cont == len(dy):	# y si todos los elementos de dy son divisibles entoces retorna verdadero
                                        print("{} es dibisible para {}".format(x, dy))
                                        return True
        return False

d1 = [2,3,5,16]		# Discurso uno 
d2 = [2,4]		# discruso dos

print(P(d1, d2))