import MapInfoToSLD
import dictionary
import extractor
import logger
import xmlFiller


inputPath = 'inputs/input.txt'
errorsPath = 'errors/errors.txt'

allLayers = {}
with open(inputPath, 'r', encoding='utf-8') as fillmapfile, open(errorsPath, 'w', encoding='utf-8') as flog:
    for line in fillmapfile:
        allLayers[extractor.extractLayer(line)] = ''

with open(inputPath, 'r', encoding='utf-8') as fin:
    with open(errorsPath, 'w', encoding='utf-8') as ferr:
        i: int = 0
        for line in fin:
            i += 1
            print(i)
            layer: str = extractor.extractLayer(line)
            key: str = extractor.extractKey(line)
            style: str = extractor.extractStyle(line)

            isCorrect: (bool, str) = logger.isCorrect(i,style, key, layer)
            if isCorrect[0]:
                allLayers[layer] += MapInfoToSLD.convertStyle(style,key) + '\n'
            else:
                ferr.write(isCorrect[1] + '\n\n')

for elem in allLayers:
    with open('styles/' + elem + "_Style.xml", 'w', encoding='utf-8') as fxml:
        fxml.write(xmlFiller.createXml(layer))
    with open('styles/' + elem + "_Style.sld", 'w', encoding='utf-8') as fsld:
        fsld.write(dictionary.styleHeading + '\n\n\n')
        fsld.write(allLayers[elem])
        fsld.write(dictionary.styleFooting + '\n')

print('Конвертация завершена\n\n')
input("Нажмите Enter")

# пример ключа, стиля и слоя
# key: m_200_roads_g_ & lt;MI_STYLE & gt;Pen(1, 65, 15774720) & lt;/MI_STYLE & gt;
# style: Pen,1,65,15774720'
# layer: m_200_roads_g
