# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------------------
# @file:        Pie
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-10-28
# @update:      2018-10-28 14:14
# @Software:    PyCharm
# -------------------------------------------------------------------------------
import plotly.plotly as py
import plotly.graph_objs as go
import plotly


class DNMPie(object):

	def __init__(self):
		pass

	def get_pie(self):
		fig = {
			'data': [
				{
					'labels': ["ADHD (Attention Deficit Hyperactivity Disorder)",
							   "ASD (Autism)",
							   "Mix (ASD or SCZ)",
							   "BP (Bipolar Disorder)",
							   "DD (Developmental Delay)",
							   "ID (Intellectual Disability)",
							   "OCD (Obsessive-Compulsive Disorder)",
							   "SCZ (Schizophrenia)",
							   "TD (Tourette Disorder)"],
					'values': [9, 206095, 2287, 75, 8340, 1425, 251, 1038, 792],
					'type': 'pie',
					'name': 'Psychiatric Disorder',
					# 'marker': {'colors': ['rgb(56, 75, 126)',
					#                       'rgb(18, 36, 37)',
					#                       'rgb(34, 53, 101)',
					#                       'rgb(36, 55, 57)',
					#                       'rgb(6, 4, 4)']},
					'domain': {'x': [0, .48],
							   'y': [.51, 1]},
					'hoverinfo': 'label+value+name',
					'textinfo': 'none',
					"hole": .4,
				},
				{
					'labels': ["DEE (Developmental and Epileptic Encephalopathies)", "EE",
							   "AD (Alzheimer disorder early-onset)", "PD (Parkinson disorder early-onset)",
							   "ALS (amyotrophic lateral sclerosis)", "CP (cerebral palsy)",
							   "IS (sporadic infantile spasm syndrome)", "NTD (neural tube defects)", ],
					'values': [288, 689, 20, 19, 94, 66, 5, 38],
					# 'marker': {'colors': ['rgb(177, 127, 38)',
					#                       'rgb(205, 152, 36)',
					#                       'rgb(99, 79, 37)',
					#                       'rgb(129, 180, 179)',
					#                       'rgb(124, 103, 37)']},
					'type': 'pie',
					'name': 'neurological disorde',
					'domain': {'x': [.52, 1],
							   'y': [.51, 1]},
					'hoverinfo': 'label+value+name',
					'textinfo': 'none',
					"hole": .4,

				},
				{
					'labels': ["CHD (congenital heart disease)", "CDH (congenital diaphragmatic hernia)",
							   "CS (cantu syndrome)", "anophthalmia microphthalmia", ],
					'values': [1900, 48, 4, 8],
					# 'marker': {'colors': ['rgb(33, 75, 99)',
					#                       'rgb(79, 129, 102)',
					#                       'rgb(151, 179, 100)',
					#                       'rgb(175, 49, 35)',
					#                       'rgb(36, 73, 147)']},
					'type': 'pie',
					'name': 'birth defect',
					'domain': {'x': [0, .48],
							   'y': [0, .49]},
					'hoverinfo': 'label+value+name',
					'textinfo': 'none',
					"hole": .4,
				},
				{
					'labels': ["Fetal (PTB)", "Fetal (non-PTB)", "siblin control", "uncharacterized (Mixed healthy)"],
					'values': [13450, 22976, 80689, 108427],
					'marker': {'colors': ['rgb(146, 123, 21)',
					                      'rgb(177, 180, 34)',
					                      'rgb(206, 206, 40)',
					                      'rgb(175, 51, 21)',
					                      'rgb(35, 36, 21)']},
					'type': 'pie',
					'name': 'control study',
					'domain': {'x': [.52, 1],
							   'y': [0, .49]},
					'hoverinfo': 'label+value+name',
					'textinfo': 'none',
					"hole": .4,
				}
			],
			'layout': {
				"height": 420,
				"width": 500,
				"margin": {
					"l": 1,
					"r": 1,
					"b": 20,
					"t": 38
				},
				# "legend": {
				# 	"orientation": "h"
				# },
				'title': '<b>DNM Statistics</b>',
				'showlegend': False,
				"annotations": [
					{
						"font": {
							"size": 12
						},
						"showarrow": False,
						"text": "<b>Psychiatric Disorder<br>DNM<br>Total:220312</b>",
						"x": 0.11,
						"y": 0.79
					},
					{
						"font": {
							"size": 12
						},
						"showarrow": False,
						"text": "<b>Neurological Disorder<br>DNM<br>Total:1219</b>",
						"x": 0.92,
						"y": 0.79
					},
					{
						"font": {
							"size": 12
						},
						"showarrow": False,
						"text": "<b>Birth Defect<br>DNM<br>Total:1960</b>",
						"x": 0.16,
						"y": 0.20
					},
					{
						"font": {
							"size": 12
						},
						"showarrow": False,
						"text": "<b>Control Study<br>DNM<br>Total:225542</b>",
						"x": 0.85,
						"y": 0.20
					},
				]
			}
		}

		# plotly.offline.plot(fig, show_link=False)
		return plotly.offline.plot(fig, show_link=False, output_type="div")


if __name__ == '__main__':
	pie = DNMPie()
	pie.get_pie()
