print ("""
	9. Write a function is_member() that takes a value ( i.e. a number, string, etc ) x 
	and a list of values a, and returns True if x is a member of a, False otherwise. 
	(Note that this is exactly what the 'IN' operator does, 
	but for the sake of the exercise you should pretend Python did not have this operator).
	""")

def is_member(x,a):
	# x=number, string, etc
	# a=list of values
	print ("\nThe value x is:			",x)
	print ("The list of values are:		",a)
	i=0
	s=len(a)
	while i<s:							# While i<length of list
		if ( a[i]==x ): return True			# if 'value' in position [i] == x return True
		else:							# then
			i+=1							# i is growing
	return False						# if the value is not a member return False
	
"""
	for l in a:							# for each value saved in a
		# if (l==x): return True			# if 'value'==x return True
		if (a[l]==x): return True			# if the 'value' in 'l' position ==x return True
		else: return False					# then False
"""

val="zxy"
l_val=[453,"Python",9,'zxy',21]
ans=is_member(val,l_val)

print ("Is a member of the list?	",ans)
print ()