"""
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.
"""

def boolean_to_string(b):
	if b is True: return 'True'
	else: return 'False'


#bien pero más facil:
def boolean_to_string_v2(b):
    return str(b)