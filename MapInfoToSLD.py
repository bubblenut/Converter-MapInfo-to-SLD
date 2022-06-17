import re
#import pysld

def translateName(): #Перевод определения стиля (Pen, Brush)
    pass

def translateParameter(): #Перевод параметров стиля(цвет, заливка, символ)
    pass

def tokenizeParameter(): #Токенизация параметров, чтобы переводить каждый отдельно
    pass

def translateString(): #Перевод строки, который будет содержать предыдущие функции
    pass

def tokenizeFile(fin, fout):            #Токенизация файла по строкам, чтобы переводить строки
    with open(fin, 'r') as inp:
        with open(fout, 'w') as outp:
            for line in inp:
                buf = re.split("\s\(|\)\s",line.replace(",",""))
                buf.pop()
                print(buf)

def translateFile():
    pass




