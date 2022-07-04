import re
import MapInfoToSLD
import filter
from pysld.style import StyleSld

with open('input.txt', 'r', encoding='utf-8') as fin:
  with open('Errors.txt', 'w', encoding='utf-8') as  ferr:
    i = 0
    for string in fin:
      i += 1
      clstring = MapInfoToSLD.splitLine(string)
      iscor = filter.isCorrect(i, clstring)
      if iscor[0]:
        MapInfoToSLD.convertLine(clstring)
      else:
        ferr.write(iscor[1])
        continue


print('Convertation complete')