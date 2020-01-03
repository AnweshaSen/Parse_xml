import xml.dom.minidom

doc = xml.dom.minidom.parse("DocumentName.xml")

lines = doc.getElementsByTagName("character")
Matrix = []

for elements in lines:
    charData = []
    charData.append(elements.getAttribute("x"))
    charData.append(elements.getAttribute("y"))
    charData.append(elements.getAttribute("width"))
    charData.append(elements.getAttribute("height"))
    Matrix.append(charData)
print (Matrix)
