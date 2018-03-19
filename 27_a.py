print ('''

	## Higher order functions and list comprehensions:

	27. Write a program that maps a list of words into a list of integers 
	representing the lengths of the corresponding words. 
	Write it in three different ways: 1) using a for-loop, 2) 
	using the higher order function `map()`, and 3) using list comprehensions.

	''')

def map_list_into_integers_1(list):

	print ('1rst way --> Using a \'For-Loop\':')
	int_list = []
	print ('Length of int_list: ', len(int_list))
	print ()
	i = 0
	temp = list
	for x in list:
		print ('Length of position ',i, ': ', len (list[i]) )
		temp = len (list[i])
		int_list = int_list + [temp]
		# int_list.append( len(list[i]) ) --> A better way to do it
		i += 1

	print ('\nThe list of words is:')
	print (words_list)
	print ('\nSo, the list of integers is: ', int_list)
	# print ('tamño: ', len(int_list) )
	print ()

words_list = ['milena', 'ana', 'caro', 'lucy', 'adriana', 'carmen', 'fernanda', 'maria']
map_list_into_integers_1(words_list)
