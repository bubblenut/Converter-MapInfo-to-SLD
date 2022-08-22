import MapInfoToSLD
import dictionary
import extractor
import logger
import xmlFiller


inputPath = 'inputs/input.txt'
errorsPath = 'errors/errors.txt'

#input("Нажмите ентер чтобы начать конвертацию\n")

with open(inputPath, 'r', encoding='utf-8') as fin, open(errorsPath, 'w', encoding='utf-8') as flog:
    fullStyle: str = ''
    i: int = 0
    layerPrev: str

    for  line in fin:
        i += 1
        print(i)
        layer: str = extractor.extractLayer(line)
        key: str = extractor.extractKey(line)
        style: str = extractor.extractStyle(line)
        # пример слоя, ключа и стиля
        # layer: m_200_roads_g
        # key: m_200_roads_g_ & lt;MI_STYLE & gt;Pen(1, 65, 15774720) & lt;/MI_STYLE & gt;
        # style: Pen,1,65,15774720'
        if i == 1:
            layerPrev = layer
        isCorrect: (bool, str) = logger.isCorrect(i,style, key, layer)

        if isCorrect[0]:
            if layer != layerPrev:
                with open('styles/' + layerPrev + "_Style.xml", 'w', encoding='utf-8') as fxml:
                    fxml.write(xmlFiller.createXml(layer))
                with open('styles/' + layerPrev + "_Style.sld", 'w', encoding='utf-8') as fsld:
                    fsld.write(dictionary.styleHeading + '\n')
                    fsld.write(fullStyle)
                    fsld.write(dictionary.styleFooting + '\n')
                fullStyle = ''
                fullStyle += MapInfoToSLD.convertStyle(style, key)
                layerPrev = layer
            else:
                fullStyle += MapInfoToSLD.convertStyle(style, key)
        else:
            flog.write(isCorrect[1] + '\n\n')
            continue


print("Конвертация успешно завершена\n")
#input("Нажмите Enter")