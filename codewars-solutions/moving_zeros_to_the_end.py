"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving 
the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

lista=[1, 0, 1, 2, 0, 1, 3]

def move_zeros(lst):
	newlist1=[]
	newlist2=[]
	for i in lst:
		if i == 0:
			newlist2.append(i)
		else:
			newlist1.append(i)

	return newlist1+newlist2

print(move_zeros(lista))