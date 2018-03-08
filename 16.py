print ("""
	16. Write a function filter_long_words() that takes a list of words and 
	an integer n and returns the list of words that are longer than n.
	""")

def filter_long_words(words_list,n):
	new_list=[]
	for word in words_list:
		if (len(word)>n):
			new_list.append(word)

	print ("The original list of words is	   :",words_list)
	print ("The list of words longer than",n,"is :",new_list)
	print ()

l1 = ["deep","down","in","louisiana","close","to","new","orleans"]
filter_long_words(l1,5)
print ()