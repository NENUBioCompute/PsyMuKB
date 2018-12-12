# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        Forms
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-09-24
# @update:      2018-09-24 0:35
# @Software:    PyCharm
#-------------------------------------------------------------------------------
from Base import compute
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, BooleanField, SelectField, HiddenField
from wtforms.fields import core
from wtforms.validators import Required


class NewForm(FlaskForm):
	name = StringField('Please Enter A Gene ID', validators=[Required()])
	submit = SubmitField('Submit')


class SearchForm(FlaskForm):
	name = StringField(' ', validators=[Required()],  render_kw={"placeholder": "Gene symbol / Gene ID / Chr. position"})
	submit = SubmitField('Submit')


class SearchForm2(FlaskForm):
	name = StringField('Gene ID or Symbol', validators=[Required()])
	submit = SubmitField('Submit', id='notice')


class GeneForm(FlaskForm):
	adname = StringField('Gene ID or Symbol', id='sf', validators=[Required()])
	adsubmit = SubmitField('Submit')


class AdvancedForm(FlaskForm):
	# adname = StringField('Chr',id='sf2',validators=[Required()])

	Chr = SelectField("Chr",
					  coerce=int,
					  id='sf',
					  choices=[(1, 'All'),
							   (2, '1'),
							   (3, '2'),
							   (4, '3'),
							   (5, '4'),
							   (6, '5'),
							   (7, '6'),
							   (8, '7'),
							   (9, '8'),
							   (10, '9'),
							   (11, '10'),
							   (12, '11'),
							   (13, '12'),
							   (14, '13'),
							   (15, '14'),
							   (16, '15'),
							   (17, '16'),
							   (18, '17'),
							   (19, '18'),
							   (20, '19'),
							   (21, '20'),
							   (22, '21'),
							   (23, '22'),
							   (24, 'X'),
							   (25, 'Y')])
	start = StringField('Start', id='sf3', validators=[])
	end = StringField('End', id='sf4', validators=[])

	DNV = SelectField("Mutation_Type",
					  coerce=int,
					  id='sf',
					  choices=[(1, 'exonic'),
							   (2, 'splicing'),
							   (3, 'intergenic'),
							   (4, 'intronic'),
							   (5, 'upstream'),
							   (6, 'missense'),
							   (7, "UTR3"),
							   (8, "UTR5")])
	disorder = SelectField("Disorders",
						   coerce=int,
						   id='sf',
						   choices=[(1, 'Psychiatric Disorder - Attention Deficit Hyperactivity Disorder(ADHD)'),
									(2, 'Psychiatric Disorder - Autism(ASD)'),
									(3, 'Psychiatric Disorder - Bipolar Disorder(BD)'),
									(4, 'Psychiatric Disorder - Developmental Delay(DD)'),
									(5, 'Psychiatric Disorder - Intellectual Disability(ID)'),
									(6, 'Psychiatric Disorder - Sotos syndrome(Sotos)'),
									(7, 'Psychiatric Disorder - Mental Retardation(MR)'),
									(8, 'Psychiatric Disorder - Obsessive Compulsive Disorder(OCD)'),
									(9, 'Psychiatric Disorder - Schizophrenia(SCZ)'),
									(10, 'Psychiatric Disorder - Tourette Disorder(TD)'),
									(11, 'Psychiatric Disorder - Psychosis not specified(PDNOS)'),
									(12, 'Neurological Disorde - Developmental and Epileptic Encephalopathies(DEE)'),
									(13, 'Neurological Disorder - Epileptic Encephalopathies(EE)'),
									(14, 'Neurological Disorder - Alzheimer Disorder Early-onset(AD)'),
									(15, 'Neurological Disorder - Parkinson Disorder Early-onset(PD)'),
									(16, 'Neurological Disorder - Amyotrophic Lateral Sclerosis(ALS)'),
									(17, 'Neurological Disorder - Cerebral Palsy(CP)'),
									(18, 'Neurological Disorder - Neural Tube Defects(NTD)'),
									(19, 'Neurological Disorder - Sporadic Infantile Spasm Syndrome(IS)'),
									(20, 'Birth Defect - Congenital Heart Disease(CHD)'),
									(21, 'Birth Defect - Acromelic Frontonasal Dysostosis(AFND)'),
									(22, 'Birth Defect - Anophthalmia and Microphthalmia(A/M)'),
									(23, 'Birth Defect - Cantu Syndrome(CS)'),
									(24, 'Birth Defect - Congenital Diaphragmatic Hernia(CDH)'),
									(25, 'Control Study - Fetal (Preterm birth)'),
									(26, 'Control Study - Fetal (Non-Preterm birth)'),
									(27, 'Control Study - Control(CTR)'),
									(28, 'Control Study - Control(SSC)(CTR)'),
									(29, 'Control Study - Uncharacterized(Uncharacterized)')])


	submit2 = SubmitField('Submit')


class AdvancedForm2(FlaskForm):
	#Using CNV Form
	# adname = StringField('Chr',id='sf2',validators=[Required()])

	Chr2 = SelectField("Chr",
					   coerce=int,
					   id='sf',
					   choices=[(1, 'All'),
								(2, '1'),
								(3, '2'),
								(4, '3'),
								(5, '4'),
								(6, '5'),
								(7, '6'),
								(8, '7'),
								(9, '8'),
								(10, '9'),
								(11, '10'),
								(12, '11'),
								(13, '12'),
								(14, '13'),
								(15, '14'),
								(16, '15'),
								(17, '16'),
								(18, '17'),
								(19, '18'),
								(20, '19'),
								(21, '20'),
								(22, '21'),
								(23, '22'),
								(24, 'X'),
								(25, 'Y')])
	start2 = StringField('Start', id='sf3', validators=[])
	end2 = StringField('End', id='sf4', validators=[])

	CNV = SelectField("Mutation_Type",
					  coerce=int,
					  id='sf',
					  choices=[(1, 'Del'),
							   (2, 'Dup')])
	disorder2 = SelectField("Disorders",
							coerce=int,
							id='sf',
							choices=[(1, 'Attention Deficit Hyperactivity Disorder'),
									 (2, 'Autism'),
									 (3, 'Bipolar Disorder'),
									 (4, 'Control'),
									 (5, 'Intellectual Disability'),
									 (6, 'Obsessive-Compulsive Disorder'),
									 (7, 'Schizophrenia'),
									 (8, 'Tourette Disorder')])

	submit3 = SubmitField('Submit')


class MutationsMrnaForm(FlaskForm):

	mrna_radio = core.RadioField(
        label="mRNA – level impact",
        choices=(
            ("m1",'all mRNA isoforms'),
            ("m2",'mRNA isoforms with coding regions being impact <abbr title="The mRNA isoforms of the selected mutation falls on the exon"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></abbr>'),
			("m3",'brain expressed mRNA isoforms  <abbr title="Have one expressed value of startswith brain tissue(log2(TPM+1) >= 1)"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></abbr>'),
			("m4", 'mRNA isoforms with coding regions being impact and brain expressed mRNA isoforms  <abbr title="The mRNA isoforms of the selected mutation falls on the exon and have one expressed value of startswith brain tissue(log2(TPM+1) >= 1"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></abbr>')
        ),
		default="m1"
        # coerce=int  #限制是int类型的
    )
	mrna_submit = SubmitField('Show')

class MutationProteinForm(FlaskForm):

	protein_radio = core.RadioField(
		label="Protein – level impact",
		choices=(
			("p1", 'all proteins'),
			("p2", 'Impacted proteins  <abbr title="The transcript of the selected mutation falls on the exon"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></abbr>'),
			("p3", 'brain expressed proteins <abbr title="The expressed value of brain (Median protein expression, lg normalized iBAQ intensit) >=0.5 )"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></abbr>'),
			("p4", 'Impacted proteins and brain expressed proteins <abbr title="The transcript of the selected mutation falls on the exon and expressed value of brain (Median protein expression, lg normalized iBAQ intensit) >=0.5 )"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></abbr>'),
		),
		default="p1"
		# coerce=int  #限制是int类型的
	)
	protein_submit = SubmitField('Show')

