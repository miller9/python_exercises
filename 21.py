print ('''

	21. Write a function `char_freq()` that takes a string
	 and builds a frequency listing of the characters contained in it. 
	 Represent the frequency listing as a Python dictionary. 
	 Try it with something like `char_freq("abbabcbdbabdbdbabababcbcbab")`.

	''')

def char_freq(string):

	freq_dict = {}

	for character in string:
		if character not in freq_dict:
				freq_dict[character] = 1
				# Verify how the dictionary is growing
				# print (freq_dict)	
		elif character in freq_dict:
			freq_dict[character] += 1

	print ('The dictionary with characters and frequency is:')
	print (freq_dict)
	print ()	


char_freq('abbabcbdbabdbdbabababcbcbab')
