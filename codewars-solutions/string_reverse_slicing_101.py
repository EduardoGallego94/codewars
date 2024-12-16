"""
You'll be given a string of characters as an input. Complete the function that returns a list of strings: (a) in the reverse order of the original string, and (b) with each successive string starting one character further in from the end of the original string.

Assume the original string is at least 3 characters long. Try to do this using slices and avoid converting the string to a list.

Examples
'123'   ==>  ['321', '21', '1']
'abcde' ==>  ['edcba', 'dcba', 'cba', 'ba', 'a']
"""

def reverse_slice(s): #Ej. 'abcde'
	longitud = len(s) #5
	count=0
	lista=[]
	corte=longitud-1 #4
	while count < longitud: #0<5-1
		lista.append(s[corte::-1])
		count+=1 #1
		corte-=1 #3
		continue
	return lista

def reverse_slice_v2(s): #Ej. 'abcde'
	longitud = len(s) #5
	lista=[]
	for i in range(longitud): #for i in range(5)
		lista.append(s[i::-1]) #[0::-1]
		continue
	return lista[::-1]
