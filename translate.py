
import os
from translate import Translator
from html.parser import HTMLParser
import re

translator= Translator(to_lang="hi")

def translate(lng):
    translation = translator.translate(lng)
    return ""+translation+""


site = r"path of file that you want to translate"

def trns(direc):
    files = os.listdir(direc)
    filesToTranslate = []
    for file in files:
        if file.endswith(".html"):
            filesToTranslate.append( direc+"\/" +file)
        elif os.path.isdir(os.path.join(direc, file)):
            direc2 = direc+"\/" +file
            filesToTranslate += trns(direc2)
    return filesToTranslate   

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.prev = ""
        self.result = ""
    def handle_starttag(self, tag, attrs):
        self.prev = tag
        atribu = ""
        for i in attrs:
            atribu += ""+i[0]+"='"+str(i[1])+"' " # "class=ASD"
        self.result += " <" + tag + " " + atribu + "> "

    def handle_endtag(self, tag):
        self.prev = ""
        self.result += " </" + tag + "> " + "\n"

    def handle_data(self, data):
        data2 = re.sub(r'\n', '', data,flags=re.MULTILINE)
        data3 = data2.replace(" ","").strip()
        if self.prev in ("style","script","link","a"):
            self.result += data 
        elif data == None:
            self.result += ""
        elif len(data3) == 0:
            self.result += ""
        else:
            print(data)  
            trad = translate(data)
        
            self.result += trad

def TranslateToHindi(direc):
    directories = trns(direc)
    parser = MyHTMLParser() 
    tempDirectories = [directories[0]]
    for i in tempDirectories:
        print(i)
        fil = open(i,"r", encoding="utf-8")
        file = fil.read()
        parser.feed(file)
        fil.close()
        fileouts = open(i,"w", encoding="utf-8")  
        fileouts.write(parser.result)       
        fileouts.close()


print(TranslateToHindi(site))