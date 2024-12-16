"""
You're playing to scrabble. But counting points is hard.

You decide to create a little script to calculate the best possible value.

The function takes two arguments :

`points` : an array of integer representing for each letters from A to Z the points that it pays
`words` : an array of strings, uppercase

You must return the index of the shortest word which realize the highest score.
If the length and the score are the same for two elements, return the index of the first one.
"""
def get_best_word(points, words):
	abc='a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
	ABC=abc.upper()
	lista_ABC=ABC.split(', ')

	ddd=dict(zip(lista_ABC,points))

	lista_valores_words=[]
	for word in words:
		letras=list(word)
		valor_word= 0
		for letra in letras:
			valor_word += ddd[letra]
		lista_valores_words.append(valor_word)

	indice_max=[]
	for i in range(len(lista_valores_words)):
		if lista_valores_words[i] == max(lista_valores_words):
			indice_max.append(i)

	longitud=1000
	for indice in indice_max:
		if len(words[indice]) < longitud:
			resultado = indice
			longitud = len(words[indice])

	return resultado

#----------------------------------------------------------------#

from string import ascii_uppercase as uppercase

def get_best_word_v2(points, words):
    points = dict(zip(uppercase, points))
    
    score = lambda word: sum(points[c] for c in word)
    
    return words.index(sorted(sorted(words, key=len), key=score, reverse=True)[0])