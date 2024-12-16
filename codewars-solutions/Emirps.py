"""
If you reverse the word "emirp" you will have the word "prime". That idea is related with the purpose of this kata: we should select all the primes that when reversed are a different prime (so palindromic primes should be discarded).

For example: 13, 17 are prime numbers and the reversed respectively are 31, 71 which are also primes, so 13 and 17 are "emirps". But primes 757, 787, 797 are palindromic primes, meaning that the reversed number is the same as the original, so they are not considered as "emirps" and should be discarded.

The emirps sequence is registered in OEIS as A006567

Your task
Create a function that receives one argument n, as an upper limit, and the return the following array:

[number_of_emirps_below_n, largest_emirp_below_n, sum_of_emirps_below_n]
"""

def find_emirp(n):

#-----------------------------------------------

	def criba_de_eratostenes(limite): #obtiene todos los primos por debajo del limite
	    primos = set()
	    es_primo = [True] * (n + 1)
	    
	    # 0 y 1 no son primos
	    es_primo[0] = es_primo[1] = False
	    
	    for p in range(2, n + 1):
	        if es_primo[p]:
	            primos.add(p)
	            for multiple in range(p * p, n + 1, p):
	                es_primo[multiple] = False
	                
	    return primos

#-----------------------------------------------

	def es_primo(n): #devuelve un booleano sobre si n es primo
	    # Los números menores que 2 no son primos
	    if n < 2:
	        return False
	    # El número 2 es primo
	    if n == 2:
	        return True
	    # Los números pares mayores que 2 no son primos
	    if n % 2 == 0:
	        return False
	    # Comprobar divisibilidad desde 3 hasta la raíz cuadrada del número
	    for i in range(3, int(n**0.5) + 1, 2):
	        if n % i == 0:
	            return False
	    return True

#-----------------------------------------------

	n_2=n*2

	set_primos=criba_de_eratostenes(n_2)

	lista=[]

	for i in set_primos:
		inv=int(str(i)[::-1])
		if inv == i:
			continue
		else:
			if es_primo(inv): lista.append(i)



	return [len(lista), max(lista), sum(lista)] #[amount of emirps in the range(13, n + 1), largest emirp smaller than n, sum of all the emirps of this range.






