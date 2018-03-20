print ('''

	9. Write a function is_member() that takes a value ( i.e. a number, string, etc ) x 
	and a list of values a, and returns True if x is a member of a, False otherwise. 
	(Note that this is exactly what the 'IN' operator does, 
	but for the sake of the exercise you should pretend Python did not have this operator).

	''')

def is_member(x, a):
	
	print ('\nThe value x is:			', x)
	print ('The list of values are:		', a)
	i = 0
	s = len(a)
	while i < s:
		if ( a[i] == x ):
			return True
		else:
			i += 1
	return False

val = 'zxy'
l_val = [453, 'Python', 9, 'zxy', 21]
ans = is_member(val, l_val)

print ('Is a member of the list?	', ans)
print ()