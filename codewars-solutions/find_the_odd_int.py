"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

def find_it(seq):
	ddd={}
	for i in seq:
		if i in ddd:
			ddd[i]+=1
		else:
			ddd[i]=1

	for i,x in ddd.items():
		if x%2!=0:
			return i
