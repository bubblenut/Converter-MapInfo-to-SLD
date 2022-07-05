import re
import MapInfoToSLD
import dictionary
import filter
from pysld.style import StyleSld

with open('input.txt', 'r', encoding='utf-8') as fin:
  with open('keys.txt', 'r', encoding='utf-8') as fkey:
    with open('Errors.txt', 'w', encoding='utf-8') as  ferr:
      with open('Style.txt', 'w', encoding='utf-8') as fout:

        fout.write(dictionary.styleHeading + '\n')
        i = 0
        for string in fin:
            i += 1
            key = fkey.readline().strip('\n')
            clearline = MapInfoToSLD.splitLine(string)
            iscor = filter.isCorrect(i, clearline)
            if iscor[0]:
            #вот тут меняется ядро записи, внимательно проверить перед комитом
              fout.write(MapInfoToSLD.convertLine(clearline, key))
            else:
              ferr.write(iscor[1])
            continue

        fout.write(dictionary.styleFooting + '\n')

print('Convertation complete')