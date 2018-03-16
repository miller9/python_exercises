print ("""

	6. Define a function sum() and a function multiply() that sums and multiplies (respectively) 
	all the numbers in a list of numbers. 
	For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

	""")

def sum_function (list):

	print ()
	print ("---")
	print ("The list to sum is: [1,2,3,4])")
	sum_res = 0
	i = 0
	while i < (len(list)):
		for index in list:
			sum_res = sum_res + list[i]
			i += 1
	print ("The sum of the numbers on the list is 	  ==>	", sum_res)
	print ("---")
	print ()

sum_function([1,2,3,4])


def multiply_function(list):

	print ("---")
	print ("The list to multiply is: [1,2,3,4])")
	mult_res = 1
	i = 0
	while i < (len(list)):
		for index in list:
			mult_res = mult_res * list[i]
			i += 1
	print ("The product of the numbers on the list is ==>	", mult_res)
	print ("---")
	print ()

multiply_function([1,2,3,4])
