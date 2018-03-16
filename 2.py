print ('''

	2. Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
	
	''')

def max_of_three(a, b, c):
	
	if (a > b):
		if (a > c):
			return a
	elif (b > c):
			return b
	else:
		return c

z = max_of_three(15, 30, 45)
w = str(z)

print ('This function returns the max value between 3 arguments --> 15, 30 y 45')
print ('The max value is: ' + w)
#print (w)

