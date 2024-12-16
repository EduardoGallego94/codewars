"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses 
between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always 
be greater than the first one.
"""

def ips_between(start, end):

	ip1=start.split('.')
	ip2=end.split('.')

	numip1=[]
	numip2=[]

	for i in ip1:
		num=int(i)
		numip1.append(num)

	for i in ip2:
		num=int(i)
		numip2.append(num)

	return (numip2[0]-numip1[0])*256**3+(numip2[1]-numip1[1])*256**2+(numip2[2]-numip1[2])*256+(numip2[3]-numip1[3])
