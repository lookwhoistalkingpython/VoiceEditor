import re
import sys


def object_macros():
 fileName= "..\scratch\object_macros.txt"
 try:
  fileHandle=open(fileName, "r")
 except:
  print ("Unable to open file: ",fileName)
  sys.exit(1)
 else:
  fileList=fileHandle.readlines()
  fileHandle.close()

 outputFileName=r'..\templates\05_macros.00_object.template'
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



def callback_macros():
 fileName= "..\scratch\callback_macros.txt"
 try:
  fileHandle=open(fileName, "r")
 except:
  print ("Unable to open file: ",fileName)
  sys.exit(1)
 else:
  fileList=fileHandle.readlines()
  fileHandle.close()

 outputFileName=r'..\templates\05_macros.01_callback.template'
 try:
  outputFileHandle=open(outputFileName,"w")
 except:
  print ("Unable to open file for writing: ",outputFileName)
  sys.exit(1)

 index=110
 for line in fileList:
  if(line.isspace()):
   continue
  line=line.rstrip()
  line=re.sub("\(T,",r'([T],',line)
  line=re.sub("CB",r'[CB]',line)
  line=re.sub("METHOD",r'[METHOD]',line)
  line=re.sub("OBJ",r'[OBJ]',line)
  line=re.sub("VAL",r'[VAL]',line)
  line=re.sub("OPER",r'[OPER]',line)
  line=re.sub("ST",r'[ST]',line)
  line=re.sub("`define ",'',line)
  outputFileHandle.write("-template_context 05_macros.01_callback.%0d"%index+"\n")
  outputFileHandle.write("-template_name %s"%line+"\n")
  outputFileHandle.write("-template_start"+"\n")
  outputFileHandle.write("`"+line+"\n")
  outputFileHandle.write("-template_end"+"\n\n")
  index+=1

 outputFileHandle.close()



def compare_macros():
 fileName= "..\scratch\compare_macros.txt"
 try:
  fileHandle=open(fileName, "r")
 except:
  print ("Unable to open file: ",fileName)
  sys.exit(1)
 else:
  fileList=fileHandle.readlines()
  fileHandle.close()

 outputFileName=r'..\templates\05_macros.02_compare.template'
 try:
  outputFileHandle=open(outputFileName,"w")
 except:
  print ("Unable to open file for writing: ",outputFileName)
  sys.exit(1)

 index=110
 for line in fileList:
  if(line.isspace()):
   continue
  line=line.rstrip()
  line=re.sub("COMPARER=comparer",r'[COMPARER=comparer]',line)
  #line=re.sub("COMPARER",r'[COMPARER]',line)
  line=re.sub("LVALUE",r'[LVALUE]',line)
  line=re.sub("RVALUE",r'[RVALUE]',line)
  line=re.sub("NAME",r'[NAME]',line)
  line=re.sub("RADIX",r'[RADIX]',line)
  line=re.sub("POLICY=UVM_DEFAULT_POLICY",r'[POLICY=UVM_DEFAULT_POLICY]',line)

  line=re.sub("`define ",'',line)
  outputFileHandle.write("-template_context 05_macros.02_compare.%0d"%index+"\n")
  outputFileHandle.write("-template_name %s"%line+"\n")
  outputFileHandle.write("-template_start"+"\n")
  outputFileHandle.write("`"+line+"\n")
  outputFileHandle.write("-template_end"+"\n\n")
  index+=1

 outputFileHandle.close()


def copy_macros():
 fileName= "..\scratch\copy_macros.txt"
 try:
  fileHandle=open(fileName, "r")
 except:
  print ("Unable to open file: ",fileName)
  sys.exit(1)
 else:
  fileList=fileHandle.readlines()
  fileHandle.close()

 outputFileName=r'..\templates\05_macros.01_copy.template'
 try:
  outputFileHandle=open(outputFileName,"w")
 except:
  print ("Unable to open file for writing: ",outputFileName)
  sys.exit(1)

 index=110
 for line in fileList:
  if(line.isspace()):
   continue
  line=line.rstrip()
  line=re.sub("LVALUE",r'[LVALUE]',line)
  line=re.sub("RVALUE",r'[RVALUE]',line)
  line=re.sub("NAME",r'[NAME]',line)
  line=re.sub("RADIX",r'[RADIX]',line)
  line=re.sub("COPIER=copier",r'[COPIER=copier]',line)
  line=re.sub("POLICY=UVM_DEFAULT_POLICY",r'[POLICY=UVM_DEFAULT_POLICY]',line)
  line=re.sub("`define ",'',line)
  outputFileHandle.write("-template_context 05_macros.03_copy.%0d"%index+"\n")
  outputFileHandle.write("-template_name %s"%line+"\n")
  outputFileHandle.write("-template_start"+"\n")
  outputFileHandle.write("`"+line+"\n")
  outputFileHandle.write("-template_end"+"\n\n")
  index+=1

 outputFileHandle.close()



def global_macros():
 fileName= "..\scratch\global_macros.txt"
 try:
  fileHandle=open(fileName, "r")
 except:
  print ("Unable to open file: ",fileName)
  sys.exit(1)
 else:
  fileList=fileHandle.readlines()
  fileHandle.close()

 outputFileName=r'..\templates\05_macros.04_global.template'
 try:
  outputFileHandle=open(outputFileName,"w")
 except:
  print ("Unable to open file for writing: ",outputFileName)
  sys.exit(1)

 index=110
 for line in fileList:
  if(line.isspace()):
   continue
  line=line.rstrip()
  outputFileHandle.write("-template_context 05_macros.04_global.%0d"%index+"\n")
  outputFileHandle.write("-template_name %s"%line+"\n")
  outputFileHandle.write("-template_start"+"\n")
  outputFileHandle.write("`"+line+"\n")
  outputFileHandle.write("-template_end"+"\n\n")
  index+=1

 outputFileHandle.close()



def messages_macros():
 fileName= "..\scratch\messages_macros.txt"
 try:
  fileHandle=open(fileName, "r")
 except:
  print ("Unable to open file: ",fileName)
  sys.exit(1)
 else:
  fileList=fileHandle.readlines()
  fileHandle.close()

 outputFileName=r'..\templates\05_macros.04_messages.template'
 try:
  outputFileHandle=open(outputFileName,"w")
 except:
  print ("Unable to open file for writing: ",outputFileName)
  sys.exit(1)

 index=110
 for line in fileList:
  if(line.isspace()):
   continue
  line=line.rstrip()
  line=re.sub("`define ",'',line)
  line=re.sub("RADIX",r'[RADIX]',line)
  line=re.sub("ID",r'[ID]',line)
  line=re.sub("MSG",r'[MSG]',line)
  line=re.sub("VERBOSITY",r'[VERBOSITY]',line)
  line=re.sub("FILE",r'[FILE]',line)
  line=re.sub("SEVERITY",r'[SEVERITY]',line)
  line=re.sub("RM",r'[RM]',line)
  line=re.sub("LINE",r'[LINE]',line)
  line=re.sub("RO",r'[RO]',line)
  line=re.sub("RM = __uvm_msg",r'[RM = __uvm_msg]',line)
  line=re.sub("ACTION=(UVM_LOG|UVM_RM_RECORD)",r'[ACTION=(UVM_LOG|UVM_RM_RECORD)]',line)
  line=re.sub("VALUE",r'[VALUE]',line)
  line=re.sub("LABEL=\"\"",r'[LABEL=""]',line)
  line=re.sub("VAR",r'[VAR]',line)
  #line=re.sub("RADIX",r'[RADIX]',line)
  outputFileHandle.write("-template_context 05_macros.04_messages.%0d"%index+"\n")
  outputFileHandle.write("-template_name %s"%line+"\n")
  outputFileHandle.write("-template_start"+"\n")
  outputFileHandle.write("`"+line+"\n")
  outputFileHandle.write("-template_end"+"\n\n")
  index+=1

 outputFileHandle.close()



def packer_macros():
 fileName= "..\scratch\packer_macros.txt"
 try:
  fileHandle=open(fileName, "r")
 except:
  print ("Unable to open file: ",fileName)
  sys.exit(1)
 else:
  fileList=fileHandle.readlines()
  fileHandle.close()

 outputFileName=r'..\templates\05_macros.05_packer.template'
 try:
  outputFileHandle=open(outputFileName,"w")
 except:
  print ("Unable to open file for writing: ",outputFileName)
  sys.exit(1)

 index=110
 for line in fileList:
  if(line.isspace()):
   continue
  line=line.rstrip()
  line=re.sub("`define ",'',line)
  line=re.sub("VAR",r'[VAR]',line)
  line=re.sub("SIZE",r'[SIZE]',line)
  line=re.sub("TYPE",r'[TYPE]',line)
  outputFileHandle.write("-template_context 05_macros.05_packer.%0d"%index+"\n")
  outputFileHandle.write("-template_name %s"%line+"\n")
  outputFileHandle.write("-template_start"+"\n")
  outputFileHandle.write("`"+line+"\n")
  outputFileHandle.write("-template_end"+"\n\n")
  index+=1

 outputFileHandle.close()


#object_macros()
#callback_macros()
#compare_macros()
#copy_macros()
#global_macros()
#messages_macros()
packer_macros()
