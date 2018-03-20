print ('''

	17. Write a version of a palindrome recognizer that also accepts phrase palindromes
	such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?",
	"Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", 
	"Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
	"Rise to vote sir", or the exclamation "Dammit, I'm mad!".
	Note that punctuation, capitalization, and spacing are usually ignored.


			Palindrome examples:
			"Go hang a salami I'm a lasagna hog.", 
			"Was it a rat I saw?",
			"Step on no pets", 
			"Sit on a potato pan, Otis", 
			"Lisa Bonet ate no basil", 
			"Satan, oscillate my metallic sonatas", 
			"I roamed under it as a tired nude Maori",
			"Rise to vote sir", 
			"Dammit, I'm mad!".

	''')

def palindrome_recognizer():
	
	print ('---')
	str1 = str( input('Please enter the phrase to verify if its palindrome or not: ') )
	phrase = str1.lower()
	phrase = phrase.strip('¿?.,\'¡!')
	print (phrase)
	print ()
	str2 = ""
	subs = -1
	i = 0
	for index, character in enumerate(phrase):
		str2 += phrase[len(phrase) + subs]
		subs -= 1

	if str2[index] == phrase[len(phrase) + subs]:
		print (True, '--> The phrase is palindrome!')
	else:
		print (False, '--> The phrase is not a palindrome!')
	print ('---')
	print ()


palindrome_recognizer()
