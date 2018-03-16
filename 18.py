print ("""

	18. A pangram is a sentence that contains all the letters 
	of the English alphabet at least once, for example: 
	"The quick brown fox jumps over the lazy dog". 
	Your task here is to write a function to check a sentence to see if it is a pangram or not.
	
	Examples of pangrams:
	1. Pretty straightforward, it addresses all the letters in the sentence, 
	even the ones that wouldn’t be there, if the whole alphabet hadn’t been mentioned.
	2. Waltz, bad nymph, for quick jigs vex.
	3. Quick zephyrs blow, vexing daft Jim.
	4. Sphinx of black quartz, judge my vow.
	5. Two driven jocks help fax my big quiz.
	6. Five quacking zephyrs jolt my wax bed.
	7. The five boxing wizards jump quickly.
	8. Pack my box with five dozen liquor jugs.
	9. Jinxed wizards pluck ivy from the big quilt

	""")

def is_pangram ():

	abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	new_abc = []
	sentence = str( input("Please enter the sentence to find if it's a pangram or not: ") )
	s = sentence.lower()
	for c in s:
		if c in abc and c not in new_abc:
			new_abc.append(c)

	if len(abc) == len(new_abc):
		print ("\nIts a pangram! :)")
		print ()
	else:
		print ("\nIt's not a pangram :(")
		print ()


is_pangram()