# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        __init__.py
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-11-14
# @update:      2018-11-14 10:24
# @Software:    PyCharm
#-------------------------------------------------------------------------------
from flask import Blueprint


app_Logs = Blueprint("logs", __name__, template_folder="templates")

# import views
from Logs import views