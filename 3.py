print ('''

	3. Define a function that computes the length of a given list or string. 
	( It is true that Python has the len() function built in, 
	but writing it yourself is nevertheless a good exercise ).
	
	''')

def string_lenght1():
	
	print ('\nPlease enter the string to compute: ')
	string_x = input()
	i = 0
	q = 0
	while (i <= len(string_x)-1):
		# If i use " ", the 'string' cannot have 'spaces' inside.
		# if (string_x[i] != " "):
		# If i change it for "", it would work well because the 'string' could have 'spaces' inside.
		if (string_x[i] != ""):
			q = q + 1
			i = i + 1
		# But doing it this way ==> using ("") --> It would never take this condition...
		else:
			print ('There is no String becasuse its empty!')
			break

	print ('The lenght of your string is: ' + str(q))
	print ('---')
	print ()
string_lenght1()
