"""
Q(1)=Q(2)=1
Q(n)=Q(n-Q(n-1))+Q(n-Q(n-2)), n>2
"""


def hofstadter_Q_yo(n):
	if n<3: return 1 # 1 and 2
	else:
		resultado1= n - hofstadter_Q_yo(n-1) #Q(n-Q(n-1))
		resultado2= n - hhofstadter_Q_yo(n-2) #Q(n-Q(n-2))
		return hofstadter_Q_yo(resultado1) + hofstadter_Q_yo(resultado2) #Q(n-Q(n-1))+Q(n-Q(n-2))

#Mi función es tan ineficiente que no se ejecuta en codewars
#Esta la saca chatgpt. 
#IMPORTANTE cuando haya recursividad tratar de no repetir cálculos, crear un ddd para 
#guardar los resultados ya calculados


def hofstadter_Q(n, memo={}):
    if n < 3:
        return 1
    elif n in memo:
        return memo[n]
    else:
        resultado1 = n - hofstadter_Q(n - 1, memo)
        resultado2 = n - hofstadter_Q(n - 2, memo)
        memo[n] = hofstadter_Q(resultado1, memo) + hofstadter_Q(resultado2, memo)
        return memo[n]