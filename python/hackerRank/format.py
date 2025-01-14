def md_format(word, style):
	values = {
	"b": "**{text}**",
	"i": "_{text}_",
	"c": "`{text}`",
	"s": "~~{text}~~"
	}
	
	return values[style].format(text=word)

## Interesting use of format string method plus a dictionary. Note bracket notation of [style] and that the text in the dictionary within braces is the same text that appears in the return line.