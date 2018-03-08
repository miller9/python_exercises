print ("""
	15. Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
	""")

def find_longest_word(words_list):
	
	int_list=[]
	for word in words_list:
		int_list.append(len(word))

	max_value=max(int_list)

	i=0
	while i<len(words_list):
		if (len(words_list[i])==max_value):
			print ("The list of words is 	  :",words_list)
			print ("The longest word is 	  :",words_list[i])
			print ("The length of the word is :",max_value)
			break
		i+=1
	print ()

l1 = ["high_hopes","echoes","comfortably_numb","johnny_be_good","roll_over_bethoven","school_days"]
find_longest_word(l1)