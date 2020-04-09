::set base="C:\Users\uvm\Projects\VoiceEditor_python\src\CmdEditFilter.py"
::set ours="C:\Users\uvm\Projects\VoiceEditor_python\src\CmdEditFilter.py"
::set theirs="C:\Users\uvm\Projects\VoiceEditor_uvm\src\CmdEditFilter.py"
::
::
::git diff-files -c --base  %base% --ours %ours% --theirs %theirs%


cd C:\Users\uvm\Projects\VoiceEditor_python\src

git branch

git checkout python
git checkout -b assembly_branch
git checkout uvm -- src\*


pause
