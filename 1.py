import string
letters = string.letters[:26]
table = string.maketrans(letters, letters[2:] + letters[:2])

message = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

# print string.translate(message, table)
print string.translate("map", table) + ".html"