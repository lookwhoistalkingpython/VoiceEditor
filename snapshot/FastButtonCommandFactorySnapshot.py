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


from FastButtonTemplatesSnapshot import FastButtonTemplatesSnapshot
from FastButtonListVariablesSnapshot import FastButtonListVariablesSnapshot
from FastButtonMarkersSnapshot import FastButtonMarkersSnapshot

class FastButtonCommandFactorySnapshot(object):



 def __init__(self,voiceEditor):

  self.voiceEditor=voiceEditor



 def get_command_object(self,fastCommandString):

  if (fastCommandString=="fast button list variables"):
   return FastButtonListVariablesSnapshot(self.voiceEditor)
  elif (fastCommandString=="fast button list templates"):
   return FastButtonTemplatesSnapshot(self.voiceEditor)
  elif (fastCommandString=="fast button list markers"):
   return FastButtonMarkersSnapshot(self.voiceEditor)
  else:
   self.voiceEditor.statusBox.Text="Unknown fast button: %s"%fastCommandString
   return None
