print ('''

	23. Define a simple "spelling correction" function `correct()` 
	that takes a string and sees to it that: 
	1) two or more occurrences of the space character is compressed into one, 
	2) inserts an extra space after a period if the period is directly followed by a letter.
	E.g. `correct("This   is  very funny  and    cool.Indeed!")` 
	should return "This is very funny and cool. Indeed!" Tip: Use regular expressions!

	''')

def correct(phrase):

	i = 0
	corrected_m = ""

	while i < len(phrase):
		if phrase[i] == ' ':
			if phrase[i + 1] != ' ':
				corrected_m += ' '
				i += 1
			else:
				i += 1
		elif phrase[i] == '.':
			corrected_m += '.'
			corrected_m += ' '
			i += 1
		else:
			corrected_m += phrase[i]
			i += 1


	print ('\nThe corrected phrase is:', corrected_m)
	print ()


correct("This   is  very funny  and    cool.Indeed!")
