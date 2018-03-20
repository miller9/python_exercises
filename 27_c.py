print ('''

	## Higher order functions and list comprehensions:

	27. Write a program that maps a list of words into a list of integers 
	representing the lengths of the corresponding words. 
	Write it in three different ways: 1) using a for-loop, 2) 
	using the higher order function `map()`, and 3) using list comprehensions.

	''')


def map_list_into_integers_3(list_1):

	print ('3rd way --> Using \'List Comprehensions\':')
	int_list = [ len(x) for x in list_1 ]

	print ('\nThe list of words is:')
	print (words_list)
	print ('\nThe list of integers using \'List Comprehensions\' is: ', int_list)
	print ()



words_list = ['milena', 'ana', 'caro', 'lucy', 'adriana', 'carmen', 'fernanda', 'maria']
map_list_into_integers_3(words_list)
