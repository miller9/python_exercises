import functools

print ('''

	## Higher order functions and list comprehensions:

	26. Using the higher order function `reduce()`, 
	write a function `max_in_list()` that takes a list of numbers 
	and returns the largest one. Then ask yourself: 
	why define and call a new function, when I can just as well call the `reduce()` function directly?

	''')

def max_in_list(list):

	print ('\nUsing the \'Higher order function --> reduce():\'')
	print ('The original list is:', list)
	print ('The largest value of the list is: ')
	f = lambda a,b: a if (a > b) else b
	ans = functools.reduce(f, list_n)
	print ( ans )
	print ()

list_n = [65342, -87654, 345, 765, 954360, 1, 990, -243, 777, -9]
max_in_list(list_n)