print ("""
	17. Write a version of a palindrome recognizer that also accepts phrase palindromes
	such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?",
	"Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", 
	"Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
	"Rise to vote sir", or the exclamation "Dammit, I'm mad!".
	Note that punctuation, capitalization, and spacing are usually ignored.
	""")

def palindrome_recognizer(phrase):
	
	new_phrase=""
	for character in phrase:
		if (character!='' or character!=',' or character!='´' or character!="'" or character!='?' or character!='.'):
			new_phrase+=character
		else:
			new_phrase+=character+1

	a=new_phrase.lower()
	print ("\nThe original phrase is:",phrase)
	print ("The new phrase is     :",a)
	print ()

pal1="Go hang a salami I'm a lasagna hog."
palindrome_recognizer(pal1)