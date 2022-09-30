# print(rres)


# print(round( (cm + cb)/ 2))
#
# rm = round(cm / 65535)
# print("rm = " + str(rm))
# gm = round((cm % 65535) / 255)
# print("gm = " + str(gm))
# bm = round(cm % 255)
# print("bm = " + str(bm))
# print(rm * 65535 + gm * 255 + bm)
# print(re.sub('0x', '', '#' + str(hex(rm * 65535 + gm * 255 + bm))))
# print("================")
#
# rb = round(cb / 65535)
# print("rb = " + str(rb))
# gb = round((cb % 65535) / 255)
# print("gb = " + str(gb))
# bb = round(cb % 255)
# print("bb = " + str(bb))
# print(re.sub('0x', '', '#' + str(hex(rb * 65535 + gb * 255 + bb))))
# print("================")
#
# rres = round((rm + rb) / 2)
# print("rres = " + str(rres))
# gres = round((gm + gb) / 2)
# print("bres = " + str(gres))
# bres = round((bm + bb) / 2)
# print("gres = " + str(bres))
# print("================")
#
# print(rres * 65535 + gres * 255 + bres)
# cres = re.sub('0x', '', '#' + str(hex(rres * 65535 + gres * 255 + bres)))
# print(cres)
import extractor

a = '<MI_STYLE>Pen (1,1,0) Brush(18,8388608,16777215)</MI_STYLE>'
style = extractor.extractStyle(a)
arr = style.split(',')
print(arr)
if 'Brush' in arr:
    print(1)
else:
    print(2)