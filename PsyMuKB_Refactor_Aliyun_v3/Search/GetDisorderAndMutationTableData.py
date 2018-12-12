# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------------------
# @file:        FindDisorderByMutation
# @Author:      GuoSijia
# @Purpose:
# @Created:     2018-10-01
# @update:      2018-10-01 11:15
# @Software:    PyCharm
# -------------------------------------------------------------------------------
from Base import DBBase


class DbMappingTable(object):

	def __init__(self):
		pass

	def dmt(self, db_type, table_type):
		if db_type == table_type:
			return True
		elif db_type.startswith(table_type):
			return True
		elif db_type.upper() == table_type.upper():
			return True
		elif db_type.upper().startswith(table_type.upper()):
			return True
		else:
			return False

	def disorder(self, db_str):
		if db_str == "ASD or SCZ":
			return "Others"
		elif self.dmt(db_str, "ADHD"):
			return "ADHD"
		elif self.dmt(db_str, "ASD"):
			return "ASD"
		elif self.dmt(db_str, "BD") or db_str == "Bipolar Disorder":
			return "BD"
		elif db_str == "Congenital Heart Disease" or self.dmt(db_str, "CHD"):
			return "CHD"
		elif self.dmt(db_str, "Control"):
			return "Control"
		elif self.dmt(db_str, "DD"):
			return "DD"
		elif self.dmt(db_str, "DEE"):
			return "DEE"
		elif self.dmt(db_str, "EE"):
			return "EE"
		elif self.dmt(db_str, "ID") or db_str == "Intellectual Disability/Developmental Disability":
			return "ID"
		elif self.dmt(db_str, "OCD"):
			return "OCD"
		elif self.dmt(db_str, "PD"):
			return "PD"
		elif self.dmt(db_str, "SCZ") or db_str == "Schizophrenia":
			return "SCZ"
		elif db_str == "Tourette Disorder" or self.dmt(db_str, "TS"):
			return "TS"
		else:
			return "Others"

	def coding_mapping(self, m_str):
		if m_str.startswith("frameshift"):
			return "frameshift"
		elif m_str == "stopgain":
			return "nonsense"
		elif m_str.startswith("splice-site"):
			return "splice-site"
		elif m_str == "start gain":
			return "start gain"
		elif m_str == "stoploss":
			return "stoploss"
		elif m_str == "nonsynonymous SNV":
			return "missense"
		elif m_str == "Non-frameshit" or m_str == "non-frameshit" or m_str == "non frameshit":
			return "Non-frameshit"
		elif m_str.startswith("synonymous") or m_str == "synonymous SNV":
			return "synonymous SNV"
		else:
			return "coding-Others"

	def non_coding_mapping(self, m_str):
		#####针对数据库中同一种突变，不同命名的格式化#####
		if m_str == "intronic":
			return "intronic"
		elif m_str == "UTR3" or m_str == "UTR5":
			return "UTR region"
		elif m_str == "upstream" or m_str == "downstream" or m_str == "upstream;downstream" or m_str == ['upstream', 'downstream']:
			return "up-/down-stream"
		elif m_str == "intergenic" or m_str.startswith("intergenic"):
			return "intergenic"
		elif m_str.startswith("ncRNA"):
			return "ncRNA"
		# elif m_str == "intergenic"
		else:
			return "non-coding-all-Others"

	def cnv(self, m_str):
		if m_str.startswith("Deletion") or m_str in ["deletion", "Deletion", "DEL", "Del"] or m_str.startswith("Del"):
			return "deletion"
		elif m_str.startswith("Duplication") or m_str in ["Duplication", "duplication", "DUP", "dup"]or m_str.startswith("Dup"):
			return "duplication"
		else:
			return "cnv-others"


class GetDisorderAndMutationTableData(object):

	def __init__(self, id):
		self.Gene_db = DBBase.DBBase("Gene")
		self.id = id
		self.mapping = DbMappingTable()

	# dis_item = {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "satrt in": [],
	# 			"stoploss": [], "Non-frameshit": [], "synonymous SNV": [], "intronic":[], "UTR region":[], "up-/down-stream":[],"intergenic":[],
	# 			"ncRNA":[]}
	# for item in self.disorder_dict.keys():
	# 	self.disorder_dict[item] = dis_item
	# print(self.disorder_dict)

	def get_dam_statics(self):
		mutation_type_list = ["frameshift", "nonsense", "splice-site", "missense", "start gain","stoploss", "Non-frameshit", "synonymous SNV", "intronic", "UTR region", "up-/down-stream","intergenic", "ncRNA", "coding-Others", "non-coding-all-Others", "deletion", "duplication", "cnv-others", "coding-all", "non-coding-all"]
		disorder_list = ["ASD", "SCZ", "BD", "ADHD", "ID", "DD", "OCD", "TS", "DEE", "EE", "AD", "PD", "CHD", "Others", "Control"]
		disorder_dict = {
			"all": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"ASD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"SCZ": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"BD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"ADHD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					 "stoploss": [], "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [],
					 "up-/down-stream": [], "intergenic": [], "ncRNA": [], "coding-Others": [],
					 "non-coding-all-Others": [],
					 "deletion": [], "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"ID": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"DD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"OCD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"TS": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"DEE": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"EE": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"AD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"PD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"CHD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"Others": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					   "stoploss": [], "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [],
					   "up-/down-stream": [], "intergenic": [], "ncRNA": [], "coding-Others": [],
					   "non-coding-all-Others": [], "deletion": [], "duplication": [], "cnv-others": [],
					   "coding-all": [], "non-coding-all": []},
			"Control": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
						"stoploss": [], "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [],
						"up-/down-stream": [], "intergenic": [], "ncRNA": [], "coding-Others": [],
						"non-coding-all-Others": [], "deletion": [], "duplication": [], "cnv-others": [],
						"coding-all": [], "non-coding-all": []}}
		mutation_count = {
			"all": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"ASD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"SCZ": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"BD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"ADHD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					 "stoploss": [], "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [],
					 "up-/down-stream": [], "intergenic": [], "ncRNA": [], "coding-Others": [],
					 "non-coding-all-Others": [],
					 "deletion": [], "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"ID": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"DD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"OCD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"TS": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"DEE": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"EE": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"AD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"PD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
				   "stoploss": [],
				   "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
				   "intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
				   "duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"CHD": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					"stoploss": [],
					"Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [], "up-/down-stream": [],
					"intergenic": [], "ncRNA": [], "coding-Others": [], "non-coding-all-Others": [], "deletion": [],
					"duplication": [], "cnv-others": [], "coding-all": [], "non-coding-all": []},
			"Others": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
					   "stoploss": [], "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [],
					   "up-/down-stream": [], "intergenic": [], "ncRNA": [], "coding-Others": [],
					   "non-coding-all-Others": [], "deletion": [], "duplication": [], "cnv-others": [],
					   "coding-all": [], "non-coding-all": []},
			"Control": {"frameshift": [], "nonsense": [], "splice-site": [], "missense": [], "start gain": [],
						"stoploss": [], "Non-frameshit": [], "synonymous SNV": [], "intronic": [], "UTR region": [],
						"up-/down-stream": [], "intergenic": [], "ncRNA": [], "coding-Others": [],
						"non-coding-all-Others": [], "deletion": [], "duplication": [], "cnv-others": [],
						"coding-all": [], "non-coding-all": []}}
		if self.Gene_db.find_one_by_one_condition("ENTREZ_ID", self.id):
			dnm_dict = self.Gene_db.find_one_by_one_condition("ENTREZ_ID", self.id).get("DNM")
			cnv_dict = self.Gene_db.find_one_by_one_condition("ENTREZ_ID", self.id).get("CNV")
			# print(cnv_dict)
			# print(cnv_dict)
			# print("Idenx, Disorder, MutationType")
			if dnm_dict != None:
				for index, item in enumerate(dnm_dict):
					# print(index + 1, end=", ")
					# print(self.mapping.disorder(item.get("Disorder")), end=", ")
					if item.get("Exonic Func") != 'null':
						# print(self.mapping.coding_mapping(item.get("Exonic Func")), end=" ")
						# type.append(item.get("Exonic Func"))
						disorder_dict[self.mapping.disorder(item.get("Disorder"))][
							self.mapping.coding_mapping(item.get("Exonic Func"))].append(item)
					# print(self.disorder_dict)
					else:
						# print(self.mapping.non_coding_mapping(item.get("Func refGene")), end=" ")
						disorder_dict[self.mapping.disorder(item.get("Disorder"))][
							self.mapping.non_coding_mapping(item.get("Func refGene"))].append(item)
				# print()
			if cnv_dict != None:
				for item in cnv_dict:
					disorder_dict[self.mapping.disorder(item.get("Disorder"))][
						self.mapping.cnv(item.get("mutation type"))].append(item)
		# print()
		# print(list(set(type)))
		# for item in self.disorder_dict.get("ASD").keys():
		# 	print(self.disorder_dict.get("ASD").get(item))
		# print(len(self.disorder_dict.get("Others").get("duplication")))
		# print(self.disorder_dict.get("Others").get("duplication"))
		# return
		for item in disorder_dict.keys():
			for item_item in ["frameshift", "nonsense", "splice-site", "missense", "start gain", "stoploss",
							  "Non-frameshit", "synonymous SNV"]:
				for item_item_item in disorder_dict[item][item_item]:
					disorder_dict[item]["coding-all"].append(item_item_item)
			for item_item in ["intronic", "UTR region", "up-/down-stream", "intergenic", "ncRNA"]:
				for item_item_item in disorder_dict[item][item_item]:
					disorder_dict[item]["non-coding-all"].append(item_item_item)
		for item in disorder_dict.keys():
			# print(item)
			for item_item in disorder_dict.get(item).keys():
				mutation_count[item][item_item] = len(disorder_dict[item][item_item])
		for m_item in mutation_type_list:
			for d_itme in disorder_list:
				for item_item1 in disorder_dict[d_itme][m_item]:
					disorder_dict["all"][m_item].append(item_item1)
				# for item_item2 in mutation_count[d_itme][m_item]:
				mutation_count["all"][m_item] = len(disorder_dict["all"][m_item])

		return disorder_dict, mutation_count


if __name__ == '__main__':
	m_str = "Del"
	if m_str == "Deletion" or m_str.startswith("Deletion") or m_str == "deletion":
		print(True)
	else:
		print(False)
	# pass
	# find = GetDisorderAndMutationTableData("9208")
	# disorder_dict, mutation_count = find.get_dam_statics()
	# print(disorder_dict)
	# # for item in mutation_count.keys():
	# # 	print(item, end=" ")
	# # 	print(mutation_count[item])
	# # print(mutation_count.get("all").get("nonsense"))
	# print(mutation_count.get("ASD").get("non-coding-all"))
	# print(disorder_dict.get("ASD").get("non-coding-all"))
	# for item in disorder_dict.get("ASD").get("non-coding-all"):
	# 	print(item)
# print(mutation_count.get("ASD").get("nonsense"))
# print(mutation_count.get("ASD").get("splice-site"))
# print(mutation_count.get("ASD").get("missense"))
# print(mutation_count.get("ASD").get("start gain"))
# print(mutation_count.get("ASD").get("stoploss"))
# print(mutation_count.get("ASD").get("Non-frameshit") )
# print(mutation_count.get("ASD").get("synonymous SNV"))
#
#
# print(mutation_count.get("ASD").get("frameshift") + mutation_count.get("ASD").get("nonsense") + mutation_count.get("ASD").get("splice-site")+ mutation_count.get("ASD").get("missense")+ mutation_count.get("ASD").get("start gain")+ mutation_count.get("ASD").get("stoploss")+ mutation_count.get("ASD").get("Non-frameshit") + mutation_count.get("ASD").get("synonymous SNV"))
