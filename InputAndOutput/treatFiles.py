#-*- coding: utf-8 -*-
import codecs
import json
import csv

#json形式(辞書)ファイル読み込み
def readJsonFile(filename):
	f = open(filename,"r")
	jsonFile = json.load(f)
	return jsonFile


#json形式(辞書)ファイル書き込み
def writeJsonFile(filename,matrix):
	with open(filename,"w") as jsonFile:
		json.dump(matrix,jsonFile,sort_keys=True,indent=4)

#csv形式ファイル読み込み
def readCsvFile(filename):
	csvFile = open(filename,"r")
	return csvFile





	
