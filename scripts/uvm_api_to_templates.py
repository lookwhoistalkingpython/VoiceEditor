import os
import re

taskList=[]
functionList=[]
previousPath=""
previousFile=""
level1Index=0
level2Index=0
templateIndex=0

searchRoot=r"C:\Users\uvm\Projects\UVM"

outputFileName=r'..\templates\06_uvm_api.template'
try:
 outputFileHandle=open(outputFileName,"w")
except:
 print ("Unable to open file for writing: ",outputFileName)
 sys.exit(1)



def process_line(fullFileName,lineNumber,line):

 m=re.search(r'\btask\b\s+(\S+)',line)
 if(m):
  taskList.append(m.group(1))

 m=re.search(r'\bfunction\b\s+\S+\s*(\S+)',line)
 if(m):
  functionList.append(m.group(1))



def output_to_template_file(path,file,level1Index,level2Index):

 directory =os.path.basename(path)

 level1Name=directory
 level2Name=file

 outputFileHandle.write("-template_context 06_uvm_api.%02d_%s.%02d_%s.%03d"%\
 (level1Index,level1Name,level2Index,level2Name,templateIndex))
 outputFileHandle.write("-template_name %s"%templateName)
 outputFileHandle.write("-template_start")
 outputFileHandle.write("-template_end")




for path,directories,files in os.walk(searchRoot):

 for file in files:

  if ( not file.endswith((".svh"))):
   continue

  if (path!=previousPath ):
   level1Index=0
  if (path!=previousFile):
   level2Index=0

  previousPath=path
  previousFile=file

  fullFileName=os.path.join(path,file)

  try:
   fileHandle=open(fullFileName,"r")
  except:
   print ("Unable to open file: ", fullFileName)
   sys.exit(1)
  else:
   fileList=fileHandle.readlines()
   fileHandle.close()
  lineNumber=0
  filterExpression=r"extern\s+.*\b(function|task)\b"
  for line in fileList :
   line=line.rstrip()
   m=re.search(filterExpression,line)
   if(m):
    process_line(fullFileName,lineNumber,line)
   lineNumber+=1

  output_to_template_file(path,file,level1Index,level2Index)

  level1Index+=1
  level2Index+=1



