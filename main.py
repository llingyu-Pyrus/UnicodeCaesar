string = ""
cleartext = ""
i = 0
for chra in string:
        cleartext += str(chr(ord(chra)-i))
print(cleartext)
