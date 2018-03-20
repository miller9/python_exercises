print ('''
	
	19. "99 Bottles of Beer" is a traditional song in the United States and Canada.
	It is popular to sing on long trips, as it has a very repetitive format which
	is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:

		Take one down, pass it around, 98 bottles of beer on the wall.```

	The same verse is repeated, each time with one fewer bottle. 
	The song is completed when the singer or singers reach zero. 
	Your task here is write a Python program capable of generating all the verses of the song.

	''')

def song():

	print ()
	i = 99
	while i >= 0:
		print ('Take one down, pass it around, {} bottles of beer on the wall!'.format(i))
		i -= 1

	print ('\nBye!')
	print ('---')
	print ()

song()