import os
import re

searchRoot=r"C:\Users\uvm\Projects\UVM"

for path,directories,files in os.walk(searchRoot):
# if(path.endswith("[directory to skip]")):
#  [continue]
 for file in files:
  fullFileName=os.path.join(path,file)
#  if ( not [fullFileName].endswith(([file type to ignore ]))):
#   [continue]
  try:
   fileHandle=open(fullFileName,"r")
  except:
   print ("Unable to open file: ", fullFileName)
   sys.exit(1)
  else:
   fileList=fileHandle.readlines()
   fileHandle.close()
  lineNumber=0
  filterExpression="\b(function|task)\b"
  for line in fileList :
   line=line.rstrip()
   m=re.match(r'%s'%filterExpression,line)
   if(m):
    self.process_line([fullFileName],lineNumber,line.rstrip())
   lineNumber+=1

def process_line(fullFileName,lineNumber,line):
 print ("matched line",line)

