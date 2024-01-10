import re
import os

id_len = 36

manual = 'href="https://play.cyberstart.com/field-manual/'

for fileName in os.listdir("Field Manual_raw/"):
#with open("Field Manual_raw/field-manual.html", "r+") as file:
    if ".html" not in  fileName:
        continue

    with open("Field Manual_raw/" + fileName, "r") as file:
        text = file.read()
    text = re.sub('\?linkType=.*\>', '">', text)


    currIndex = 0
    startIndex = 0
    while currIndex >= 0:
        currIndex = text.find(manual, startIndex)
        print(text[currIndex + len(manual) : currIndex + len(manual) + id_len] + ".html")
        text = text[:currIndex + 6] + text[currIndex + len(manual) : currIndex + len(manual) + id_len] + ".html" + text[currIndex + len(manual) + id_len :]
        startIndex = currIndex + len(manual) + id_len

    text = text.replace(manual, 'href="')
    #file.write(text)
    with open("Field Manual/" + fileName, "w") as newFile:
        newFile.write(text)