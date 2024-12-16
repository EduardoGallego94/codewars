"""
For this reason, it is usually a good idea to check for and remove outliers before computing 
the mean or the standard deviation of a sample. To this aim, your function will receive a 
list of numbers representing a sample of data. Your function must remove any outliers and 
return the mean of the sample, rounded to two decimal places (round only at the end).

Since there is no objective definition of "outlier" in statistics, your function will also 
receive a cutoff, in standard deviation units. So for example if the cutoff is 3, then any 
value that is more than 3 standard deviations above or below the mean must be removed. 
Notice that, once outlying values are removed in a first "sweep", other less extreme values 
may then "become" outliers, that you'll have to remove as well!
"""

sample1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000]
cutoff1 = 3

def clean_mean(sample, cutoff):

	def desviacion(sample):
		N=len(sample)
		media= sum(sample)/N 
		suma_diferencias=0
		for i in sample:
			suma_diferencias += (i-media)**2
		return (suma_diferencias/N)**0.5 #sigma

	i=0
	while i < len(sample):

		media= sum(sample)/len(sample)
		desv= desviacion(sample)

		if sample[i] < media-desv*cutoff or sample[i] > media+desv*cutoff:
				del sample[i]
				i=0
		else:
			i+=1

	return round(sum(sample)/len(sample),2) 

print(clean_mean(sample1, cutoff1))

