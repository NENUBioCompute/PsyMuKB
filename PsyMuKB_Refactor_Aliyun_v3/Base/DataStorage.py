"""
Author:Xian Tan
Aim:Storage dictionary type data to Biodata database(for testing)
data:18/1/23
Update:18/1/27
"""

import pymongo
from pymongo import MongoClient


class DataStorage:

	def __init__(self, name):
		self.name = name
		self.path = self.__login()

	def __login(self):
		"""
		连接聚集
		:return: 返回连接的聚集
		"""
		client = pymongo.MongoClient("127.0.0.1", 27017)
		# db = client['Denovo']
		# db.authenticate("tanxian123", "123456")
		collection = client['Denovo'][self.name]
		return collection

	def Storage(self, dic):
		return self.path.insert(dic)

	def FindAll(self):
		a = self.path.find()
		x = []
		for i in a:
			x.append(i)
		return x

	def FindSuperD(self, Chr, DNV, disorder, start, end):
		dic1 = {2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8", 10: "9", 11: "10",
				12: "11", 13: "12", 14: "13", 15: "14", 16: "15", 17: '16', 18: '17', 19: '18',
				20: '19', 21: '20', 22: '21', 23: '22', 24: 'X', 25: 'Y'}
		dic2 = {1: 'exonic', 2: 'splicing', 3: 'intergenic', 4: 'intronic', 5: 'upstream', 6: 'missense', 7: "UTR3",
				8: "UTR5"}
		dic3 = {1: 'ADHD', 2: 'ASD', 3: 'BD', 4: 'DD', 5: 'ID', 6: 'Sotos',
				7: 'MR', 8: 'OCD', 9: 'SCZ', 10: 'TD', 11: 'PDNOS', 12: 'DEE',
				13: 'EE', 14: 'AD', 15: 'PD', 16: 'ALS', 17: 'CP', 18: 'NTD',
				19: 'IS', 20: 'OCD', 21: 'AFND', 22: 'A/M', 23: 'CS', 24: 'CDH', 25: 'Fetal (PTB)', 26: 'Fetal (non-PTB)',
				27: 'CTR', 28: 'CTR', 29: 'Uncharacterized'}
		if Chr != 1:
			con1 = {"chr": dic1[Chr]}
		else:
			con1 = {}
		con2 = {"Func refGene": dic2[DNV]}
		con3 = {"Disorder": {'$in': [dic3[disorder]]}}
		if start != "" and end != "":
			if int(end) < int(start):
				i = end
				end = start
				start = i
			con4 = {'Position': {'$lte': end}}
			con5 = {'Position': {'$gte': start}}
		else:
			con4 = {}
			con5 = {}
		n = self.path.find({'$and': [con1, con2, con3, con4, con5]})
		x = []
		for i in n:
			x.append(i)
		return x

	def FindSuperC(self, Chr, CNV, disorder, start, end):
		dic1 = {2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8", 10: "9", 11: "10",
				12: "11", 13: "12", 14: "13", 15: "14", 16: "15", 17: '16', 18: '17', 19: '18',
				20: '19', 21: '20', 22: '21', 23: '22', 24: 'X', 25: 'Y'}
		dic2 = {1: 'DEL', 2: 'DUP'}
		dic3 = {1: 'ADHD', 2: 'ASD', 3: 'BD', 4: 'Control', 5: 'ID', 6: 'OCD', 7: 'SCZ', 8: 'TS'}
		# print(Chr)
		if Chr != 1:
			con1 = {"chr": dic1[Chr]}
		else:
			con1 = {}
		con2 = {"mutation type": dic2[CNV]}
		con3 = {"Disorder": {'$in': [dic3[disorder]]}}
		if start != "" and end != "":
			if int(end) < int(start):
				i = end
				end = start
				start = i
			con4 = {'start': {'$lte': int(end)}}
			con5 = {'end': {'$gte': int(start)}}
		else:
			con4 = {}
			con5 = {}
		# print(con1)
		# print(con2)
		# print(con3)
		# print(con4)
		# print(con5)
		n = self.path.find({'$and': [con1, con2, con3, con4, con5]})
		x = []
		for i in n:
			# print(i)
			x.append(i)
		# print(x)
		return x

	def FindByID(self, ID):
		x = []
		x.append(self.path.find_one({"ENTREZ_ID": ID}))
		return x

	def FindBySymbol(self, Symbol):
		# return self.path.find_one({'Symbol':Symbol} $or {'NAME':[Symbol]} )
		x = []
		# if "*" in Symbol:
		# 	result1 = self.path.find_one({'Symbol': Symbol.replace("*", "")})
		# 	result = self.path.find({'NAME': {'$in': [Symbol.replace("*", "")]}})
		# 	if result1 != None:
		# 		if result1 not in x:
		# 			x.append(result1)
		# 	for i in result:
		# 		if i not in x:
		# 			x.append(i)
		# 	for j in "0123456789":
		# 		SymbolX = Symbol.replace("*", j)
		# 		result1 = self.path.find_one({'Symbol': SymbolX})
		# 		result = self.path.find({'NAME': {'$in': [SymbolX]}})
		# 		if result1 != None:
		# 			if result1 not in x:
		# 				x.append(result1)
		# 		for i in result:
		# 			if i not in x:
		# 				x.append(i)
		# elif "," in Symbol:
		# 	name = Symbol.split(",")
		# 	x = []
		# 	for i in name:
		# 		result1 = self.path.find_one({'Symbol': i})
		# 		result = self.path.find({'NAME': {'$in': [i]}})
		# 		if result1 != None:
		# 			if result1 not in x:
		# 				x.append(result1)
		# 		for j in result:
		# 			if j not in x:
		# 				x.append(j)
		# 	return x

		# else:
		result1 = self.path.find_one({'Symbol': Symbol})
		result = self.path.find({'NAME': {'$in': [Symbol]}})
		if result1 != None:
			x.append(result1)
		for i in result:
			x.append(i)
		return x

	def FindByChr(self, Chr):
		lis = Chr.split(":")
		lis[1] = lis[1].replace(",", "")
		pos = lis[1].split("-")
		pos[0] = int(pos[0])
		pos[1] = int(pos[1])
		query = self.path.find({'$and': [{'LOC': lis[0]},
										 {'start': {'$lte': pos[1]}},
										 {'end': {'$gte': pos[0]}}
										 ]}).limit(50).sort([("Symbol", 1)])
		x = []
		for i in query:
			x.append(i)
		return x

	def FindBydisease(self, Chr):
		x = []
		a = self.path.find({'Disorder': {'$in': [Chr]}}).sort([("ENTREZ_ID", 1)])
		for i in a:
			x.append(i)
		# print(len(x))
		return x

	def UpdataByID(self, dic, key, ID):
		i = self.path.find_one({'ENTREZ_ID': ID})
		if i != None:
			if key not in i:
				lis = []
				lis.append(dic)
			else:
				if isinstance(i[key], list):
					lis = i[key]
					lis.append(dic)
				else:
					lis = []
					lis.append(dic)
			return self.path.update_one({"_id": i["_id"]}, {"$set": {key: lis}})
		else:
			print("Updata false")


if __name__ == "__main__":
	a = DataStorage("CNV")
	GeneID = 53335
	# print(a.FindSuperC(2, 2, 4, '0', '7000000'))

"""
You can use this class to test your code
Firstly you can do Storage = DS.DataStorage(Name) Name is your database's name
Then when you get a dic. type data,use Storage.Storage(Name2) Name2 is your data's name
Have fun
"""
