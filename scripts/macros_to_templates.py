import re

fileName= "..\scratch\object_macros.txt"
try:
 fileHandle=open(fileName, "r")
except:
 print ("Unable to open file: ",fileName)
 sys.exit(1)
else:
 fileList=fileHandle.readlines()
 fileHandle.close()

outputFileName=r'..\templates\05_macros.01_object.template'
try:
 outputFileHandle=open(outputFileName,"w")
except:
 print ("Unable to open file for writing: ",outputFileName)
 sys.exit(1)

index=110
for line in fileList:
 line=line.rstrip()
 line=re.sub("T",r'[T]',line)
 line=re.sub("ARG",r'[ARG]',line)
 line=re.sub("FLAG",r'[FLAG]',line)
 line=re.sub("`define ",'',line)
 outputFileHandle.write("-template_context 05_macros.01_object.%0d"%index+"\n")
 outputFileHandle.write("-template_name %s"%line+"\n")
 outputFileHandle.write("-template_start"+"\n")
 outputFileHandle.write("`"+line+"\n")
 outputFileHandle.write("-template_end"+"\n\n")
 index+=1

outputFileHandle.close()

