#!/usr/bin/python3

import os

from jk_simplexml import *
from jk_xmlparser import *


BASEDIR = "/media/jknauth/ac513147-21ad-456b-b0eb-a36a4b1cc7d7"
BASEDIR = "/mounts/net/sdcard"

with open(BASEDIR + "/Temp/file2.txt", "r") as f:
	path = f.readline().strip()



p = XMLDOMParser()
xmlWriteSettings = XMLWriteSettings()

if os.path.isfile(path):
	xRoot = p.parseFile(path)
	#HSerializer.writeXML(xRoot, xmlWriteSettings)

	with open(BASEDIR + "/Temp/file.html", "w") as f:
		f.write(HSerializer.toHTMLDocStr(xRoot))
	#HSerializer.printXML(xRoot, xmlWriteSettings)
	HSerializer.printDump(xRoot, xmlWriteSettings)

elif os.path.isdir(path):
	for fileEntry in sorted(os.listdir(path)):
		try:
			xRoot = p.parseFile(os.path.join(path, fileEntry))
			print("SUCCESS :: " + repr(fileEntry))
		except ParserErrorException as ee:
			print()
			print("TOKENIZATION ERROR :: " + repr(fileEntry))
			print("\tmessage = " + repr(ee.message))
			print("\tlocation = " + repr(ee.location))
			print("\ttextClip = " + ee.textClip)
			print("\tstateName = " + repr(ee.stateName))
			break
		except KeyboardInterrupt as ee:
			print()
			print("INTERRUPTED.")
			break
		except:
			print()
			print("GENERAL ERROR :: " + repr(fileEntry))
			xRoot = p.parseFile(os.path.join(path, fileEntry))

else:
	print("???? " + path)

















