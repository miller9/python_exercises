print ("""
	8. Define a function is_palindrome() that recognizes palindromes 
	(i.e. words that look the same written backwards).
	For example, is_palindrome( "radar" ) should return True.	
	""")

def is_palindrome():

	print ("---")
	str1=str(input("Please enter the string to verify if its palindrome or not: "))
	str2=""
	subs=-1
	i=0
	for index, character in enumerate(str1):
		str2+=str1[len(str1)+subs]
		subs-=1

	if str2[index] == str1[len(str1)+subs]:
		print (True, "--> The word is palindrome!")
	else:
		print (False, "--> The word is not a palindrome!")
	print ("---")
	print ()
"""
Palindrome Examples: --> Dont use special characters:
Alí tomó tila.
Allí ves Sevilla.
Aman a Panamá.
A Mercedes ése de crema.
Amad a la dama.
A mamá Roma le aviva el amor a papá y a papá Roma le aviva el amor a mamá.
Amigo no gima.
A mí me mima.
"""

is_palindrome()