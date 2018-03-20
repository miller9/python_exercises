print ('''

	25. In English, the present participle is formed by adding the suffix -ing 
	to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

			1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
			2. If the verb ends in ie, change ie to y and add ing
			3. For words consisting of consonant-vowel-consonant, double the final letter before adding ing
			4. By default just add ing

	Your task in this exercise is to define a function `make_ing_form()` 
	which given a verb in infinitive form returns its present participle form. 
	Test your function with words such as lie, see, move and hug. 
	However, you must not expect such simple rules to work for all cases.

	''')

def make_ing_form(verb):

	ans = ''
	i = 0
	while i < len(verb):
		if (verb[1] != ' '):
			if (len(verb) == 3):
				if (verb == 'lie'):
					ans = verb[0]
					ans += 'ying'
					break
				if (verb[1] == 'a' or verb[1] == 'e' or verb[1] == 'i' or verb[1] == 'o' or verb[1] == 'u'):
					if (verb[2] == 'a' or verb[2] =='e' or verb[2] == 'i' or verb[2] == 'o' or verb[2] == 'u'):
						ans = verb
						ans += 'ing'
						break
					else:
						ans = verb
						ans += verb[-1]
						ans += 'ing'
						break
			if (verb[-1] == 'e'):
				if (verb == 'be' or verb == 'see' or verb == 'flee' or verb == 'knee'):
					ans = verb
					break
				else:
					ans += verb[0: - 1]
					ans += 'ing'
					break
				i += 1
			if (verb[-2] == 'i' and verb[-1] == 'e'):
				ans += verb
				ans += 'ying'
				break
			i += 1
			if (verb[-1] != 'e'):
				ans += verb
				ans += 'ing'
				break
			i += 1


	print ('The present participle form of the verb is: ', ans)


make_ing_form('go')
make_ing_form('be')
make_ing_form('see')
make_ing_form('flee')
make_ing_form('knee')
make_ing_form('watch')
make_ing_form('fly')
make_ing_form('think')
make_ing_form('ride')
make_ing_form('need')
make_ing_form('grow')
make_ing_form('pass')
make_ing_form('lie')
make_ing_form('move')
make_ing_form('hug')

print ()