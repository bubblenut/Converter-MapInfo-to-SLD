import MapInfoToSLD
import dictionary
import re


def isCorrect(num, line)->(bool, str):

    linearr = re.sub(',|\(|\n|\)', '', line).split()
    errortext  =  'В строке '  + str(num) + ' \' ' + line + '\': '
    iscorrect = True

    if len(linearr) < 4 or len(linearr) > 8:
        iscorrect = False
        errortext += 'Невалидная длина строки\n\n'
        return iscorrect, errortext
    elif len(linearr) == 8:
        if linearr[0] != 'Pen':
            iscorrect = False
            errortext += 'аттрибут \'Pen\' не найден, вместо него стоит ' + linearr[0] + '; '
        if int(linearr[1]) > 1000:
            iscorrect = False
            errortext += 'аттрибут ширины Pen = ' + linearr [1] + '. Слишком широко;'
        if  int(linearr[2]) not in dictionary.penDict:
            if int(linearr[2]) != 1:
                iscorrect = False
                errortext += 'аттрибут шаблона линии содержит невалидное значение ' + linearr[2] + '; '
        if int(linearr[3]) < 0  or int(linearr[3]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета обводки содержит невалидное значение ' + linearr[3]
        if linearr[4] != 'Brush':
            iscorrect = False
            errortext += 'аттрибут \'Brush\' не найден, вместо него стоит ' + linearr[0] + '; '
        if linearr[5] not in dictionary.brushPattern:
            iscorrect = False
            errortext += 'аттрибут шаблона заливки содержит невалидное значение ' + linearr[5] + '; '
        if int(linearr[6]) < 0  or int(linearr[6]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета заливки содержит невалидное значение ' + linearr[3]
        if re.search('\D', linearr[7]) != None or int(linearr[7]) < 0  or int(linearr[7]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета фона содержит невалидное значение ' + linearr[3]
    elif len(linearr) == 7:
        if linearr[0] != 'Symbol':
            iscorrect = False
            errortext += 'аттрибут \'Symbol\' не найден, вместо него стоит ' + linearr[0] + '; '
        if int(linearr[1]) < 32:
            iscorrect = False
            errortext + 'аттрибут шаблона символа ttf содержит невалидное значение ' + linearr[1] + ' Необходимо значение 32 или больше; '
        if int(linearr[2]) < 0  or int(linearr[2]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета содержит невалидное значение ' + linearr[2]
        if int(linearr[3]) < 1  or int(linearr[3]) > 48:
            iscorrect =  False
            errortext += 'невалидный размер ' + linearr[3]
        #не проверяю валидность имени шрифта
        #не проверяю валидность стиля шрифта
        #не проверяю валидность поворота
    elif len(linearr) == 4:
        if linearr[0] != 'Pen':
            iscorrect = False
            errortext += 'аттрибут \'Pen\' не найден, вместо него стоит ' + linearr[0] + '; '
        if int(linearr[1]) > 1000:
            iscorrect = False
            errortext += 'аттрибут ширины = ' + linearr [1] + '. Слишком широко;'
        if int(linearr[2]) not in dictionary.penDict:
            iscorrect = False
            errortext += 'аттрибут шаблона линии содержит невалидное значение ' + linearr[2] + '; '
        if int(linearr[3]) < 0  or int(linearr[3]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета содержит невалидное знаение ' + linearr[3]
    elif linearr[0] == 'Symbol' and (len(linearr) == 4 or len(linearr) == 5):
        iscorrect = False
        errortext += 'строка содержит тип неподходящий для конвертации тип Symbol'
    else:
        iscorrect = False
        errortext += 'невалидное количество аттрибутов'

    errortext += '\n\n'
    return iscorrect, errortext


    #Проверка на количество аттрибутов в целом
    # if len(linearr) != 8 and len(linearr) != 4:
    #     if len(linearr) != 0 and linearr[0] == 'Symbol':
    #         iscorrect = False
    #         errortext += 'строка содержит Symbol\n\n'
    #         return iscorrect, errortext
    #     iscorrect = False
    #     errortext += 'введены не все аттрибуты\n\n'
    #     return iscorrect, errortext