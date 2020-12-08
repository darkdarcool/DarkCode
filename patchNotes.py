import os
w = "\033[0;37m"
print(w + 'Version 1.0.0\nLAUNCH\n\n\nVersion 1.0.1\nAdded error prompts')
sun = input(w + 'Hit enter to leave\n')
if sun == '':
  os.system('clear')
  os.system('python3 main.py')
else:
  os.system('clear')
  os.system('python3 main.py')