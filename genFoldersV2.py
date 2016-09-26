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
genCss = open(genDir+'.css', 'w')
print("######")
print(genDir+'.html created')
print(genDir+'.css created')
genFile.write('<div id="'+genDir.split("_")[1].lower()+'_viewer" class="viewer">'+"\n")

############## Main Parsing Loop #############

for currentFolder in dirList:
    print("###")
    print("Parsing",currentFolder,"...")
    fileList = os.listdir(genDir+"\\"+currentFolder)
    with open(genDir+"/"+currentFolder+"/tags.txt",'r') as fileTags:
        tags = fileTags.read().splitlines()
    print("Found",len(fileList), "files :",fileList)
    for f in fileList:
        # ext = os.path.splitext(f)[1]
        if (f == "01.jpg") or (f == "01.png"):
            # HTML
            genFile.write('<div id="'+currentFolder.split("_")[1]+'_viewer" class="viewer_element">'+"\n")
            genFile.write('<a href="#">'+currentFolder.split("_")[1]+'</a>')
            genFile.write('<p>['+" ; ".join(tags)+']</p>'+"\n")
            genFile.write('</div>'+"\n")
            # CSS
            genCss.write('#'+currentFolder.split("_")[1]+'_viewer {'+"\n")
            genCss.write('background-image: url("'+genDir+'/'+currentFolder+'/'+f+'");'+"\n")
            genCss.write('}'+"\n")

genFile.write('</div>'+"\n")

genFile.close()
