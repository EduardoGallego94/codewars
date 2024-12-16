"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""

def solution (number):

	if number < 0:
		return 0

	else:

		x = 1

		lista = []

		while x < number: # tb for x in range(number): (o incluso x for x in range(number))
			if x % 3 == 0 or x % 5 == 0:
				lista.append(x)
			x += 1

		resultado = 0

		for e in lista:
			resultado += e

		return resultado

