import MapInfoToSLD
import dictionary
import extractor
import logger
import xmlFiller
import re

name:str = ("")
inputPath = 'inputs/input.txt'
errorsPath = 'errors/' + name + 'errors.txt'

allLayers = {}
headings={}
with open(inputPath, 'r', encoding='utf-8') as fillmapfile, open(errorsPath, 'w', encoding='utf-8') as flog:
    for line in fillmapfile:
        allLayers[extractor.extractLayer(line)] = ''
        headings[extractor.extractLayer(line)] = extractor.extractKey(line)

with open(inputPath, 'r', encoding='utf-8') as fin:
    with open(errorsPath, 'w', encoding='utf-8') as ferr:
        i: int = 0
        brokenstyles: int = 0
        normalstyles: int = 0
        for line in fin:
            i += 1
            layer: str = extractor.extractLayer(line)
            key: str = extractor.extractKey(line)
            style: str = extractor.extractStyle(line)

            isCorrect: (bool, str) = logger.isCorrect(i, style, key, layer)
            if isCorrect[0]:
                normalstyles += 1
                print(str(i) + " ", layer + ": OK")
                allLayers[layer] += MapInfoToSLD.convertStyle(style, key) + '\n'
            else:
                brokenstyles += 1
                print(str(i) + " ", layer + ": ушел в лог")
                ferr.write(isCorrect[1] + '\n\n')


        with open("errors/"+ name + "stat.txt", "w", encoding="utf-8") as fstat:
            fstat.write("Входной файл " + str(fin.name) + "\n\n")
            fstat.write("Всего прочитано " + "строк: "  + str(i) + "\n")
            fstat.write("Среди них правильных стилей: " + str(normalstyles) + "\n")
            fstat.write("Неконвертируемых стилей: " + str(brokenstyles) + "\n")
            fstat.write("Уникальных пар sld c xml должно быть: " + str(len(allLayers)) + "\n")

for elem in allLayers:
    print(elem)
    with open(name + 'styles/' + elem + "_Style.xml", 'w', encoding='utf-8') as fxml:
        fxml.write(xmlFiller.createXml(elem))
    with open(name + 'styles/' + elem + "_Style.sld", 'w', encoding='utf-8') as fsld:
        if allLayers[elem] == '':
            allLayers[elem] = dictionary.emerencyStyle
        fsld.write(re.sub("_STYLE_", headings[elem], dictionary.styleHeading) + '\n\n\n')
        fsld.write(allLayers[elem])
        fsld.write(dictionary.styleFooting + '\n')

print('\nКонвертация завершена')
input("Нажмите Enter")

# пример ключа, стиля и слоя
# key: m_200_roads_g_ & lt;MI_STYLE & gt;Pen(1, 65, 15774720) & lt;/MI_STYLE & gt;
# style: Pen,1,65,15774720'
# layer: m_200_roads_g
