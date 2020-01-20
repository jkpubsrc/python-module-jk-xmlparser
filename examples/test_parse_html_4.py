#!/usr/bin/python3



import os

import jk_xmlparser

from jk_simplexml import *



USER = "jknauth"
FILE_PATH = "/home/" + USER + "/DevExperiments/PDF2HTML/x/Peldszus - 2014 - Towards segment-based recognition of argumentation.html"


with open(FILE_PATH, "r") as f:
	TEXT_DATA = f.read()


def debugMessageWriter(text):
	print("DEBUG: " + text)



domParser = jk_xmlparser.HtmlDOMParser(bPreserveLineEndings = True)
#xRoot = domParser.parseText(TEXT_DATA, debugMessageWriter = debugMessageWriter)
xRoot = domParser.parseText(TEXT_DATA)

# NOTE: xRoot is of type HElement from jk_simplexml

xmlWriteSettings = XMLWriteSettings()
HSerializer.printDump(xRoot, xmlWriteSettings)













