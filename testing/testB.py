#!/usr/bin/python3


import sys
import xml.sax
from xml.sax import saxutils, handler, make_parser

from jk_simplexml import *
import jk_xmlparser




with open("some-test-file.xml", "r") as f:
	TEXT_DATA = f.read()






class SAXConverter(handler.ContentHandler):

	def __init__(self):
		handler.ContentHandler.__init__(self)
		self.__rootElement = None
		self.__stack = []
	#

	def getRootElement(self) -> HElement:
		return self.__rootElement
	#
		
	def startDocument(self):
		# self._out.write("<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>\n")
		pass
	#

	def startElement(self, name, attrs):
		x = HElement(name, [ HAttribute(k, v) for k, v in attrs.items() ])
		if self.__stack:
			self.__stack[-1].children.append(x)
		self.__stack.append(x)

		if self.__rootElement is None:
			self.__rootElement = x
	#

	def endElement(self, name):
		del self.__stack[-1]
	#

	def characters(self, content):
		xElement = self.__stack[-1]
		if xElement.children:
			xLast = xElement.children[-1]
			if isinstance(xLast, HText):
				xLast.text += content
			else:
				xElement.children.append(HText(content))
		else:
			xElement.children.append(HText(content))
	#

	def ignorableWhitespace(self, content):
		xElement = self.__stack[-1]
		if xElement.children:
			xLast = xElement.children[-1]
			if isinstance(xLast, HText):
				xLast.text += content
			else:
				xElement.children.append(HText(content))
		else:
			xElement.children.append(HText(content))
	#
		
	def processingInstruction(self, target, data):
		#self._out.write("<?%s %s?>" % (target, data))
		pass
	#

#




saxConverter = SAXConverter()
xml.sax.parseString(TEXT_DATA, saxConverter)
xRoot = saxConverter.getRootElement()

xmlWriteSettings = XMLWriteSettings()
HSerializer.printDump(xRoot, xmlWriteSettings)











