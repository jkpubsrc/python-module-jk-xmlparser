#!/usr/bin/python3



import os

import jk_xmlparser

from jk_simplexml import *



USER = "jknauth"
FILE_PATH = "/home/" + USER + "/DevExperiments/PDF2HTML/x/Peldszus - 2014 - Towards segment-based recognition of argumentation.html"


with open(FILE_PATH, "r") as f:
	TEXT_DATA = f.read().replace("content=\"text/html; charset=\"UTF-8\">", "content=\"text/html; charset=UTF-8\">")





tok = jk_xmlparser.HtmlTokenizerImpl()
for t in tok.tokenizeText(TEXT_DATA):
	print(t)













