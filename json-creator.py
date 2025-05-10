import os

folderPath = './assets/'
extensions = ('.jpg', '.jpeg', '.png', '.webp')
images = os.listdir(folderPath)

with open("assets.json", "w") as f:
    f.write("[\n")
    for i, filename in enumerate(images):
        if filename.lower().endswith(extensions):
            f.write('  "')
            f.write(folderPath)
            f.write(filename)
            f.write('"')
            if i < len(images) - 1:
                f.write(",")
            f.write("\n")
    f.write("]")