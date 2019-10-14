# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# @file:        __init__.py
# @Author:      GuoSijia
# @Purpose:     
# @Created:     2018-09-24
# @update:      2018-09-24 17:07
# @Software:    PyCharm
#-------------------------------------------------------------------------------
from flask import Blueprint


app_Document = Blueprint("document", __name__, template_folder="templates")

from Document import views