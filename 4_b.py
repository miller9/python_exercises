print ('''

	4. Write a function that takes a character ( i.e. a string of length 1 )
	and returns True if it is a vowel, False otherwise.

	''')

def vowel_or_not2():
	
	print ('\n Diference between vowel_or_not and vowel_or_not2 is that this function ask for user input:')
	print ('\nEnter a letter to tell you if it is a vowel or not:')
	
	vowel = input()
	if (vowel == 'a' or vowel == 'e'or vowel == 'i'or vowel == 'o' or vowel == 'u'):
		print ('True, it is a vowel')
	else:
		print ('False, it is not a vowel')

vowel_or_not2()