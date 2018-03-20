print ('''

	5. Write a function translate() that will translate a text into 
	"rövarspråket" (Swedish for "robber's language"). 
	That is, double every consonant and place an occurrence of "o" in between. 
	For example, translate("this is fun") should return the string "tothohisos isos fofunon".

	''')

def translate():
	
	print ()
	print ('---')
	str1 = str( input('Please enter the string to be translated: ') )
	str2 = " "
	consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
					'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

	for index, character in enumerate(str1):
		if str1[index] in consonant_list:
			str2 += (str1[index] + 'o' + str1[index])
		else: 
			str2 += str1[index]
	print ()
	print ('Our new \'rövarspråket\' String is: ' + str2)
	print ('---')



translate()