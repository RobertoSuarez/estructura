""" 
	para todo - existe
	∀x, ∃y | x % y == 0
"""

# func que verifica si x es divible para y.
def es_divisible(x, y):
    if(x % y == 0):
        return True
    return False

def P(dx,dy):
	for i in dy:
		cont = 0
		for j in dx:
			if es_divisible(i,j):
				cont += 1	# agregamos 1 al contador
				if cont == len(dx):	# y si todos los elementos de dy son divisibles entoces retorna verdadero
					print("{} es dibisible para {}".format(i, dx))
					return True
			else:
				break
	return False   
# un numero de dx deve ser divisible para todos los numeros de dy.
dx = [2,2,4]		# Discurso x 
dy = [2,4,16]		# discruso y

print(P(dx, dy))