# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        __init__.py
# @Author:      GuoSijia
# @Purpose:     搜索页模块
# @Created:     2018-09-24
# @update:      2018-09-24 17:07
# @Software:    PyCharm
#-------------------------------------------------------------------------------
from flask import Blueprint


app_Search = Blueprint("search", __name__, template_folder="templates")

# import views
from Search import views, Gene, Mutatioin