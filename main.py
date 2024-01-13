string = str(input("输入密文："))
cleartext = ""
i = int(input("输入位移大小："))
for chra in string:
        cleartext += str(chr(ord(chra)-i))
print(cleartext)
