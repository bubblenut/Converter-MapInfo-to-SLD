import re
from pysld.style import StyleSld
import dictionary

def splitLine(line):
    if 'Pen' in line and 'Brush' in line:
        res = re.split("\)\s", re.sub(',|\(|\n', '', line))
    else:
        res = re.sub(',|\(|\)\n', '', line)
    return res


def convertBrush(line, key):
  brushDict = dictionary.brushDict
  penDict = dictionary.penDict

  if len(line) == 2:
    penattr = line[0].split()
    widthPen = penattr[1]
    patternPen = int(penattr[2])
    colorPen = re.sub('0x', '', '#'+str(hex(int(penattr[3].replace(")", "")))))

    brushattr = line[1].split()
    patternBrush = brushattr[1]
    colorMain = brushattr[2]
    colorBg = re.sub('0x', '', '#'+str(hex(int(brushattr[3].replace(")", "")))))

    res = ''
    res = res + dictionary.filterHeading + key + dictionary.filterFooting + '\n<Rule>'

    for elem in brushDict[patternBrush]:
        if elem == 'patternBrush':
            elem = '''<se:OnlineResource xlink:href="images/''' + dictionary.brushDict[patternBrush] + '''.svg?fill=+ '''+ colorMain + '''" xlink:type="simple"/>'''
        if elem == colorBg:
            elem = colorBg
        res += elem

    for elem in penDict[patternPen]:
        if elem == 'width':
            elem = widthPen
        if elem == 'color':
            elem = colorPen
        res += elem

  return res + '\n</Rule>'



def convertPen(line, key):
    dict = dictionary.penDict
    penattr = line.split()
    width = penattr[1]
    pattern = int(penattr[2])
    color = re.sub('0x', '', '#'+str(hex(int(penattr[3].replace(")", "")))))

    res = ''
    res = res + dictionary.filterHeading + key + dictionary.filterFooting + '\n<Rule>'

    for elem in dict[pattern]:
        if elem == 'width':
            elem = width
        if elem == 'color':
            elem = color
        res += elem

    return res + '\n</Rule>'


def convertLine(line, key):
  if len(line) == 2:
    return convertBrush(line, key)
  else:
    return convertPen(line, key)