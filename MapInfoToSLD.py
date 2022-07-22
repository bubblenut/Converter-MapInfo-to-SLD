import re
import dictionary

denominator = '\n<MinScaleDenominator>34124</MinScaleDenominator>\n' + '<MaxScaleDenominator>2183916</MaxScaleDenominator>\n'

def splitLine(line):
    if 'Pen' in line and 'Brush' in line:
        res = re.split("\)\s", re.sub(',|\(|\n', '', line))
    else:
        res = re.sub(',|\(|\)\n', '', line)
    return res


def convertBrush(line, key):
  penDict = dictionary.penDict

  if len(line) == 2:
    penattr = line[0].split()
    widthPen = penattr[1]
    patternPen = int(penattr[2])
    colorPen = re.sub('0x', '', '#'+str(hex(int(penattr[3].replace(")", "")))))

    brushattr = line[1].split()
    patternBrush = brushattr[1]
    colorMain = re.sub('0x', '', '#'+str(hex(int(brushattr[2].replace(')', '')))))
    colorBg = re.sub('0x', '', '#'+str(hex(int(brushattr[3].replace(')', '')))))

    if int(patternPen) == 1 and int(patternBrush) == 1:
        return '\n'

    res = '<FeatureTypeStyle>' + '\n<Rule>\n' + dictionary.filterHeading + key + dictionary.filterFooting  + denominator

    if (int(patternBrush) != 1):
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


def convertPen(line, key):
    dict = dictionary.penDict

    penattr = line.split()
    width = penattr[1]
    pattern = int(penattr[2])
    color = re.sub('0x', '', '#'+str(hex(int(penattr[3].replace(")", "")))))

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


def convertLine(line, key):
  if len(line) == 2:
    return convertBrush(line, key)
  else:
    return convertPen(line, key)