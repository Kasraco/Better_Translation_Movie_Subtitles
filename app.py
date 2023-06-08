import re
import os
from translate import Translator
from itertools import groupby
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
   ''' this is a main page of the Better translate videos subtitle
   '''

   convertedText=readfile()
   translatefile(convertedText)
   return 'Hello World mostafa'

def readfile():
   #translator= Translator(to_lang="Persian")    
    texts=""
    # read file line by line
    filepath=os.path.join(os.path.dirname(__file__), "subfile.srt")
    print(filepath)
    file = open(filepath, "r")
    lines=file.readlines()
    
    texts=''.join(lines)    

    file.close()
    linepoins=texts.split(".")
    alltext=''
    for lineNum in range(0,len(linepoins)-1):
         thisline=linepoins[lineNum]+'\n\n'    
         matches=re.findall(r"([0-9]+)\n([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}) --> ([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3})\n(.*?)\n",thisline)
       
         number1=0
         datetime1=''
         datetime2=''
         grouptext=''
         number1=matches[0][0]
         datetime1=matches[0][1] 
         for matchNum in enumerate(matches, start=1):
               datetime2=matchNum[1][2]
               grouptext+=matchNum[1][3]

        # grouptxtTranslate = translator.translate(grouptext)
         alltext+=("{num1}\n{d1} --> {d2}\n{txt}.\n\n".format(num1=number1,d1=datetime1,d2=datetime2,txt=grouptext))
    return(alltext)

def writefile(txt):
    filepath=os.path.join(os.path.dirname(__file__), "DestinationSubFile.srt")
    f = open(filepath, "w")
    f.write(txt)
    f.close()

def translatefile(txt):
    filepath=os.path.join(os.path.dirname(__file__), "DestinationSubFile.fa.srt")
    f = open(filepath, "w")
    f.write(txt)
    f.close()

if __name__=="__main__":
    app.run("0.0.0.0",5000)