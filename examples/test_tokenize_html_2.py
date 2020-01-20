#!/usr/bin/python3



import jk_xmlparser




TEXT_DATA = """<!-- This is a comment -->
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




tok = jk_xmlparser.HtmlTokenizerImpl()
for t in tok.tokenizeText(TEXT_DATA):
	print(t)



















