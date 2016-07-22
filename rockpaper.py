from random import choice 
c_score = 0
p_score = 0
def c_choice(lizard):
	x = choice (lizard)
	return x
def game(p_score , c_score):
	print "Hi, I'm Doug the computer. Let's play 1 game of rock-paper-scissors!"
	a = 0
	while a==0:
		if c_score >=2:
			print "I win!"
			c_score = 0
			p_score = 0
		if p_score >= 2:
			print "I lose!"
			c_score = 0
			p_score = 0
		p = raw_input("Make your move. (r, p, s)")
		x = c_choice("rps")
		if p == "q":
			a = 1
		elif (p == "r") and (x == "p"):
		 	print "I play paper"
		 	c_score = c_score + 1
		 	print p_score, ":", c_score
		elif (p == "r") and (x == "s"):
		 	print "I play scissors"
		 	p_score = p_score + 1
		 	print p_score,":", c_score
		elif (p == "p") and (x == "r"):
		 	print "I play rock"
		 	p_score = p_score + 1
		 	print p_score,":", c_score
		elif (p == "p") and (x == "s"):
		 	print "I play scissors"
		 	c_score = c_score + 1
		 	print p_score,":", c_score
		elif (p == "s") and (x == "r"):
		 	print "I play rock"
		 	c_score = c_score + 1
		 	print p_score,":", c_score
		elif (p == "s") and (x == "p"):
		 	print "I play rock"
		 	p_score = p_score + 1
		 	print p_score,":", c_score
		else: 
			if p == "p":
				print "I play paper"
			elif p == "r":
				print "I play rock"
			else:
				print "I play scissors"	
			print "It's a tie"
			print p_score,":", c_score		
	if a == 1:
		print "Goodbye!"
	return p_score, c_score
p_score, c_score = game(p_score, c_score)
