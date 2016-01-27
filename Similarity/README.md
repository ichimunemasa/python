#Similarity
* 辞書形式行列の行間類似度を算出する

##euclidean(matrix,row1,row2)
* ユークリッド距離の算出を行う
* 辞書形式の行列(matrix),行列の行2つを引数とする
### code 
		def euclidean(matrix,row1,row2):
			si = {}
	
			for column in matrix[row1]:
		
				if column in matrix[row1]:
					si[column] = 1
		
				if len(si)==0: return 0
		
				sum_of_squares = sum([pow(matrix[row1][column]-matrix[row2][column],2) for column in matrix[row1] if column in matrix[row2]])		
	
			return 1/(1 + sum_of_squares)


##pearson(matrix,row1,row2)
* ピアソン相関の算出を行う
* 辞書形式の行列(matrix),行列の行2つを引数とする
### code
		def pearson(matrix,row1,row2):
			si = {}
			for column in matrix[row1]:
				if column in matrix[row2] : si[column] = 1

			n = len(si)
			if n==0: return 0
	
			sum1 = sum([matrix[row1][it] for it in si])
			sum2 = sum([matrix[row2][it] for it in si])

			sum1Sq = sum([pow(matrix[row1][it],2) for it in si])
			sum2Sq = sum([pow(matrix[row2][it],2) for it in si])

			pSum = sum([matrix[row1][it]*matrix[row2][it] for it in si])

			num = pSum-(sum1*sum2/n)

			den = sqrt((sum1Sq-pow(sum1,2)/n) * (sum2Sq-pow(sum2,2)/n))

			if den==0 : return 0

			r = num/den

			return r


##cosine(matrix,row1,row2)
* コサイン類似度の算出を行う
* 辞書形式の行列(matrix),行列の行2つを引数とする
###code
		def cosine(matrix,row1,row2):
			numer = sum(matrix[row1][column] * matrix[row2][column] for column in matrix[row1] if column in matrix[row2])
			denom = sqrt(sum(matrix[row1][column]**2 for column in matrix[row1]) * sum(matrix[row2][column]**2 for column in matrix[row2]))
		
			if denom == 0: return 0
	
			return numer/denom

