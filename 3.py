def string_lenght1():
	print ("Please enter the string to compute: ")
	string_x = input()	
	i=0
	q=0
	while (i<=len(string_x)-1):
	#	if (string_x[i] != " "): # If i use " ", the 'string' cannot have 'spaces' inside.
		if (string_x[i] != ""): # If i change it for "", it would work well because the 'string' could have 'spaces' inside.
			q=q+1
			i=i+1
		else:			# But doing it this way ==> using ("") --> It would never take this condition...
			print ("There's no String becasuse its empty!")
			break

	print("The lenght of your string is: "+str(q))
	print("---")

string_lenght1()
