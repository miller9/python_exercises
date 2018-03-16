print ('''

	10. Define a function overlapping() that takes two lists and 
	returns True if they have at least one member in common, False otherwise. 
	You may use your 'is_member()' function, or the 'in' operator, 
	but for the sake of the exercise, you should (also) write it using two nested for-loops.

	''')

def  overlapping(a_list, b_list):
	
	print ('The first list is:	', a_list)
	print ('The second list is:	', b_list)

	i = 0
	x1 = []
	x2 = []
	if (len(a_list) > len(b_list)):
		x1 = a_list
		x2 = b_list
	else:
		x1 = b_list
		x2 = a_list

	while i < len(x1):
		for num in x1:
			# Using the 'in' operator to verify if the member belongs to the other list
			# if num in x2:
			if (num == x2[i]):
				print ('\nThere is at least 1 member repeated -->', num)
				return True
		i += 1
	return False


list_1 = ['python', 963, 'abc', 321, 954810, 3]
list_2 = [12, 'py', 'bwqeqweqwc', 9, 1, 2, 4, 5, 6, 7, 8, 963]
ans = overlapping(list_1, list_2)
print ('Have both lists at least 1 member in common?', ans)
print ()