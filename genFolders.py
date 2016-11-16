#!/usr/bin/python

# TODO: Add .viewer_link

import sys,os,os.path
import configparser

# print(sys.argv)
genDir = sys.argv[1]
config = configparser.ConfigParser()

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

htmlFile = open(genDir+'.html', 'w')
cssFile = open(genDir+'.css', 'w')
print("######")
print(genDir+'.html created')
print(genDir+'.css created')
htmlFile.write('<div id="'+genDir.split("_")[1].lower()+'_viewer" class="viewer">'+"\n")

############## Main Parsing Loop #############

for currentFolder in dirList:
    print("###")
    print("Parsing",currentFolder,"...")
    # fileList = os.listdir(genDir+"\\"+currentFolder)
    config.read(genDir+"/"+currentFolder+"/config.ini")

    # HTML
    htmlFile.write('<div id="'+currentFolder.split("_")[1]+'_viewer" class="viewer_element">'+"\n")
    htmlFile.write('<a href="#">'+currentFolder.split("_")[1]+'</a>')
    htmlFile.write('<p>['+config["infos"]["tags"]+']</p>'+"\n")
    if config["infos"]["linkname"] != "#": htmlFile.write('<aside>[Galerie :<a target="_blank" href="'+config["infos"]["linkurl"]+'">'+config["infos"]["linkname"]+'</a> ]</aside>')
    htmlFile.write('</div>'+"\n")
    print("HTML parsed")
    # CSS
    cssFile.write('#'+currentFolder.split("_")[1]+'_viewer {'+"\n")
    cssFile.write('background-image: url("'+genDir+'/'+currentFolder+'/01.jpg");'+"\n")
    cssFile.write('}'+"\n")
    print("CSS parsed")

htmlFile.write('</div>'+"\n")
htmlFile.close()
cssFile.close()
