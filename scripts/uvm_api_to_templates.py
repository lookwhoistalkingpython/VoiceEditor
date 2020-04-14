import os
import re

methodList=[]
level1Index=0
level2Index=0

searchRoot=r"C:\Users\uvm\Projects\UVM"


def process_line(path,file,level1Index,level2Index,line):

 directory =os.path.basename(path)

 m=re.search(r'\btask\b\s+(.*)',line)
 if(m):
  methodList.append(["task",directory,file,level1Index,level2Index,m.group(1),line])

 m=re.search(r'\bfunction\b\s+\S+\s*(.*)',line)
 if(m):
  methodList.append(["function",directory,file,level1Index,level2Index,m.group(1),line])



def output_to_template_file():

 templateIndex=0

 outputFileName=r'..\templates\06_uvm_api.template'
 try:
  outputFileHandle=open(outputFileName,"w")
 except:
  print ("Unable to open file for writing: ",outputFileName)
  sys.exit(1)

 for taskType,directory,file,level1Index,level2Index,templateName,line in sorted(methodList):

  level1Name=directory
  level2Name=file.replace(".svh","")

  outputFileHandle.write("-template_context 06_uvm_api.%02d_%s.%02d_%s.%s.%03d"%\
  (level1Index,level1Name,level2Index,level2Name,taskType,templateIndex)+"\n")
  #outputFileHandle.write("-template_name %s %s"%(taskType,templateName)+"\n")
  outputFileHandle.write("-template_name %s"%(templateName)+"\n")
  outputFileHandle.write("-template_start"+"\n")
  #outputFileHandle.write(taskType+" "+templateName+"\n")
  outputFileHandle.write(line+"\n")
  outputFileHandle.write("-template_end"+"\n")

  templateIndex+=1




for path,directories,files in os.walk(searchRoot):

 for file in files:

  if ( not file.endswith((".svh"))):
   continue

  fullFileName=os.path.join(path,file)

  try:
   fileHandle=open(fullFileName,"r")
  except:
   print ("Unable to open file: ", fullFileName)
   sys.exit(1)
  else:
   fileList=fileHandle.readlines()
   fileHandle.close()
  filterExpressionComment=r'^\s*//'
  filterExpression=r"\b(function|task)\s*(\w+\s+)?(\w+)\s*\(.*\)\s*;"
  filterExpressionEndClass=r'^\s*endclass\b'
  for line in fileList :
   line=line.rstrip()
   matchComment=re.search(filterExpressionComment,line)
   if (matchComment):
    continue
   matchEndClass=re.search(filterExpressionEndClass,line)
   if (matchEndClass):
    break
   m=re.search(filterExpression,line)
   if(m):
    process_line(path,file,level1Index,level2Index,line)


  level2Index+=1

 level1Index+=1

output_to_template_file()




