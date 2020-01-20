#!/usr/bin/python3



import jk_xmlparser

from jk_simplexml import *




TEXT_DATA = """<html lang="en">
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













