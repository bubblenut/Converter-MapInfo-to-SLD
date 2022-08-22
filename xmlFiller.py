import dictionary

def createXml(layer) -> str:
    res = ''
    for elem in dictionary.xmlDict:
        if elem == 'layer':
            elem = layer
        res += elem
    return res