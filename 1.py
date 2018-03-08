print ("""
	1. Define a function max() that takes two numbers as arguments and returns the largest of them.
	Use the if-then-else construct available in Python. 
	(It is true that Python has the max() function built in, 
	but writing it yourself is nevertheless a good exercise ).
	""")

def max (a,b):
	if (a>b):
		return a
	else:
		return b

z=max(18,21)
w=str(z)

print ("This function returns the max value between 2 arguments --> 18 & 21")
print ("The max value is: " + w)
# print (w)
print ()