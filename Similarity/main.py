#-*- coding: utf-8 -*-
import similarity as sim

if __name__=="__main__":

	
	#$B<-=q(B
	dictionary = {
	"A":{"apple":2.5,"mikan":2.5,"banana":5.0,"melon":2.0},
	"B":{"apple":2.5,"banana":1.5,"kiui":3.0,"melon":4.0}
	}

	#$B%f!<%/%j%C%I5wN%(B
	value = sim.euclidean(dictionary,"A","B")
	print str(value)
	
	#$B%T%"%=%sAj4X(B
	value = sim.pearson(dictionary,"A","B")
	print str(value)
	
	#$B%3%5%$%sN`;wEY(B
	value = sim.cosine(dictionary,"A","B")
	print str(value)






