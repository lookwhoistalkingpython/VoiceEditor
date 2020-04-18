os.chdir([directory path])
for file in glob.glob(r'*'):
 shellCommand=r'[command] %s'% [file]
 shellOutput=subprocess.check_output(shellCommand,shell=True)
