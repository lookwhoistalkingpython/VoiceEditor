::set base="C:\Users\uvm\Projects\VoiceEditor_python\src\CmdEditFilter.py"
::set ours="C:\Users\uvm\Projects\VoiceEditor_python\src\CmdEditFilter.py"
::set theirs="C:\Users\uvm\Projects\VoiceEditor_uvm\src\CmdEditFilter.py"
::
::
::git diff-files -c --base  %base% --ours %ours% --theirs %theirs%


cd C:\Users\uvm\Projects\VoiceEditor\src

git branch

:: Assembly Branch
git checkout python
git checkout -b assembly_branch
git checkout assembly_branch
git branch
git checkout uvm -- *
git add --all
git commit -m "Changes imported from UVM branch."
git status

:: Merge Branch
::git checkout python
::git checkout -b merge_branch
::git checkout merge_branch
::git status




pause
