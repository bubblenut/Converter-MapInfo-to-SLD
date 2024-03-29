import re
import dictionary

def convertSymbolTTF(line: str, key: str):
    symdict = dictionary.symbolDictTTF

    symattr = line.split(",")
    shape = int(symattr[1])
    color = re.sub('0x', '', '#' + str(hex(int(symattr[2].replace(")", "")))))
    # добавлен коэф размера, вероятно формула там сложнее, исправить, поискать
    if int(symattr[3]) > 16:
        size = str(0.35 * int(symattr[3]))
    else:
        size = symattr[3]

    fontname = symattr[4].strip("\"")
    fontstyle = symattr[5]

    res = '  <FeatureTypeStyle>' + '\n\t  <Rule>\n' + dictionary.filterHeading + key + dictionary.filterFooting

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

    return res + '\t  </Rule>\n' + '  </FeatureTypeStyle>\n\n'


def convertBrush(line: str, key: str):
    penDict = dictionary.penDict

    params = line.split(",")

    widthPen:str = params[1]
    patternPen:int = int(params[2])
    colorPen:str = re.sub('0x', '', '#'+str(hex(int(params[3].replace(")", "")))))
    patternBrush:str = params[5]
    colorMain:str = re.sub('0x', '', '#'+str(hex(int(params[6].replace(')', '')))))
    colorBg:str = re.sub('0x', '', '#'+str(hex(int(params[7].replace(')', '')))))

    #смешивание цветов фона и основного цвета для 15 шаблона
    if int(patternBrush) == 15:
        cmhex = re.sub("0x", "", str(hex(int(params[6])))).zfill(6)
        cbhex = re.sub("0x", "", str(hex(int(params[7])))).zfill(6)
        rres = hex(round((int(cmhex[:2], 16) + int(cbhex[:2], 16)) / 2))
        gres = hex(round((int(cmhex[2:-2], 16) + int(cbhex[2:-2], 16)) / 2))
        bres = hex(round((int(cmhex[-2:], 16) + int(cbhex[-2:], 16)) / 2))

        rres = re.sub("0x", "", rres)
        gres = re.sub("0x", "", gres)
        bres = re.sub("0x", "", bres)

        colorMain = "#" + rres + gres + bres

    if int(patternPen) == 1 and int(patternBrush) == 1:
        return '\n'

    res = '  <FeatureTypeStyle>'  + '\n\t  <Rule>\n' + dictionary.filterHeading + key + dictionary.filterFooting

    #
    # if int(patternBrush) != 1 and int(patternBrush) != 0 :
    #     if (int(patternBrush) == 2 or int(patternBrush) == 15):
    #         for elem  in dictionary.brushDictSimple:
    #             if elem == 'colorMain':
    #                 elem = colorMain
    #             res += elem
    if int(patternBrush) != 1 and int(patternBrush) != 0 :
        if (int(patternBrush) == 2 or int(patternBrush) == 15):
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

    if int(widthPen) > 7:
        widthPen = str((int(widthPen) - 10) / 10)

    if patternPen != 1:
        for elem in penDict[patternPen]:
            if elem == 'width':
                elem = widthPen
            if elem == 'color':
                elem = colorPen
            res += elem

    return res + '\t  </Rule>\n' + '  </FeatureTypeStyle>\n\n'


def convertPen(line: str, key: str):
    dict = dictionary.penDict

    params = line.split(",")
    width = params[1]
    pattern = int(params[2])
    color = re.sub('0x', '', '#'+str(hex(int(params[3].replace(")", "")))))

    # конвертация толщины линий больше 7 из точек в пиксели
    if int(width) > 7:
        width = str((int(width) - 10) / 10)

    res = '  <FeatureTypeStyle>'  + '\n\t  <Rule>\n' + dictionary.filterHeading + key + dictionary.filterFooting

    for elem in dict[pattern]:
        if elem == 'width':
            elem = width
        if elem == 'color':
            elem = color
        res += elem

    return res + '\t  </Rule>\n' + '  </FeatureTypeStyle>\n\n'


def convertStyle(style: str, key: str) -> str:
    stylearr = style.split(",")
    if len(stylearr) == 8:
        return convertBrush(style, key)
    elif len(stylearr) == 7:
        return convertSymbolTTF(style, key)
    else:
        return convertPen(style, key)
