#-*- coding: utf-8 -*-
import treatFiles

if __name__=="__main__":
	#辞書形式のファイル名
	readJsonFileName = "readJson.txt"
	writeJsonFileName = "writeJson.txt"
	#読み込み
	jsonFile = treatFiles.readJsonFile(readJsonFileName)
	#書き込み
	treatFiles.writeJsonFile(writeJsonFileName,jsonFile)


	#Csv形式ファイル名
	readCsvFileName = "readCsv.csv"
	#読み込み
	csvFile = treatFiles.readCsvFile(readCsvFileName)
