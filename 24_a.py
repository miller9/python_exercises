print ('''

	24. The third person singular verb form in English is distinguished by the suffix -s, 
	which is added to the stem of the infinitive form: run -> runs. 
	A simple set of rules can be given as follows:

			a. If the verb ends in y, remove it and add ies
			b. If the verb ends in o, ch, s, sh, x or z, add es
			c. By default just add s

	Your task in this exercise is to define a function `make_3sg_form()` 
	which given a verb in infinitive form returns its third person singular form. 
	Test your function with words like try, brush, run and fix. 
	Note however that the rules must be regarded as heuristic, 
	in the sense that you must not expect them to work for all cases. 
	Tip: Check out the string method `endswith()`.

	''')

def make_3sg_form(inf_verb):

	ans = ' '
	i = 0

	while i < len(inf_verb):
		if (inf_verb[1] != ' '):
			if (inf_verb[-1] == 'y'):
				ans += inf_verb[0: - 1]
				ans += 'ies'
				break
			i += 1
			if (inf_verb[-2] == 'c' and inf_verb[-1] == 'h') or (inf_verb[-2] == 's' and inf_verb[-1] == 'h'):
				ans += inf_verb
				ans += 'es'
				break
			i += 1
			if (inf_verb[-1] == 'o' or inf_verb[-1] == 's' or inf_verb[-1] == 'x' or inf_verb[-1] == 'z'):
				ans += inf_verb
				ans += 'es'
				break
			i += 1
			if (inf_verb[-1] != 'y' or inf_verb[-1] != 'o' or inf_verb[-1] != 'h' or inf_verb[-1] != 's' 
				or inf_verb[-1] != 'x' or inf_verb[-1] != 'z'):
				ans += inf_verb
				ans += 's'
				break
			i += 1


	print ('The third person singular verb form is: ', ans)


make_3sg_form('try')
make_3sg_form('brush')
make_3sg_form('run')
make_3sg_form('fix')
make_3sg_form('cry')
make_3sg_form('crash')

print ()