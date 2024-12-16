"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

texto1='Hello world !'

def pig_it(text):
	palabras=text.split()
	newpalabras=[]
	for palabra in palabras:
		if palabra=='?' or palabra=='!':
			newpalabras.append(palabra)
		else:
			letras=list(palabra)
			letra1=letras[0]
			letras.remove(letra1)
			letras.append(letra1)
			letras.append('ay')
			newpalabra=''.join(letras)
			newpalabras.append(newpalabra)

	return ' '.join(newpalabras)

print(pig_it(texto1))