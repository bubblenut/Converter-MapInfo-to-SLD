import MapInfoToSLD
import dictionary
import re


def isCorrect(num: int, style: str, key: str, layer: str) -> (bool, str):

    key = re.sub("&lt;", "<", key)
    key = re.sub("&gt;", ">", key)

    stylearr = style.split(",")

    errortext  =  str(num) + ' строка input.txt' + ' :\nВ таблице ' + layer + ':\nпо ключу ' + key + ':\n'
    iscorrect = True

    if len(stylearr) < 4 or len(stylearr) > 8:
        iscorrect = False
        errortext += 'Невалидная длина строки\n\n'
        return iscorrect, errortext
    elif len(stylearr) == 8:
        if stylearr[0] != 'Pen':
            iscorrect = False
            errortext += 'аттрибут \'Pen\' не найден, вместо него стоит ' + stylearr[0] + '; '
        if int(stylearr[1]) > 1000:
            iscorrect = False
            errortext += 'аттрибут ширины Pen = ' + stylearr [1] + '. Слишком широко;'
        if  int(stylearr[2]) not in dictionary.penDict:
            if int(stylearr[2]) != 1:
                iscorrect = False
                errortext += 'аттрибут шаблона линии содержит невалидное значение ' + stylearr[2] + '; '
        if int(stylearr[3]) < 0  or int(stylearr[3]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета обводки содержит невалидное значение ' + stylearr[3]
        if stylearr[4] != 'Brush':
            iscorrect = False
            errortext += 'аттрибут \'Brush\' не найден, вместо него стоит ' + stylearr[0] + '; '
        if stylearr[5] not in dictionary.brushPattern:
            iscorrect = False
            errortext += 'аттрибут шаблона заливки содержит невалидное значение ' + stylearr[5] + '; '
        if int(stylearr[6]) < 0  or int(stylearr[6]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета заливки содержит невалидное значение ' + stylearr[3]
        #if re.search('\D', stylearr[7]) != None or int(stylearr[7]) < 0  or int(stylearr[7]) > 16777215:
        if int(stylearr[7]) < 0 or int(stylearr[7]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета фона содержит невалидное значение ' + stylearr[7]
    elif len(stylearr) == 7:
        if stylearr[0] != 'Symbol':
            iscorrect = False
            errortext += 'аттрибут \'Symbol\' не найден, вместо него стоит ' + stylearr[0] + '; '
        if int(stylearr[1]) < 32:
            iscorrect = False
            errortext + 'аттрибут шаблона символа ttf содержит невалидное значение ' + stylearr[1] + ' Необходимо значение 32 или больше; '
        if int(stylearr[2]) < 0  or int(stylearr[2]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета содержит невалидное значение ' + stylearr[2]
        if int(stylearr[3]) < 1  or int(stylearr[3]) > 48:
            iscorrect =  False
            errortext += 'невалидный размер символа ' + stylearr[3]
        #не проверяю валидность имени шрифта
        #не проверяю валидность стиля шрифта
        #не проверяю валидность поворота
    elif stylearr[0] == 'Symbol' and (len(stylearr) == 4 or len(stylearr) == 5):
        iscorrect = False
        errortext += 'строка содержит тип неподходящий для конвертации Symbol'
        return iscorrect, errortext
    elif len(stylearr) == 4:
        if stylearr[0] != 'Pen':
            iscorrect = False
            errortext += 'аттрибут \'Pen\' не найден, вместо него стоит ' + stylearr[0] + '; '
        if int(stylearr[1]) > 1000:
            iscorrect = False
            errortext += 'аттрибут ширины = ' + stylearr [1] + '. Слишком широко;'
        if int(stylearr[2]) not in dictionary.penDict:
            iscorrect = False
            errortext += 'аттрибут шаблона линии содержит невалидное значение ' + stylearr[2] + ' (его пока нет в словаре); '
        if int(stylearr[3]) < 0  or int(stylearr[3]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета содержит невалидное знаение ' + stylearr[3]
    else:
        iscorrect = False
        errortext += 'невалидное количество аттрибутов'

    errortext += '\n\n'
    return iscorrect, errortext
