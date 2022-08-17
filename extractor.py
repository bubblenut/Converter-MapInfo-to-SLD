import re

def extractKey(line)->str:
    res = ""
    res  = re.sub("<", "&lt;", re.sub(">", "&gt;", line))
    return res


def extractStyle(line)->str:
    style = line
    style = re.sub("^\w*_g_", "", style)
    style = re.sub("<MI_STYLE>", "", style)
    style = re.sub("</MI_STYLE>", "", style)
    style = re.sub("Pen", "Pen ", style)
    style = re.sub("Brush", "Brush ", style)
    style = re.sub("Symbol", "Symbol ", style)
    style = re.sub(",", ", ", style)
    style = re.sub(",\s\s", ", ", style)
    return style