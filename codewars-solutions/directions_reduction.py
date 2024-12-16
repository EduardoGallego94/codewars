"""
Write a function dirReduc which will take an array of strings and returns an array of 
strings with the needless directions removed (W<->E or S<->N side by side).
"""
direcciones=["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

def dirReduc(direcciones):

	ddd={
		'NORTH':'SOUTH',
		'SOUTH':'NORTH',
		'EAST':'WEST',
		'WEST':'EAST'
	}

	pila=[]

	for direccion in direcciones:
		if pila and pila[-1]==ddd.get(direccion):
			pila.pop() #elimina la última dirección
		else:
			pila.append(direccion) #añade la dirección actual a la pila

	return pila