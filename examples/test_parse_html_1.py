#!/usr/bin/python3



import jk_xmlparser

from jk_simplexml import *




TEXT_DATA = """<!doctype html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">
<!-- This is a comment -->
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="css/styles.css?v=1.0">
  	</head>
	<body>
		<hr/>
		<script src="js/scripts.js"></script>
		<h1>Heading 1</h1>
		<p>
			Test
			< br />
			<img src = "bla" width = "abc" height = 123 important />
		</p>
	</body>
</html>
"""





domParser = jk_xmlparser.HtmlDOMParser(True, True)
xRoot = domParser.parseText(TEXT_DATA, None)


xmlWriteSettings = XMLWriteSettings()
HSerializer.printDump(xRoot, xmlWriteSettings)













