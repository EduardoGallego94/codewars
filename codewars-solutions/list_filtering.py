"""
In this kata you will create a function that takes a list of non-negative integers and strings 
and returns a new list with the strings filtered out.
"""

def filteredlist(l):
	#return a new list with the strings filtered out
	newlist=[]
	for i in l:
		if type(i) == int:
			newlist.append(i)
		else:
			continue
	return newlist

lista=[1,2,'aasf','1','123',123]

print(filteredlist(lista))