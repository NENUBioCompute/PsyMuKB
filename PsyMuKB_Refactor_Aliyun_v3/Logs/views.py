# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        views
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-11-14
# @update:      2018-11-14 10:25
# @Software:    PyCharm
#-------------------------------------------------------------------------------
from . import app_Logs
from flask import render_template
import json

@app_Logs.route('/')
def logs():
	return render_template('Logs.html')