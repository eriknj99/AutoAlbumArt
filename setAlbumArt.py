import csv
import os
import eyed3

scanDir = input("Enter scan directory: ")
key = input("Enter image keys as CSV: ")

keyArray = key.split(',')

def getSubDirs(dirpath):
    dirArray = []
    for (dirpath, dirnames, filenames) in os.walk(dirpath):
        for f in filenames:
           dirArray.append(os.path.join(dirpath, f))

    return dirArray


dirArray = (getSubDirs(scanDir))
foundArt = []


print("Searching for album art...")
for f in dirArray:
    tmp = f[f.rfind('/') + 1:]
  
    if tmp in keyArray:
        foundArt.append(f)
print("done.")
print("Found: " +str(len(foundArt)) + " albums: ")
print(foundArt)
         
for f in dirArray:
    for tmpArt in foundArt:
        if (tmpArt[:tmpArt.rfind('/')] == f[:f.rfind('/')]) and (f not in foundArt):
            if ".mp3" in f:
                print("Embeding " + f + " with image " + tmpArt)
                audiofile = eyed3.load(f)
                if (audiofile.tag == None):
                    audiofile.initTag()
                encodeType = 'image/jpeg'
                if ".png" in tmpArt:
                    encodeType = 'image/png'

                audiofile.tag.images.set(3, open(tmpArt,'rb').read(), 'image/jpeg')
                audiofile.tag.save()
