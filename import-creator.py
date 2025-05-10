import os

extensions = ('.avif', '.jpg', '.jpeg', '.png', '.webp')

def generateImportStatements (folderPath, fObj, startIndex, arrayName):
    images = os.listdir(folderPath)
    num = startIndex
    for i, imageName in enumerate(images):
        if imageName.lower().endswith(extensions):
            fObj.write("import img")
            fObj.write(str(num))
            fObj.write(" from ")
            fObj.write(imageName)
            fObj.write(";\n")
            num = num + 1
    fObj.write(f"const {arrayName} = [")
    for i in range (startIndex, num):
        fObj.write(f"img{str(i)}")
        if (i < num - 1):
            fObj.write(", ")
    fObj.write("];\n\n")
    return num

with open("import-statements.js", "w") as f:
    nextStart = generateImportStatements('./assets/folder1', f, 0, "folder1")
    nextStart = generateImportStatements('./assets/folder2', f, nextStart, "folder2")