import os

voiceeditorroot=os.environ["VOICEEDITORROOT"]
outputFileName=os.path.join(voiceeditorroot,"run\import_from_uvm.bat")
outputFilePath=os.path.join(voiceeditorroot,"run")

try:
 outputFileHandle=open(outputFileName,"w")
except:
 print ("Unable to open file for writing: ",outputFileName)
 sys.exit(1)

outputFileHandle.write("cd %s"%outputFilePath)


outputFileHandle.close()
