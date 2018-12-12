# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------------------
# @file:        line_cnv
# @Author:      WangJingru
# @Purpose:     
# @Created:     2018/5/22
# @update:      2018/5/22 10:08
# @Software:    PyCharm
# -------------------------------------------------------------------------------
import pymongo
import plotly.graph_objs as go
import plotly.offline as py
from itertools import chain

class DataStorage:
	"""
	数据库查询类
	"""

	def __init__(self, name):
		self.name = name
		self.path = self.__login()

	def __login(self):
		client = pymongo.MongoClient("127.0.0.1", 27017)
		# db = client['Denovo']
		# db.authenticate("tanxian123", "123456")
		collection = client['Denovo'][self.name]
		return collection

	def FindByID(self, ID):
		x = self.path.find_one({'ENTREZ_ID': ID})
		return x

class Cnv_gene:
	def __init__(self):
		pass

	def get_len(self, cnv_x_list):
		alist = []
		for item in cnv_x_list:
			for item_item in item:
				alist.append(item_item)
		alist = list(set(alist))
		return len(alist)

	def cnv_gene(self, id, f, cnv):
		Symbol = cnv['Symbol']
		"""
		number_cnv:找到的cnv总数
		"""
		colors = []
		cnvID = []
		geneSymbol = []
		number_cnv = 0
		dis_list = []
		for item in cnv['CNV']:
			cnvID.append(item['CNV_ID'])
			geneSymbol.append(item['genesymbol'])
			dis_list.append(item.get("Disorder"))
		# print(len(geneSymbol))

		"""
		重复的CNV去重
		"""

		del_cnvID = []
		del_geneSymbol = []
		for item in cnvID:
			if str(item).lower() not in del_cnvID:
				number_cnv += 1
				del_cnvID.append(str(item).lower())
				loc = cnvID.index(item)
				del_geneSymbol.append(geneSymbol[loc])
				if str(item).lower().endswith('del'):
					colors.append("rgba(" + str(199) + "," + str(21) + "," + str(133) + ",1)")
				else:
					colors.append("rgba(" + str(109) + "," + str(90) + "," + str(205) + ",1)")

		"""
		location:搜索基因所在的最远位置；
		x:x轴坐标名称；
		"""
		location = 0
		for item in del_geneSymbol:
			cut_str = item
			gene_location = cut_str.index(Symbol)
			if location < gene_location:
				location = gene_location
			if location < (len(cut_str) - gene_location - 1):
				location = (len(cut_str) - gene_location - 1)

		"""
		loc:当前CNV中的gene位置；
		以搜索基因为中心，左右补“”；
		min:空格最少的
		"""
		min = []
		list_gene_of_cnv = []
		list_y_cnv = []
		time = 0
		for item in del_geneSymbol:
			num = 0
			list_eachCNV = []
			list_eachY = []
			cut_str = item
			"""
			cut_str去重
			"""
			quchong = []
			[quchong.append(t) for t in cut_str if not t in quchong]
			loc = quchong.index(Symbol)
			if loc < location:
				for i in range(location - loc):
					list_eachCNV.append("")
					list_eachY.append("")
					num += 1
			for j in range(len(quchong)):
				list_eachCNV.append(quchong[j])
				list_eachY.append(time)
			time += 1
			if len(list_eachCNV) < (location * 2):
				for k in range(location * 2 - len(list_eachCNV)):
					list_eachCNV.append("")
					list_eachY.append("")
			min.append(num)
			list_gene_of_cnv.append(list_eachCNV)
			list_y_cnv.append(list_eachY)

		"""
		找到前面空格最少的那条cnv
		和第一条cnv交换
		"""
		min_null = min[0]
		index = 0
		for item in min:
			if item < min_null:
				min_null = item
				index = min.index(item)

		"""
		最前面的要第一个画，不然会按照第一条cnv的横坐标画图
		"""
		if index != 0:
			temp = list_gene_of_cnv[index]
			list_gene_of_cnv[index] = list_gene_of_cnv[0]
			list_gene_of_cnv[0] = temp
			temp_y = list_y_cnv[index]
			list_y_cnv[index] = list_y_cnv[0]
			list_y_cnv[0] = temp_y

		"""
		colors:每条线的颜色
		labels:每条线的标签（纵坐标）
		line_size:每条线的宽度
		list_gene_of_cnv:横坐标数据
		y_data:纵坐标数据
		"""
		labels = []
		line_size = []
		y_data = []
		mode_size = []
		for i in range(number_cnv):
			labels.append("cnv" + str(i) + ":")
			line_size.append(6)
			l_y = []
			for j in range(location * 2):
				l_y.append(i)
			y_data.append(l_y)
			mode_size.append(6)

		traces = []

		# print(self.get_len(list_gene_of_cnv))
		for i in range(0, number_cnv):
			# for item1, item2 in zip(list_gene_of_cnv[i], list_y_cnv[i]):
			# 	traces.append(go.Scatter(
			# 		x=item1,
			# 		y=item2,
			# 		xaxis='x1',
			# 		yaxis='y1',
			# 		mode='markers',
			# 		marker=dict(color=colors[i], size=mode_size[i]),
			# 		hoverinfo=None,
			# 		text='',
			# 	))
			traces.append(go.Scatter(
				x=list_gene_of_cnv[i],
				y=list_y_cnv[i],
				xaxis='x1',
				yaxis='y1',
				mode='markers',
				marker=dict(color=colors[i], size=mode_size[i]),
				hoverinfo='x+name',
				name=dis_list[i],
			))
		traces.append(go.Scatter(
			x=[Symbol],
			y=[number_cnv],
			mode='markers+text',
			text='X-axis of gene pos',
			textposition='right',
			xaxis='x1',
			yaxis='y1',
			marker=dict(color="#000000", size=10, opacity=0.3),
			hoverinfo='text',
			hoveron="points+fills",
			hovertext='the position of gene on the X-axis'
		))

		annotations = []
		i = 0
		# Adding labels
		for y_trace, label, color in zip(y_data, labels, colors):
			# labeling the left_side of the plot
			annotations.append(dict(xref='paper', x=0.02, y=y_trace[0],
									xanchor='right', yanchor='middle',
									text=del_cnvID[i],
									font=dict(family='Arial',
											  size=10,
											  color=colors, ),
									# tickangle=-40,
									showarrow=False))
			i += 1
		if len(traces) <= 2:
			layout_height = 200
		elif len(traces) <= 6:
			layout_height = len(traces) * 60
		else:
			layout_height = len(traces) * 30
		# print(len(traces))
		if self.get_len(list_gene_of_cnv) <50:
			layout_weight = 800
		elif self.get_len(list_gene_of_cnv) <100:
			layout_weight = 1300
		else:
			layout_weight = 6*self.get_len(list_gene_of_cnv)+500
		layout = go.Layout(
			paper_bgcolor='rgb(249, 249, 249)',
			plot_bgcolor='rgb(249, 249, 249)',
			height=layout_height,
			width=layout_weight,
			margin = go.Margin(
				l=150,
				r=0,
				t=20,
				b=80,
				pad=0
			),
			xaxis = dict(
				showline=True,
				showgrid=False,
				linecolor='rgb(204, 204, 204)',
				linewidth=4,
				autotick=True,
				tickfont=dict(size=8),
				tickangle=70,
			),
			yaxis = dict(
				showgrid=False,
				zeroline=False,
				showline=False,
				showticklabels=False,
			),
			autosize=True,
			showlegend=False,
			hovermode='closest',

	)
		layout['annotations'] = annotations

		# for item in traces:
		# 	print(item)
		fig = go.Figure(data=traces, layout=layout)
		# plotly.offline.plot(fig, show_link=False)
		try:
			# plotly.offline.plot(fig, show_link=False)
			return py.plot(fig, show_link=False, output_type="div")
		except:
			# print(1)
			return '<div><p>There is no corresponding data published yet,we will update it when such data available.</p></div>'

class Cnv_gene_double:
	def __init__(self):
		pass

	def get_len(self, cnv_x_list, cnv_x2_list):
		alist = []
		for item in chain(cnv_x_list, cnv_x2_list):
			for item_item in item:
				alist.append(item_item)
		alist = list(set(alist))
		return len(alist)

	def cnv_gene(self, id, f, ppi):
		Symbol = ppi['Symbol']

		"""
		**************************1.找出所有control的数据********************************
		**************************2.其他全都归为case的数据*******************************
		x_cnvID：存储找到的cnv名称
		x_geneSymbol：存储和cnv名称对应的geneSymbol段
		x_colors：存储颜色值，用于区分del和dup类型
		x_number_cnv：用于存储cnv条数
		"""

		control_cnvID = []
		control_colors = []
		control_number_cnv = 0
		control_geneSymbol = []
		case_cnvID = []
		case_colors = []
		case_number_cnv = 0
		case_geneSymbol = []
		# print(ppi)
		dis_list = []
		for item in ppi['CNV']:
			if item['Disorder'] == 'Control':
				control_cnvID.append(item['CNV_ID'])
				control_geneSymbol.append(item['genesymbol'])
				dis_list.append(item.get("Disorder"))
		for item in ppi['CNV']:
			if item.get('Disorder') != 'Control':
				case_cnvID.append(item['CNV_ID'])
				case_geneSymbol.append(item['genesymbol'])
				dis_list.append(item.get("Disorder"))
		# print(dis_list)
		# print(control_cnvID)
		# print(case_cnvID)
		"""
		cnv去重，并按照del dup类型给定颜色值作为区分
		"""
		if control_cnvID != []:
			del_control_cnvID = []
			del_control_geneSymbol = []
			for item in control_cnvID:
				if str(item).lower() not in del_control_cnvID:
					control_number_cnv += 1
					del_control_cnvID.append(str(item).lower())
					loc = control_cnvID.index(item)
					del_control_geneSymbol.append(control_geneSymbol[loc])
					# print(str(item).lower(), geneSymbol[loc])
					if str(item).lower().endswith('del'):
						control_colors.append("rgba(" + str(199) + "," + str(21) + "," + str(133) + ",1)")
					else:
						control_colors.append("rgba(" + str(109) + "," + str(90) + "," + str(205) + ",1)")
		if case_cnvID != []:
			del_case_cnvID = []
			del_case_geneSymbol = []
			for item in case_cnvID:
				if str(item).lower() not in del_case_cnvID:
					case_number_cnv += 1
					del_case_cnvID.append(str(item).lower())
					loc = case_cnvID.index(item)
					del_case_geneSymbol.append(case_geneSymbol[loc])
					# print(str(item).lower(), geneSymbol[loc])
					if str(item).lower().endswith('del'):
						case_colors.append("rgba(" + str(199) + "," + str(21) + "," + str(133) + ",1)")
					else:
						case_colors.append("rgba(" + str(109) + "," + str(90) + "," + str(205) + ",1)")

		"""
		location:搜索基因所在的最远位置；
		x:x轴坐标名称；
		"""
		control_location = 0
		for item in del_control_geneSymbol:
			cut_str = item
			gene_location = cut_str.index(Symbol)
			if control_location < gene_location:
				control_location = gene_location
			if control_location < (len(cut_str) - gene_location - 1):
				control_location = (len(cut_str) - gene_location - 1)

		case_location = 0
		for item in del_case_geneSymbol:
			cut_str = item
			gene_location = cut_str.index(Symbol)
			if case_location < gene_location:
				case_location = gene_location
			if case_location < (len(cut_str) - gene_location - 1):
				case_location = (len(cut_str) - gene_location - 1)

		"""
		time是y轴坐标值
		"""
		time = 0
		"""
		loc:当前CNV中的gene位置；
		以搜索基因为中心，左右补“”；
		min:空格最少的
		"""
		control_min = []
		control_list_gene_of_cnv = []
		control_list_y_cnv = []

		for item in del_control_geneSymbol:
			num = 0
			list_eachCNV = []
			list_eachY = []
			cut_str = item
			"""
			cut_str去重
			"""
			quchong = []
			[quchong.append(t) for t in cut_str if not t in quchong]
			loc = quchong.index(Symbol)
			if loc < control_location:
				for i in range(control_location - loc):
					list_eachCNV.append("")
					list_eachY.append("")
					num += 1
			for j in range(len(quchong)):
				list_eachCNV.append(quchong[j])
				list_eachY.append(time)
			time += 1
			if len(list_eachCNV) < (control_location * 2):
				for k in range(control_location * 2 - len(list_eachCNV)):
					list_eachCNV.append("")
					list_eachY.append("")
			control_min.append(num)
			control_list_gene_of_cnv.append(list_eachCNV)
			control_list_y_cnv.append(list_eachY)

		case_min = []
		case_list_gene_of_cnv = []
		case_list_y_cnv = []

		for item in del_case_geneSymbol:
			num = 0
			list_eachCNV = []
			list_eachY = []
			cut_str = item
			"""
			cut_str去重
			"""
			quchong = []
			[quchong.append(t) for t in cut_str if not t in quchong]
			loc = quchong.index(Symbol)
			if loc < case_location:
				for i in range(case_location - loc):
					list_eachCNV.append("")
					list_eachY.append("")
					num += 1
			for j in range(len(quchong)):
				list_eachCNV.append(quchong[j])
				list_eachY.append(time)
			time += 1
			if len(list_eachCNV) < (case_location * 2):
				for k in range(case_location * 2 - len(list_eachCNV)):
					list_eachCNV.append("")
					list_eachY.append("")
			case_min.append(num)
			case_list_gene_of_cnv.append(list_eachCNV)
			case_list_y_cnv.append(list_eachY)
		"""
		找到前面空格最少的那条cnv
		和第一条cnv交换
		"""
		control_min_null = control_min[0]
		control_index = 0
		for item in control_min:
			if item < control_min_null:
				control_min_null = item
				control_index = control_min.index(item)

		case_min_null = case_min[0]
		case_index = 0
		for item in case_min:
			if item < case_min_null:
				case_min_null = item
				case_index = case_min.index(item)

		# print(self.get_len(control_list_gene_of_cnv, case_list_gene_of_cnv))
		"""
		找到最前面的那个，第一个画
		"""
		del_cnvID = del_control_cnvID + del_case_cnvID
		labels = []
		line_size = []
		y_data = []
		mode_size = []
		traces = []
		"""
		先画case
		"""
		if control_index >= case_index:
			colors = case_colors + control_colors
			if case_index != 0:
				temp = case_list_gene_of_cnv[case_index]
				case_list_gene_of_cnv[case_index] = case_list_gene_of_cnv[0]
				case_list_gene_of_cnv[0] = temp
				temp_y = case_list_y_cnv[case_index]
				case_list_y_cnv[case_index] = case_list_y_cnv[0]
				case_list_y_cnv[0] = temp_y

			"""
			labels:每条线的标签（纵坐标）
			line_size:每条线的宽度
			list_gene_of_cnv:横坐标数据
			y_data:纵坐标数据
			"""
			labels = []
			line_size = []
			y_data = []
			mode_size = []

			"""
			画纵坐标：先画control 再画case
			"""
			for i in range(control_number_cnv):
				labels.append("cnv" + str(i) + ":")
				line_size.append(6)
				l_y = []
				for j in range(control_location * 2):
					l_y.append(i)
				y_data.append(l_y)
				mode_size.append(6)
			"""
			middle_y:找到中间空格的位置
			"""
			middle_y = y_data[len(y_data) - 1][0] + 3

			for i in range(case_number_cnv):
				labels.append("cnv" + str(i) + ":")
				# colors.append("rgba(" + str(74) + "," + str(112) + "," + str(139) + ",1)")
				line_size.append(6)
				l_y = []
				for j in range(case_location * 2):
					l_y.append(i + middle_y)
				y_data.append(l_y)
				mode_size.append(6)

			"""
			所有都是control占用 0-->i行； case占用 i+1--> n 行；
			"""
			for i in range(0, case_number_cnv):
				linshi_y = case_list_y_cnv[i]
				y_list = []
				for item in linshi_y:
					if item != '':
						y_list.append(int(item) + 2)
					else:
						y_list.append('')
				traces.append(go.Scatter(
					x=case_list_gene_of_cnv[i],
					y=y_list,
					xaxis='x1',
					yaxis='y1',
					mode='markers',
					marker=dict(color=case_colors[i], size=mode_size[i]),
					hoverinfo='x+name',
					name=dis_list[control_number_cnv+i]
				))
			for i in range(0, control_number_cnv):
				# print("x坐标(control)：", control_list_gene_of_cnv[i])
				traces.append(go.Scatter(
					x=control_list_gene_of_cnv[i],
					y=control_list_y_cnv[i],
					xaxis='x1',
					yaxis='y1',
					mode='markers',
					marker=dict(color=control_colors[i], size=mode_size[i + middle_y - 2]),
					hoverinfo='x+name',
					name=dis_list[i]
				))
			traces.append(go.Scatter(
				x=[Symbol],
				y=[case_number_cnv + middle_y],
				mode='markers+text',
				text='X-axis of gene pos',
				textposition='bottom',
				xaxis='x1',
				yaxis='y1',
				marker=dict(color="#000000", size=10, opacity=0.3),
				hoverinfo='text',
				hoveron="points+fills",
				hovertext='the position of gene on the X-axis'
			))
		else:
			"""
			先画control
			"""

			colors = control_colors + case_colors
			if control_index != 0:
				temp = control_list_gene_of_cnv[control_index]
				control_list_gene_of_cnv[control_index] = control_list_gene_of_cnv[0]
				control_list_gene_of_cnv[0] = temp
				temp_y = control_list_y_cnv[control_index]
				control_list_y_cnv[control_index] = control_list_y_cnv[0]
				control_list_y_cnv[0] = temp_y

			"""
			colors:每条线的颜色
			labels:每条线的标签（纵坐标）
			line_size:每条线的宽度
			list_gene_of_cnv:横坐标数据
			y_data:纵坐标数据
			"""
			"""
			画纵坐标：先画control 再画case
			"""
			for i in range(control_number_cnv):
				labels.append("cnv" + str(i) + ":")
				line_size.append(6)
				l_y = []
				for j in range(control_location * 2):
					l_y.append(i)
				y_data.append(l_y)
				mode_size.append(6)
			"""
			middle_y:找到中间空格的位置
			"""
			middle_y = y_data[len(y_data) - 1][0] + 3

			for i in range(case_number_cnv):
				labels.append("cnv" + str(i) + ":")
				line_size.append(6)
				l_y = []
				for j in range(case_location * 2):
					l_y.append(i + middle_y)
				y_data.append(l_y)
				mode_size.append(6)

			"""
			画散点：先画control 再画case
			"""

			for i in range(0, control_number_cnv):
				traces.append(go.Scatter(
					x=control_list_gene_of_cnv[i],
					y=control_list_y_cnv[i],
					# xaxis='x1',
					# yaxis='y1',
					mode='markers',
					marker=dict(color=control_colors[i], size=mode_size[i]),
					hoverinfo='x+name',
					name=dis_list[i]
				))

			for i in range(0, case_number_cnv):
				linshi_y = case_list_y_cnv[i]
				y_list = []
				for item in linshi_y:
					if item != '':
						y_list.append(int(item) + 2)
					else:
						y_list.append('')
				traces.append(go.Scatter(
					x=case_list_gene_of_cnv[i],
					y=y_list,
					# xaxis='x1',
					# yaxis='y1',
					mode='markers',
					marker=dict(color=case_colors[i], size=mode_size[i + middle_y - 2]),
					hoverinfo='x+name',
					name=dis_list[control_number_cnv+i]
				))
			traces.append(go.Scatter(
				x=[Symbol],
				y=[case_number_cnv + middle_y],
				mode='markers+text',
				text='X-axis of gene pos',
				textposition='bottom',
				# xaxis='x1',
				# yaxis='y1',
				marker=dict(color="#000000", size=10, opacity=0.3),
				hoverinfo='text',
				hoveron="points+fills",
				hovertext='the position of gene on the X-axis'
			))
		if len(traces) <= 2:
			layout_height = 450
		elif len(traces) <= 6:
			layout_height = len(traces) * 90
		elif len(traces) <= 10:
			layout_height = len(traces)*40
		else:
			layout_height = len(traces) * 30
		if self.get_len(control_list_gene_of_cnv, case_list_gene_of_cnv) <50:
			layout_weight = 800
		elif self.get_len(control_list_gene_of_cnv, case_list_gene_of_cnv) <100:
			layout_weight = 1300
		else:
			layout_weight = 6*self.get_len(control_list_gene_of_cnv, case_list_gene_of_cnv)+500

		layout = go.Layout(
			height=layout_height,
			width=layout_weight,
			paper_bgcolor='rgb(249, 249, 249)',
			plot_bgcolor='rgb(249, 249, 249)',
			margin=go.Margin(
				l=90,
				r=0,
				t=0,
				b=80,
				pad=0
			),
			xaxis=dict(
				showline=True,
				showgrid=False,
				linecolor='rgb(204, 204, 204)',
				linewidth=4,
				autotick=True,
				tickfont=dict(size=7),
				tickangle=70,
			),
			yaxis=dict(
				showgrid=False,
				zeroline=False,
				showline=False,
				showticklabels=False,
			),
			autosize=True,
			showlegend=False,
			hovermode='closest',
		)

		annotations = []
		i = 0
		# Adding labels
		for y_trace, label, color in zip(y_data, labels, colors):
			# labeling the left_side of the plot

			annotations.append(dict(xref='paper', x=0.02, y=y_trace[0],
									xanchor='right', yanchor='middle',
									text=del_cnvID[i],
									font=dict(family='Arial',
											  size=8,
											  color=colors),
									showarrow=False))
			i += 1

		layout['annotations'] = annotations

		# print(traces)
		fig = go.Figure(data=traces, layout=layout)
		# print(fig)
		# plotly.offline.plot(fig, show_link=False)
		try:
			# plotly.offline.plot(fig, show_link=False)
			return py.plot(fig, show_link=False, output_type="div")
			# py.plot(fig, show_link=False, filename="biogrid_PPI.html")
		except:
			return '<div><p>There is no corresponding data published yet,we will update it when such data available.</p></div>'

class Main:
	def __init__(self):
		pass

	def run(self, id):
		cg = Cnv_gene_double()
		dan_cg = Cnv_gene()
		f = DataStorage("Gene")
		cnv = f.FindByID(str(id))
		if cnv != None:
			if 'CNV' in cnv.keys():
				case_f = 0
				control_f = 0
				for item in cnv['CNV']:
					if item.get('Disorder') == 'Control':
						# 有control
						control_f = 1
					elif item.get('Disorder') != None:
						# print(False)
						case_f = 1
				# print(control_f)
				# print(case_f)
				# 判断  有control字段执行当前函数；没有则执行dan_cnv.py类的函数
				if control_f == 1 and case_f == 0:
					# 没有case  有 control
					# print(False)
					return dan_cg.cnv_gene(id, f, cnv)

				elif control_f == 0 and case_f == 1:
					# 有case 没有control
					# print(True)
					return dan_cg.cnv_gene(id, f, cnv)
				elif control_f == 1 and case_f == 1:
					return cg.cnv_gene(id, f, cnv)
		else:
			pass

			# else:
			# 	print(2)
		# else:
		# 	# print(1)
		# 	return "<div>not found!</div>"


def main(ID):
	mainer = Main()
	ID = str(ID)
	return mainer.run(ID)

if __name__ == '__main__':
	mainer = Main()
	# mainer.run("253980")
	# mainer.run("53335")
	mainer.run("100500860")
	# mainer.run("3737")

