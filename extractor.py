import re

def extractLayer(line: str) -> str:
    layer = line.split("\t")[0]
    return layer

def extractKey(line: str) -> str:
    key = re.sub("<", "&lt;", re.sub(">", "&gt;", line.strip('\n')))
    key = re.sub("^\w*\s", "", key)
    return key


def extractStyle(line:str) -> str:
    style = line
    style = re.sub("^[\w\s]*<MI_STYLE>", "", style)
    style = re.sub("</MI_STYLE>", "", style)
    style = re.sub("Pen", "Pen,", style)
    style = re.sub("Brush", "Brush,", style)
    style = re.sub("Symbol[^s\"]", "Symbol,", style)
    style = re.sub(",\s+", ",", style)
    style = re.sub("\(|\)", "", style)
    style = re.sub("\sBrush", ",Brush", style)
    style = re.sub("\n", "", style)
    return style
