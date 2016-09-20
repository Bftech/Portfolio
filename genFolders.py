#!/usr/bin/python

import sys,os

# print(sys.argv)
genDir = sys.argv[1]

############# Files exploration ###########

if not os.path.exists(genDir):
    print(genDir, "don't exists")
    sys.exit(-1)
print("Generating HTML for", genDir)

dirList = os.listdir(genDir)
if not dirList:
    print(genDir,"is empty")
    sys.exit(-1)
print("Found",len(dirList), "dirs :",dirList)

############## HTML output init #######

genFile = open(genDir+'.html', 'w')
print("######")
print(genDir+'.html created')
genFile.write('<div id="'+genDir.split("_")[1].lower()+'_viewer" class="viewer hidden">'+"\n")

############## Main Parsing Loop #############

for currentFolder in dirList:
    print("###")
    print("Parsing",currentFolder,"...")
    fileList = os.listdir(genDir+"\\"+currentFolder)
    print("Found",len(fileList), "files :",fileList)
    for f in fileList:
        # ext = os.path.splitext(f)[1]
        if (f == "01.jpg") or (f == "01.png"):
            genFile.write('<div class="viewer_element">'+"\n")
            genFile.write('<img src="'+genDir+'/'+currentFolder+'/'+f+'"/>'+"\n")
            genFile.write('<br>'+"\n")
            genFile.write('<a href="#">'+currentFolder.split("_")[1]+'</a>'+"\n")
            genFile.write('</div>'+"\n")

genFile.write('</div>'+"\n")

genFile.close()
