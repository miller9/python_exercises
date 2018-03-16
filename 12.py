print ("""

	12. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
	For example, histogram( [ 4, 9, 7 ] ) should print the following:
		****
		*********
		*******

	""")

def histogram (l):

	for value in l:
		print ("*" * value)

int_list = [4,9,7]
print ("The histogram of the list:", int_list, "is:")
histogram(int_list)
print ()

