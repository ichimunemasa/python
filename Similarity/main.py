#-*- coding: utf-8 -*-
import similarity as sim

if __name__=="__main__":

	
	#辞書
	dictionary = {
	"A":{"apple":2.5,"mikan":2.5,"banana":5.0,"melon":2.0},
	"B":{"apple":2.5,"banana":1.5,"kiui":3.0,"melon":4.0}
	}

	#ユークリッド距離
	value = sim.euclidean(dictionary,"A","B")
	print str(value)
	
	#ピアソン相関
	value = sim.pearson(dictionary,"A","B")
	print str(value)
	
	#コサイン類似度
	value = sim.cosine(dictionary,"A","B")
	print str(value)






