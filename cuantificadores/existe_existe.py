"""
	Existe - Existe
	∃x, ∃y | x % y == 0
"""

# func que verifica si x es divible para y.
def es_divisible(x, y):
    if(x % y == 0):
        return True
    return False

def P(dx,dy):
        for i in dx: # listamo el discurso dx
                for j in dy:	# listamo el discruso dy
                	if es_divisible(i, j):
                		return True
                	else:
                		break
        return False


d1 = [1,3,5,7]		# Discurso uno 
d2 = [2,4,6]		# discruso dos

print(P(d1, d2))