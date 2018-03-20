print ('''

	20. Represent a small bilingual lexicon as a Python dictionary in the following fashion

		{ "merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år" }

	and use it to translate your Christmas cards from English into Swedish. 
	That is, write a function `translate()` that takes a list of 
	English words and returns a list of Swedish words.


	''')

def translate(list):

	output = ""
	b_lexicon = { 'merry': 'god', 'christmas': 'jul', 'and': 'och', 'happy': 'gott', 'new': 'nytt', 'year': 'år' }
	for i in list:
		if i in b_lexicon:
			output += b_lexicon[i]
			output += " "

	print ('Your translated Christmas card is: ', output)
	print ()


list1 = ['merry', 'christmas', 'and', 'happy', 'new', 'year']
translate(list1)

