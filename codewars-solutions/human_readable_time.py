"""
Write a function, which takes a non-negative integer (seconds) as input and returns the 
time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

def make_readable(seconds):
	hh = seconds // (60*60)
	mm = (seconds % (60*60)) // 60
	ss = seconds % 60

	return (f'{hh:02}:{mm:02}:{ss:02}')

print(make_readable(59))