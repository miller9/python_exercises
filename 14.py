print ("""
	14. Write a program that maps a list of words into a list of integers
	representing the lengths of the corresponding words.
	""")

def map_list_of_words(words_list):
	int_list=[]
	for word in words_list:
		int_list.append(len(word))

	print ("\nThe list of words is   :",words_list)
	print ("The list of integers is:",int_list)
	print ()

l1=["david","gilmour","roger","waters","ray","manzarek","jim","morrison"]
map_list_of_words(l1)
print ()
