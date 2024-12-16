"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
"""

def basic_op(operator, value1, value2):

	if operator == '+':
		resultado = value1 + value2
	elif operator == '-':
		resultado = value1 - value2
	elif operator == '*':
		resultado = value1 * value2
	elif operator == '/':
		try:
			resultado = value1 / value2
		except:
			resultado = 'Dividete por cero'
	else:
		resultado = "Operador no válido"

	return resultado
