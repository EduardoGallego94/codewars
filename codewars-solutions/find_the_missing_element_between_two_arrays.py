"""
Given two integer arrays where the second array is a shuffled duplicate of the first array
with one element missing, find the missing element.

Please note, there may be duplicates in the arrays, so checking if a numerical value exists
in one and not the other is not a valid solution.
find_missing([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]) => 8
"""

from collections import Counter

def find_missing(arr1, arr2):
	lista=arr1+arr2 #join arrays
	ddd=Counter(lista) #dict convert

	for e, v in ddd.items(): #for loop in dict
		if v % 2 != 0: #if the counter is ood return key value
			return e
		else:
			continue


#Bien pero más facil esto:
def find_missing(arr1, arr2):
    return sum(arr1) - sum(arr2)