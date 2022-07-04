import MapInfoToSLD


def isCorrect(num, line):
    linearr = line.split()
    errortext  =  'В строке '  + str(num) + ' \' ' + line + '\': '
    iscorrect = True

    #Проверка на валидность Pen
    if len(linearr) == 4:
        if linearr[0] != 'Pen':
            iscorrect = False
            errortext += 'аттрибут \'Pen\' не найден, вместо него стоит ' + linearr[0] + ';'
        if int(linearr[1]) > 1000:
            iscorrect = False
            errortext += 'аттрибут ширины = ' + linearr [1] + '. Слишком широко;'
        if int(linearr[2]) < 0 or int(linearr[2]) > 127:
            iscorrect = False
            errortext += 'аттрибут шаблона линии содержит невалидное значение ' + linearr[2] + ';'
        if int(linearr[3]) < 0  or int(linearr[3]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета содержит невалидное знаение ' + linearr[3]
    #Проверка на валидность Brush
    elif len(linearr) == 8:
        if linearr[0] != 'Pen':
            iscorrect = False
            errortext += 'аттрибут \'Pen\' не найден, вместо него стоит ' + linearr[0] + ';'
        if int(linearr[1]) > 1000:
            iscorrect = False
            errortext += 'аттрибут ширины = ' + linearr [1] + '. Слишком широко;'
        if int(linearr[2]) < 0 or int(linearr[2]) > 127:
            iscorrect = False
            errortext += 'аттрибут шаблона линии содержит невалидное значение ' + linearr[2] + ';'
        if int(linearr[3]) < 0  or int(linearr[3]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета обводки содержит невалидное знаение ' + linearr[3]
        if linearr[4] != 'Brush':
            iscorrect = False
            errortext += 'аттрибут \'Brush\' не найден, вместо него стоит ' + linearr[0] + ';'
        if int(linearr[5]) < 1 or (int(linearr[5]) > 8 and int(linearr[5]) < 12) or int(linearr[5]) > 71:
            iscorrect = False
            errortext += 'аттрибут шаблона заливки содержит невалидное значение ' + linearr[4] + ';'
        if int(linearr[6]) < 0  or int(linearr[6]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета заливки содержит невалидное знаение ' + linearr[3]
        if int(linearr[7]) < 0  or int(linearr[7]) > 16777215:
            iscorrect = False
            errortext += 'аттрибут цвета фона содержит невалидное знаение ' + linearr[3]
    #проверка на количество аттрибутов
    else:
        iscorrect = False
        errortext += 'введены не все аттрибуты'

    errortext += '\n'

    return iscorrect, errortext