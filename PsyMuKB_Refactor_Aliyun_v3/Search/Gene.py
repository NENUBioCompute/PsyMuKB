# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        gene
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-09-24
# @update:      2018-09-24 22:33
# @Software:    PyCharm
#-------------------------------------------------------------------------------
from . import app_Search
import Forms
from Base import compute
from flask import render_template
from Visualization import VisualizeProteinProteinNetwork
from Visualization import VisualizeMouseBrainExpression
from Visualization import VisualizeGSExpression
from Visualization import Transcript_DNM_visualization, Visualization_of_regulatory_element_DNMs
from Visualization import VisualizeGtexGeneExpress
from Visualization import VisulizationCNV, VisualizeBrainSpanExpression
from Search import GetDisorderAndMutationTableData
import Visualization.VisualizeProteinExpressInGenePage as VAPEIG


@app_Search.route('/Gene/', methods=['GET', 'POST'])
def index():
	name = None
	form = Forms.NewForm()
	if form.validate_on_submit():
		name = form.name.data
		source = compute.Datafinder(name)
		message = source.FindOne()
		form.name.data = ''
		return render_template('Gene.html', message=message)
	return render_template('Gene.html', form=form)

@app_Search.route('/Gene/<name>', methods=['GET', 'POST'])
def index2(name):
	form = Forms.NewForm()
	source = compute.Datafinder(name)
	message = source.FindOne()
	form.name.data = ''
	return render_template('Gene.html', message=message)

@app_Search.route('/GeneDetail/')
@app_Search.route('/GeneDetail/<name>')
def GeneDetail(name):
	source = compute.Datafinder(name)
	message = source.FindOne()
	get_disorder_and_mutation_data = GetDisorderAndMutationTableData.GetDisorderAndMutationTableData(name)
	if source.is_type(name) == "symbol":
		try:
			ppi = VisualizeProteinProteinNetwork.Main()
			nodes_edges = ppi.run(message[0]["ENTREZ_ID"])
		except:
			nodes_edges = None
		try:
			pic2 = VisualizeBrainSpanExpression.main(message[0]["ENTREZ_ID"])
		except:
			pic2 = None
		try:
			vmbe = VisualizeMouseBrainExpression.MouseBrainExpressPlot((message[0]["ENTREZ_ID"]))
			pic3_1 = vmbe.run()
		except:
			pic3_1 = None
		try:
			vgse = VisualizeGSExpression.EmbryonicExpressPlot((message[0]["ENTREZ_ID"]))
			pic3_2 = vgse.run()
		except:
			pic3_2 = None
		try:
			pic5 = Transcript_DNM_visualization.main(message[0]["ENTREZ_ID"])
		except:
			pic5 = None
		try:
			pic6 = Visualization_of_regulatory_element_DNMs.main(message[0]["ENTREZ_ID"])
		except:
			pic6 = None

		try:
			ggp = VisualizeGtexGeneExpress.gtex_gene_plot(message[0]["ENTREZ_ID"])   #转录本脑表达
			pic7 = ggp.plot()
		except:
			pic7 = None

		try:
			pic8 = VisulizationCNV.main(message[0]["ENTREZ_ID"])
		except:
			pic8 = None
		return render_template('GeneDetail.html',
							   message=message, nodes_edges=nodes_edges, pic2=pic2,
							   pic3_1=pic3_1, pic3_2=pic3_2, pic5=pic5, pic6=pic6,
							   pic7=pic7,
							   pic8=pic8)

	elif source.is_type(name) == "ID":
		try:
			name = str(name)
			ppi = VisualizeProteinProteinNetwork.Main()
			nodes_edges = ppi.run(name)
		except:
			nodes_edges = None
		try:
			name = str(name)
			pic2 = VisualizeBrainSpanExpression.main(name)
		except:
			pic2 = None
		try:
			vmbe = VisualizeMouseBrainExpression.MouseBrainExpressPlot(name)
			pic3_1 = vmbe.run()
		except:
			pic3_1 = None
		try:
			vgse = VisualizeGSExpression.EmbryonicExpressPlot(name)
			pic3_2 = vgse.run()
		except:
			pic3_2 = None
		try:
			protein_express_plot = VAPEIG.ProteinExpressPlot(name, "all")
			pic3_3 = protein_express_plot.plot()
		except:
			pic3_3 = None

		try:
			pic5 = Transcript_DNM_visualization.main(name)
		except:
			pic5 = None

		try:
			pic6 = Visualization_of_regulatory_element_DNMs.main(name)
		except:
			pic6 = None

		try:
			ggp = VisualizeGtexGeneExpress.gtex_gene_plot(name)  # 转录本脑表达
			pic7 = ggp.plot()
		except:
			pic7 = None

		try:
			pic8 = VisulizationCNV.main(name)
		except:
			pic8 = None
		# print(pic2)

		try:
			mutation_dict, mutation_count  = get_disorder_and_mutation_data.get_dam_statics()
		except:
			mutation_dict, mutation_count = None, None

		return render_template('GeneDetail.html',
							   message=message, nodes_edges=nodes_edges, pic2=pic2,
							   pic3_1=pic3_1, pic3_2= pic3_2, pic3_3= pic3_3,pic5=pic5, pic6=pic6,
							   pic7=pic7,name=name,
							   pic8=pic8, mutation_count=mutation_count,mutation_dict=mutation_dict)

@app_Search.route('/GeneDetailMutation/<name>/')
def GeneMutaion(name):
	# demo_str = "7468_ASD_frameshift"
	id, disorder, mutation_type = name.split("_")
	get_disorder_and_mutation_data = GetDisorderAndMutationTableData.GetDisorderAndMutationTableData(id)
	disorder_dict, mutation_count = get_disorder_and_mutation_data.get_dam_statics()
	data_dict = disorder_dict.get(disorder).get(mutation_type)
	# print(mutation_count.get(disorder).get(mutation_type))
	# print(data_dict)
	# print(len(data_dict))
	return render_template('GeneDetailMutation.html', data_dict = data_dict)

