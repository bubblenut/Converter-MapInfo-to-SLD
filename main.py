import MapInfoToSLD
import dictionary
import logger

input = "m_w_input.txt"
keys = "m_w_keys.txt"
errors = "m_w_errors.txt"
style = "m_w_Style.txt"

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
                        # вот тут меняется ядро записи, внимательно проверить перед комитом
                        fout.write(MapInfoToSLD.convertLine(clearline, key))
                    else:
                        ferr.write(iscor[1])
                    continue

                fout.write(dictionary.styleFooting + '\n')

print('Convertation complete')
