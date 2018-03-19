print ('''

	## Higher order functions and list comprehensions:

	26. Using the higher order function `reduce()`, 
	write a function `max_in_list()` that takes a list of numbers 
	and returns the largest one. Then ask yourself: 
	why define and call a new function, when I can just as well call the `reduce()` function directly?

	''')

def max_in_list(list):

	print ('Using the sort() function instead of the reduce() function:\'')
	print ('The original list is:', list)
	list.sort()
	print ('The ordered list is :', list)
	print ('Greatest value is   :', list[ (len(list) - 1) ])


list_n = [65342, -87654, 345, 765, 954360, 1, 990, -243, 777, -9]
max_in_list(list_n)