"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' 
comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels 
removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""

def disemvowel(string_):
	a= string_.replace('a','')
	e= a.replace('e','')
	i= e.replace('i','')
	o= i.replace('o','')
	u= o.replace('u','')
	A= u.replace('A','')
	E= A.replace('E','')
	I= E.replace('I','')
	O= I.replace('O','')
	return O.replace('U','')

#esta mejor:
def disemvowel_v2(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s