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


import re
from FastButtonMarkersSnapshot import FastButtonMarkersSnapshot

class CmdEditDuplicateYankInsertLinesSnapshot(object):

 def __init__(self,parent,cmdBox,editBox,viewBox,statusBox):
  self.fileToEditList=parent.fileToEditList
  self.cmdBox=cmdBox
  self.editBox=editBox
  self.viewBox=viewBox
  self.statusBox=statusBox
  self.lineOperationBuffer=parent.lineOperationBuffer
  self.operation = ""
  self.rangeStart=0
  self.rangeEnd=0
  self.parent=parent

 def __call__(self,command,currentEditLine):

  self.currentEditLine=currentEditLine

  matchCurrentLine=\
      re.match(
          r'(duplicate|yank)\s+lines\s*\[start line\]\s*:\s*\[end line\]',
              command)
  if(matchCurrentLine):
   self.operation=matchCurrentLine.group(1)
   self.rangeStart=currentEditLine
   self.rangeEnd=currentEditLine

  matchSingleLine=\
      re.match(
          r'(duplicate|yank)\s+lines\s*(\d+)\s*:\s*\[end line\]',
              command)
  if(matchSingleLine):
   self.operation=matchSingleLine.group(1)
   self.rangeStart=int(matchSingleLine.group(2))
   self.rangeEnd=self.rangeStart

  matchLineRange=\
      re.match(
          r'(duplicate|yank)\s+lines\s*(\d+)\s*:\s*(\d+)',
               command)
  if(matchLineRange):
   self.operation=matchLineRange.group(1)
   self.rangeStart=int(matchLineRange.group(2))
   self.rangeEnd=int(matchLineRange.group(3))

  matchInsertLines=re.match(r'(insert)\s+lines\s*(\d+)', command)
  if(matchInsertLines):
   self.operation=matchInsertLines.group(1)
   self.rangeStart=int(matchInsertLines.group(2))

  if(self.rangeStart < 0):
   self.rangeStart=0

  if(self.rangeEnd >=len(self.fileToEditList)-1):
   self.rangeEnd=len(self.fileToEditList)-1

  if(self.operation not in ("duplicate", "yank", "insert")):
   self.statusBox.Text="Invalid operation: %s" % self.operation
   return

  if(self.operation=="duplicate"):
   self.duplicate_lines()

  if(self.operation=="yank"):
   self.yank_lines()

  if(self.operation=="insert"):
   self.insert_lines()

 def duplicate_lines(self):
  del self.lineOperationBuffer[:]
  for lineNumber in range(self.rangeStart,self.rangeEnd+1):
   self.lineOperationBuffer.append(self.fileToEditList[lineNumber])

 def yank_lines(self):
  del self.lineOperationBuffer[:]
  for lineNumber in range(self.rangeStart,self.rangeEnd+1):
   self.lineOperationBuffer.append(self.fileToEditList[lineNumber])
  del self.fileToEditList[self.rangeStart:self.rangeEnd+1]
  if (len(self.fileToEditList)==0):
   self.fileToEditList.append("")
   self.parent.currentEditLine=0
  elif (self.currentEditLine>self.rangeEnd):
   self.parent.currentEditLine-=(self.rangeEnd-self.rangeStart+1)
  elif ((self.currentEditLine>=self.rangeStart) and (self.currentEditLine<=self.rangeEnd)):
   if (self.rangeStart>0):
    self.parent.currentEditLine=self.rangeStart-1
   else:
    self.parent.currentEditLine=0


  rangeDelta=self.rangeStart-self.rangeEnd-1
  FastButtonMarkersSnapshot.adjust_markers(self.parent.fullFileName,self.rangeStart,rangeDelta)
  self.parent.voiceEditor.fastButtonAreaHandler.refresh()

 def insert_lines(self):
  lineNumber=self.rangeStart
  for lineToInsert in self.lineOperationBuffer:
   self.fileToEditList.insert(lineNumber,lineToInsert)
   lineNumber=lineNumber+1
  rangeDelta=len(self.lineOperationBuffer)
  FastButtonMarkersSnapshot.adjust_markers(self.parent.fullFileName,self.rangeStart,rangeDelta)
  self.parent.voiceEditor.fastButtonAreaHandler.refresh()

