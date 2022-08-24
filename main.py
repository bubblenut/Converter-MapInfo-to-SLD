import MapInfoToSLD
import dictionary
import extractor
import logger
import xmlFiller

inputPath = 'inputs/input.txt'
errorsPath = 'errors/errors.txt'


last: str
with open(inputPath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    last = lines[-1]

layercount: int = 0
with open(inputPath, 'r', encoding='utf-8') as fin, open(errorsPath, 'w', encoding='utf-8') as flog:
    fullStyle: str = ''
    i: int = 0
    layerPrev: str
    ulayers = set()

    for  line in fin:
        i += 1
        print(i)
        layer: str = extractor.extractLayer(line)
        key: str = extractor.extractKey(line)
        style: str = extractor.extractStyle(line)

        ulayers.add(layer)

        if i == 1:
            layerPrev = layer
        isCorrect: (bool, str) = logger.isCorrect(i,style, key, layer)

        if isCorrect[0]:
            if layer != layerPrev:
                with open('styles/' + layerPrev + "_Style.xml", 'w', encoding='utf-8') as fxml:
                    fxml.write(xmlFiller.createXml(layer))
                with open('styles/' + layerPrev + "_Style.sld", 'w', encoding='utf-8') as fsld:
                    fsld.write(dictionary.styleHeading + '\n\n\n')
                    fsld.write(fullStyle)
                    fsld.write(dictionary.styleFooting + '\n')
                fullStyle = ''
                fullStyle += MapInfoToSLD.convertStyle(style, key)
                layerPrev = layer
            else:
                fullStyle += MapInfoToSLD.convertStyle(style, key)
        else:
            if layer != layerPrev:
                with open('styles/' + layerPrev + "_Style.xml", 'w', encoding='utf-8') as fxml:
                    fxml.write(xmlFiller.createXml(layer))
                with open('styles/' + layerPrev + "_Style.sld", 'w', encoding='utf-8') as fsld:
                    fsld.write(dictionary.styleHeading + '\n\n\n')
                    fsld.write(fullStyle)
                    fsld.write(dictionary.styleFooting + '\n')
                fullStyle = ''
                flog.write(isCorrect[1] + '\n\n')
                layerPrev = layer
            else:
                flog.write(isCorrect[1] + '\n\n')

        if line == last:
            with open('styles/' + layerPrev + "_Style.xml", 'w', encoding='utf-8') as fxml:
                fxml.write(xmlFiller.createXml(layer))
            with open('styles/' + layerPrev + "_Style.sld", 'w', encoding='utf-8') as fsld:
                fsld.write(dictionary.styleHeading + '\n\n\n')
                fsld.write(fullStyle)
                fsld.write(dictionary.styleFooting + '\n')

        layercount = len(ulayers)



print("Конвертация успешно завершена\n" + "Должно быть " + str(layercount) + " стилей. Если их не столько - ошибка в конвертере")
input("Нажмите Enter")

# пример слоя, ключа и стиля
# layer: m_200_roads_g
# key: m_200_roads_g_ & lt;MI_STYLE & gt;Pen(1, 65, 15774720) & lt;/MI_STYLE & gt;
# style: Pen,1,65,15774720'