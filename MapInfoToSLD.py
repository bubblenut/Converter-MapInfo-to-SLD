import re
import dictionary

#denominator = '\n<MinScaleDenominator>534</MinScaleDenominator>\n' + '<MaxScaleDenominator>2183916</MaxScaleDenominator>\n'
denominator = ''

def convertSymbolTTF(line: str, key: str):
    symdict = dictionary.symbolDictTTF

    symattr = line.split(",")
    shape = int(symattr[1])
    color = re.sub('0x', '', '#' + str(hex(int(symattr[2].replace(")", "")))))
    size = symattr[3]
    fontname = symattr[4].strip("\"")
    fontstyle = symattr[5]

    res = '<FeatureTypeStyle>' + '\n<Rule>\n' + dictionary.filterHeading + key + dictionary.filterFooting + denominator

    for elem in symdict:
        if elem == 'shape':
            elem = shape
        if elem == 'color':
            elem = color
        if elem == 'size':
            elem = size
        if elem == 'fontname':
            elem = fontname
        if elem == 'fontstyle':
            elem = fontstyle
        res += str(elem)

    return res + '\n</Rule>\n' + '</FeatureTypeStyle>\n'


def convertBrush(line: str, key: str):
    penDict = dictionary.penDict

    params = line.split(",")

    widthPen = params[1]
    patternPen = int(params[2])
    colorPen = re.sub('0x', '', '#'+str(hex(int(params[3].replace(")", "")))))
    patternBrush = params[5]
    colorMain = re.sub('0x', '', '#'+str(hex(int(params[6].replace(')', '')))))
    colorBg = re.sub('0x', '', '#'+str(hex(int(params[7].replace(')', '')))))


    if int(patternPen) == 1 and int(patternBrush) == 1:
        return '\n'

    res = '<FeatureTypeStyle>' + '\n<Rule>\n' + dictionary.filterHeading + key + dictionary.filterFooting  + denominator

    if int(patternBrush) != 1 and int(patternBrush) != 0:
        if (int(patternBrush) == 2):
            for elem  in dictionary.brushDictSimple:
                if elem == 'colorMain':
                    elem = colorMain
                res += elem
        else:
            for elem in dictionary.brushDict:
                if elem == 'pattern':
                    elem = '''<OnlineResource xlink:href="images/''' + str(dictionary.brushPattern[patternBrush]) + '''.svg?fill='''+ colorMain + '''" xlink:type="simple"/>'''
                if elem == 'colorBg':
                    elem = colorBg
                res += elem

    if patternPen != 1:
        for elem in penDict[patternPen]:
            if elem == 'width':
                elem = widthPen
            if elem == 'color':
                elem = colorPen
            res += elem

    return res + '\n</Rule>\n' + '</FeatureTypeStyle>\n'


def convertPen(line: str, key: str):
    dict = dictionary.penDict

    params = line.split(",")
    width = params[1]
    pattern = int(params[2])
    color = re.sub('0x', '', '#'+str(hex(int(params[3].replace(")", "")))))

    # конвертация толщины линий больше 7 из точек в пиксели
    if int(width) > 7:
        width = str((int(width) - 10) / 10)

    res = '<FeatureTypeStyle>'  + '\n<Rule>\n' + dictionary.filterHeading + key + dictionary.filterFooting + denominator

    for elem in dict[pattern]:
        if elem == 'width':
            elem = width
        if elem == 'color':
            elem = color
        res += elem

    return res + '\n</Rule>\n' + '</FeatureTypeStyle>\n'


def convertStyle(style: str, key: str) -> str:
    stylearr = style.split(",")
    if len(stylearr) == 8:
        return convertBrush(style, key)
    elif len(stylearr) == 7:
        return convertSymbolTTF(style, key)
    else:
        return convertPen(style, key)
