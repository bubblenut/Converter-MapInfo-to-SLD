import re
cm = 10157824
cb = 16777215

cmhex = re.sub("0x", "", str(hex(cm))).zfill(6)
print("#" + cmhex)
cbhex = re.sub("0x", "", str(hex(cb))).zfill(6)
print("#" + cbhex)

print("========================")

rres = hex(round(( int(cmhex[:2],16) + int(cbhex[:2],16) ) / 2))
gres = hex(round(( int(cmhex[2:-2],16) + int(cbhex[2:-2],16) ) / 2))
bres = hex(round(( int(cmhex[-2:],16) + int(cbhex[-2:],16) ) / 2))

rres = re.sub("0x", "", rres)
gres = re.sub("0x", "", gres)
bres = re.sub("0x", "", bres)

print("#" + rres + gres + bres)
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