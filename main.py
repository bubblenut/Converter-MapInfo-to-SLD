import MapInfoToSLD
import dictionary
import extractor
import logger

# name = "m_w"
name = input('Доступные имена:\n\tm_w\n\tm_r\n\tm_200\n\tm_25\n\tm_1k\n\tm_1\n\nВведите имя карты: ')
inputPath = 'inputs/' + name + "_input.txt"
errorsPath = 'errors/' + name + "_errors.txt"
stylePath = 'styles/' + name + "_Style.txt"


with open(inputPath, 'r', encoding='utf-8') as fin:
    with open(errorsPath, 'w', encoding='utf-8') as ferr:
        with open(stylePath, 'w', encoding='utf-8') as fout:

            fout.write(dictionary.styleHeading + '\n')
            i: int = 0
            for inpline in fin:
                i += 1

                #ключ для фильтра слд файла, уйдет в аутпут
                key: str = extractor.extractKey(inpline)

                #разложенный стиль для внутренней обработки конвертером
                style: str = extractor.extractStyle(inpline)
                print(str(i) + ": " + style)

                #удобный для чтения стиль, уйдет в файл лога
                layer: str = extractor.extractLayer(inpline)

                #пример ключа, стиля и лога
                # key: m_200_roads_g_ & lt;MI_STYLE & gt;Pen(1, 65, 15774720) & lt;/MI_STYLE & gt;
                # style: Pen,1,65,15774720'
                # layer: m_200_roads_g
                iscor: (bool, str) = logger.isCorrect(i, style, key, layer)
                if iscor[0]:
                    fout.write(MapInfoToSLD.convertLine(style, key))
                else:
                    ferr.write(iscor[1])
                continue

            fout.write(dictionary.styleFooting + '\n')

print('Конвертация завершена\n\n')
input("Нажмите Enter")
