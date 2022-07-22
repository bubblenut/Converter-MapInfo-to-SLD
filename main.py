import MapInfoToSLD
import dictionary
import logger

name = "m_200"

input = name + "_input.txt"
keys = name + "_keys.txt"
errors = name + "_errors.txt"
style = name + "_Style.txt"

with open(input, 'r', encoding='utf-8') as fin:
    with open(keys, 'r', encoding='utf-8') as fkey:
        with open(errors, 'w', encoding='utf-8') as ferr:
            with open(style, 'w', encoding='utf-8') as fout:

                fout.write(dictionary.styleHeading + '\n')
                i = 0
                for string in fin:
                    i += 1
                    print(i)
                    key = fkey.readline().strip('\n')
                    clearline = MapInfoToSLD.splitLine(string)
                    iscor = logger.isCorrect(i, string.strip('\(|\)|\,'))
                    if iscor[0]:
                        fout.write(MapInfoToSLD.convertLine(clearline, key))
                    else:
                        ferr.write(iscor[1])
                    continue

                fout.write(dictionary.styleFooting + '\n')

print('Convertation complete')
