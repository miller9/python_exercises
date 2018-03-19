print ('''

	## Higher order functions and list comprehensions:

	27. Write a program that maps a list of words into a list of integers 
	representing the lengths of the corresponding words. 
	Write it in three different ways: 1) using a for-loop, 2) 
	using the higher order function `map()`, and 3) using list comprehensions.

	''')

import functools

def map_list_into_integers_2(list_1):

	print ('2nd way --> Using the higher order function \'map()\':')
	int_list = []

	f = lambda a: len(a)
	int_list = list( map(f, list_1) )

	print ('\nThe list of words is:')
	print (words_list)
	print ('\nThe list of integers using \'map\' and \'lambda\' is: ', int_list)
	print ()

words_list = ['milena', 'ana', 'caro', 'lucy', 'adriana', 'carmen', 'fernanda', 'maria']
map_list_into_integers_2(words_list)
