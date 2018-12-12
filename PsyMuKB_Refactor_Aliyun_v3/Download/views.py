# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        views
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-09-24
# @update:      2018-09-24 21:33
# @Software:    PyCharm
#-------------------------------------------------------------------------------

from . import app_Download
from flask import render_template

@app_Download.route('/')
def Download():
	return render_template('Download.html')