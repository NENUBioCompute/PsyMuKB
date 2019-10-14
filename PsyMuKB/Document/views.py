# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        views
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-09-24
# @update:      2018-09-24 18:59
# @Software:    PyCharm
#-------------------------------------------------------------------------------
from . import app_Document
from flask import render_template

@app_Document.route('/UserGuide')
def Document():
	return render_template('Document.html')

@app_Document.route('/Instruction')
def Download():
	return render_template('Instruction.html')