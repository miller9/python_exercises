print ('''

	13. The function max() from exercise 1) and the function max_of_three() from exercise 2) 
	will only work for two and three numbers, respectively. 
	But suppose we have a much larger number of numbers, 
	or suppose we cannot tell in advance how many they are?
	Write a function max_in_list() that takes a list of numbers and returns the largest one.

	''')

def max_in_list(l):

	print ('\nSecond way:')
	print ('The original list is:', l)				
	l.sort()										
	print ('The ordered list is :', l)				
	print ('Greatest value is   :', l[ (len(l) - 1) ])

l1 = [234, -300, 1, 213, 576, 678, 3456, 4646, -13455, -98765, 1324, 876543, 982, 98, 76]
max_in_list(l1)
print ()

