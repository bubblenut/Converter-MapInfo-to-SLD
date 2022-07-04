import re
from pysld.style import StyleSld
import dictionary

def splitLine(line):
    if 'Pen' in line and 'Brush' in line:
        res = re.split("\)\s", re.sub(',|\(|\n', '', line))
    else:
        res = re.sub(',|\(|\)\n', '', line)
    return res


def convertBrush(line):
  filename = (" ".join(map(str,line))).replace(")", "")

  if len(line) == 2:
    penattr = line[0].split()
    p1 = penattr[1]
    p2 = penattr[2]
    p3 = penattr[3]

    brushattr = line[1].split()
    b1 = brushattr[1]
    b2 = brushattr[2]
    b3 = brushattr[3].replace(")", "")

  with open (filename, 'w+') as outp:
    simple_sld = StyleSld(style_name=filename,
                          geom_type='polygon',
                          fill_color=re.sub('0x', '', '#'+str(hex(int(b3)))),
                          stroke_color=re.sub('0x', '', '#'+str(hex(int(p3)))),
                          stroke_width=p1)
    simple_sld_style = simple_sld.generate_simple_style()
    outp.write(simple_sld_style)


def convertPen(line):
   filename = (" ".join(map(str, line))).replace(")", "")

   penattr = line.split()
   p1 = penattr[1]
   p2 = int(penattr[2])
   p3 = int(penattr[3].replace(")", ""))

   #Проверка на dasharray
   dasharrayattr = None
   if p2 >= 3 and p2 <= 14:
       dasharrayattr = dictionary.penDict.get(p2)


   with open(filename + '.sld', 'w+') as outp:
     simple_sld = StyleSld(style_name=filename,
                           geom_type='line',
                           stroke_color=re.sub('0x', '', '#'+str(hex(int(p3)))),
                           stroke_width=p1,
                           stroke_dasharray=dasharrayattr
                           )
     simple_sld_style = simple_sld.generate_simple_style()
     outp.write(simple_sld_style)


def convertLine(line):
  if (len(line) == 2 and (('Brush' in line[0]) or ('Brush' in line[1]))) :
    convertBrush(line)
  else:
    convertPen(line)