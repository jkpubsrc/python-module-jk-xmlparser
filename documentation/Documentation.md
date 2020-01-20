Low Level Tokenization
======================

In `jk_xmlparser` the class `HtmlTokenizerImpl` implements the tokenization of a HTML file and delivers instances of the following type on request:

* `jk_xmlparser.TagBegin` if a begin tag has been encountered
* `jk_xmlparser.TagEnd` if an end tag has been encountered
* `jk_xmlparser.TagComment` if a comment has been encountered
* `jk_xmlparser.TagSpecial` if a tag of the style `<!abcdef...>` has been encountered
* `jk_tokenizingparsing.Token` if regular text content has been encountered

High Level Tokenization and Parsing
===================================

These tokens produced by `HtmlTokenizerImpl` are then used to perform high level tokenization/parsing and produce a DOM tree. This is done by an instance of `HtmlDOMParser`. Use this class like this:

```python
TEXT_DATA = ....
domParser = jk_xmlparser.HtmlDOMParser(normalizeStr=True, beTolerant=True)
xRoot = domParser.parseText(TEXT_DATA, sourceID=None)
```

This method returns a `HElement` object of package `jk_simplexml`.





