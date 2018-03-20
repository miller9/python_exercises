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

	string = ['n', 'sh']
	suffixes = 0
	if (inf_verb.endswith('n') ):
		print ('The new form of the verb is: ', inf_verb + 's')
	elif (inf_verb.endswith('y') ):
		print ('The new form of the verb is: ', inf_verb[0: -1] + 'ies')
	elif (inf_verb.endswith(('o', 'ch', 'sh')) ):
		print ('The new form of the verb is: ', inf_verb + 'es')
	elif (inf_verb.endswith(('x', 'z', 's')) ):
		print ('The new form of the verb is: ', inf_verb + 'es')
	else:
		print ('The new form of the verb is: ', inf_verb + 's')
#	if ( inf_verb.endswith(suffixes) ):
#		print ()


print ('Solution using function \'endswith()\':')
make_3sg_form('try')
make_3sg_form('brush')
make_3sg_form('run')
make_3sg_form('fix')
make_3sg_form('cry')
make_3sg_form('crash')
make_3sg_form('think')
make_3sg_form('smile')


print ()