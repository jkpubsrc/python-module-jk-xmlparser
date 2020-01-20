#!/usr/bin/python3


import jk_simplexml
import jk_xmlparser



with open("some-test-file.xml", "r") as f:
	TEXT_DATA = f.read()




parser = jk_xmlparser.XMLDOMParser(bEnableDebugging=True)
try:
	xRoot = parser.parseText(TEXT_DATA)
	assert isinstance(xRoot, jk_simplexml.HElement)
except jk_xmlparser.ParserErrorException as ee:
	print("ERROR")
	print("\tmessage = " + repr(ee.message))
	print("\tlocation = " + repr(ee.location))
	print("\ttextClip = " + ee.textClip)
	print("\tstateName = " + repr(ee.stateName))
else:
	xmlWriteSettings = jk_simplexml.XMLWriteSettings()
	jk_simplexml.HSerializer.printXML(xRoot, xmlWriteSettings)

	#with open("test.html", "w") as f:
	#	f.write(jk_simplexml.HSerializer.toHTMLDocStr(xRoot))

parser._debugging_saveProtocols("test-protocols-")

















