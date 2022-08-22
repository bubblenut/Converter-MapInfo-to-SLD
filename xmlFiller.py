import datetime
import dictionary

def createXml(layer) -> str:
    res = ''
    for elem in dictionary.xmlDict:
        if elem == 'layer':
            elem = layer
        if elem == 'date':
            elem = str(datetime.datetime.now())[:-3] + ' UTC'
        res += elem
    return res