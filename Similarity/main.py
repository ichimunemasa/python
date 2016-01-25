#-*- coding: utf-8 -*-
import similarity as sim

if __name__=="__main__":


	dictionary01 = {
	"A":{"apple":2.5,"mikan":2.5,"banana":5.0,"melon":2.0},
	"B":{"apple":2.5,"banana":1.5,"kiui":3.0,"melon":4.0}
	}

	value = sim.euclidean(dictionary00,"Lisa Rose","Gene Seymour")
	print str(value)
	
	value = sim.pearson(dictionary00,"Lisa Rose","Gene Seymour")
	print str(value)

	value = sim.cosine(dictionary01,"A","B")
	print str(value)






