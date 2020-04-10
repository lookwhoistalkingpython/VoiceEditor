#
#Copyright 2020 Carsten Thiele
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
#associated documentation files (the "Software"), to deal in the Software without restriction, including
#without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject
#to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial
#portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
#LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import sys
import os
import re

from CmdDosListDirectoryBaseSnapshot import CmdDosListDirectoryBaseSnapshot
from CmdEditSnapshot import CmdEditSnapshot
from CmdDosCreateNewFileSnapshot import CmdDosCreateNewFileSnapshot
from CmdDosCreateNewDirectorySnapshot import CmdDosCreateNewDirectorySnapshot
#from CmdDosCopyMoveDeletePasteFileSnapshot import CmdDosCopyMoveDeletePasteFileSnapshot
import VoiceEditorSettingsSnapshot
from CmdDosRecentFilesSnapshot import CmdDosRecentFilesSnapshot
from CmdDosRecentDirectoriesSnapshot import CmdDosRecentDirectoriesSnapshot
from CmdDosFavouriteFilesSnapshot import CmdDosFavouriteFilesSnapshot
from CmdDosFavouriteDirectoriesSnapshot import CmdDosFavouriteDirectoriesSnapshot



class CmdDosListDirectorySnapshot(CmdDosListDirectoryBaseSnapshot) :

 recentFilesList=[]
 recentDirectoriesList=[]
 previousFile=""



 def __init__(self,voiceEditor,cmdBox,editBox,scaleBox,viewBox,statusBox):
  CmdDosListDirectoryBaseSnapshot.__init__(self,voiceEditor,cmdBox,editBox,scaleBox,viewBox,statusBox)
  self.fileList = ""
  self.commandState = "idle"
  self.allTheBoxes=(
      self.cmdBox,
          self.editBox,
              self.scaleBox,
                  self.viewBox,
                      self.statusBox)
#  self.cmdDosCopyMoveDeletePasteFile=\
#      CmdDosCopyMoveDeletePasteFileSnapshot(self,self.files,self.cmdBox,self.editBox,self.viewBox,self.statusBox)
  self.cmdDosRecentFiles=CmdDosRecentFilesSnapshot(self,self.recentFilesList,self.allTheBoxes)
  self.cmdDosRecentDirectories=CmdDosRecentDirectoriesSnapshot(self,self.recentDirectoriesList,self.allTheBoxes)
  self.cmdDosFavouriteFiles=CmdDosFavouriteFilesSnapshot(self,self.statusBox)
  self.cmdDosFavouriteDirectories=CmdDosFavouriteDirectoriesSnapshot(self,self.statusBox)
#  self.cmdEdit=CmdEditSnapshot(self,self.cmdBox,self.editBox,self.scaleBox,self.viewBox,self.statusBox)



 def processThisCommand(self,command):
  self.statusBox.Text="OK"
  self.nextCommand=self
  if (self.commandState=="wait for selection" and command.isdigit()) :
   self.select_file_directory_or_operation(command)
  elif (self.commandState=="wait for selection" and command=="switch to previous file") :
   previousFile=self.get_previous_file()
   if (previousFile!=""):
    self.nextCommand=self.edit_file(self.previousFile)
  elif (self.commandState=="wait for selection" and command=="list favourite files") :
   self.commandState="idle"
   self.nextCommand=self.cmdDosFavouriteFiles()
  elif (self.commandState=="wait for selection" and command=="list favourite directories") :
   self.commandState="idle"
   self.nextCommand=self.cmdDosFavouriteDirectories()
  elif (self.commandState=="wait for selection" and command=="list recent files") :
   self.commandState="idle"
   self.nextCommand=self.cmdDosRecentFiles()
  elif (self.commandState=="wait for selection" and command=="list recent directories") :
   self.commandState="idle"
   self.nextCommand=self.cmdDosRecentDirectories()
  elif (self.commandState=="idle") :
   self.list_directory()
   self.commandState = "wait for selection"
  return self.nextCommand

 def select_file_directory_or_operation(self,command):
  index=int(command)
  if(index>len(self.fileList)-1):
   self.statusBox.Text="Choice not available. Max choice index is : %d" % (len(self.fileList)-1)
   return
  desiredPath = ""
  currentPath= os.getcwd()
  if(currentPath not in self.recentDirectoriesList):
   self.recentDirectoriesList.append(currentPath)
  choiceTag=self.fileList[index][2]
  #choiceType=self.fileList[index][0]
  if(self.fileList[index][2]==".."):
   desiredPath = os.path.join(self.path, "..")
  elif(self.fileList[index][2]=="create new file"):
   self.viewBox.Text="please  enter file name in command box"
   self.create_new_file()
  elif(self.fileList[index][2]=="create new directory"):
   self.viewBox.Text="please  enter directory name in command box"
   self.create_new_directory()
#  elif(re.match(r'(duplicate|move|delete|insert) file',choiceTag)):
#   self.commandState="idle"
#   self.nextCommand = self.cmdDosCopyMoveDeletePasteFile(choiceTag)
  elif(self.fileList[index][0]==1):
   desiredPath = os.path.join(self.path,self.fileList[index][2])
  elif(self.fileList[index][0]==0):
   fullName = os.path.join(self.path,self.fileList[index][2])
   self.nextCommand=self.edit_file(fullName)
   return self.nextCommand
  if(desiredPath!=""):
   try:
    os.listdir(desiredPath)
    self.statusBox.Text="OK"
   except OSError :
    self.statusBox.Text=""
    self.statusBox.AppendText("Unable to enter directory %s" % desiredPath)
    desiredPath=currentPath
   os.chdir(desiredPath)
   self.list_directory()
   return self.nextCommand

 def edit_file(self,fullName):
  if(fullName not in self.recentFilesList):
   self.recentFilesList.append(fullName)
  self.commandState="idle"
  cmdEdit=CmdEditSnapshot(self.voiceEditor,self,self.cmdBox,self.editBox,self.scaleBox,self.viewBox,self.statusBox)
  cmdEdit.processThisCommand(fullName)
  return cmdEdit

 def create_new_file(self):
  self.commandState="idle"
  cmdDosCreateNewFile=CmdDosCreateNewFileSnapshot(self.cmdBox,self.editBox,self.viewBox,self.statusBox)
  cmdDosCreateNewFile.listDirectory=self
  self.nextCommand=cmdDosCreateNewFile
  return self.nextCommand

 def create_new_directory(self):
  self.commandState="idle"
  cmdDosCreateNewDirectory=CmdDosCreateNewDirectorySnapshot(self.cmdBox,self.editBox,self.viewBox,self.statusBox)
  cmdDosCreateNewDirectory.listDirectory=self
  self.nextCommand=cmdDosCreateNewDirectory
  return self.nextCommand



 def create_cmd_edit_object(self):
  cmdEdit=CmdEditSnapshot(self.voiceEditor,self,self.cmdBox,self.editBox,self.scaleBox,self.viewBox,self.statusBox)
  return cmdEdit



 def create_recent_files_object(self):
  cmdDosRecentFiles=CmdDosRecentFilesSnapshot(self,self.recentFilesList,self.allTheBoxes)
  return cmdDosRecentFiles



 def create_recent_directories_object(self):
  cmdDosRecentDirectories=CmdDosRecentDirectoriesSnapshot(self,self.recentDirectoriesList,self.allTheBoxes)
  return cmdDosRecentDirectories



 def create_favourite_files_object(self):
  cmdDosFavouriteFiles=CmdDosFavouriteFilesSnapshot(self,self.statusBox)
  return cmdDosFavouriteFiles



 def create_favourite_directories_object(self):
  cmdDosFavouriteDirectories=CmdDosFavouriteDirectoriesSnapshot(self,self.statusBox)
  return cmdDosFavouriteDirectories



 def get_previous_file(self):
   return CmdDosListDirectorySnapshot.previousFile

 def set_previous_file(self,fullFileName):
  CmdDosListDirectorySnapshot.previousFile=fullFileName
