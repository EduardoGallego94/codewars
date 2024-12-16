"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will 
result in a hexadecimal representation being returned. Valid decimal values for RGB are 
0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
"""


def rgb(r, g, b):
	if r<0: r=0
	elif r>255: r=255
	if g<0: g=0
	elif g>255: g=255
	if b<0: b=0
	elif b>255: b=255

	return f'{r:02X}{g:02X}{b:02X}'

print(rgb(148, 0, 211))