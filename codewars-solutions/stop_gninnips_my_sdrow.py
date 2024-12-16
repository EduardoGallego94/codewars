"""
Write a function that takes in a string of one or more words, and returns the same string, 
but with all words that have five or more letters reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when 
more than one word is present.
"""

def spin_words(sentence):
	lista=sentence.split()
	listaResultado=[]

	for word in lista:
		if len(word)>4:
			rev_word=word[::-1]
			listaResultado.append(rev_word)
		else:
			listaResultado.append(word)

	return ' '.join(listaResultado)
