import MapInfoToSLD
import dictionary
import extractor
import logger
import xmlFiller


inputPath = 'inputs/input.txt'
errorsPath = 'errors/errors.txt'

input("Нажмите ентер чтобы начать конвертацию\n")



with open(inputPath, 'r', encoding='utf-8') as fin:
    with open(errorsPath, 'w', encoding='utf-8') as ferr:

        layerPrev: str = extractor.extractLayer(fin.readline())
        fullStyle: str = ''
        i: int = 0

        for inpline in fin:

            i += 1
            key: str = extractor.extractKey(inpline)
            style: str = extractor.extractStyle(inpline)
            layer: str = extractor.extractLayer(inpline)
            iscor: (bool, str) = logger.isCorrect(i, style, key, layer)

            if layer != layerPrev:
                stylePath = 'styles/' + layerPrev + "_Style.sld"
                xmlPath = 'styles/' + layerPrev + "_Style.xml"
                with open(xmlPath, 'w', encoding='utf-8') as fxml:
                    #заполянем метаданными файл xml
                    fxml.write(xmlFiller.createXml(layer))
                with open(stylePath, 'w', encoding='utf-8') as fsld:
                    #заполняем стилем файл sld
                    fsld.write(dictionary.styleHeading + '\n')
                    fsld.write(fullStyle)
                    fsld.write(dictionary.styleFooting + '\n')

                layerPrev = layer
                fullStyle = ''
                if iscor[0]:
                    fullStyle += MapInfoToSLD.convertStyle(style, key)
                else:
                    ferr.write(iscor[1])
                continue
            else:
                if iscor[0]:
                    fullStyle += MapInfoToSLD.convertStyle(style, key)
                else:
                    ferr.write(iscor[1])
                continue


print('Конвертация завершена\n\n')
input("Нажмите Enter")

# пример ключа, стиля и слоя
# key: m_200_roads_g_ & lt;MI_STYLE & gt;Pen(1, 65, 15774720) & lt;/MI_STYLE & gt;
# style: Pen,1,65,15774720'
# layer: m_200_roads_g
