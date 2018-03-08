print ("""
	7. Define a function reverse() that computes the reversal of a string. 
	For example, reverse( "I am testing" ) should return the string "gnitset ma I".
	""")

def reverse_function():
	
	str1=str(input("Please enter the string to reverse: "))
	str2=""
	subs=-1
	for index, character in enumerate(str1):
		str2 += str1[len(str1)+subs]
		subs-=1
	print ("---")
	print ("The new word is: ", str(str2))
	print ("---")

reverse_function()