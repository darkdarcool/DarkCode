import os
red = "\033[0;91m"
w = "\033[0;37m"
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
bold = '\033[1m'
end = '\033[0m'
new_line = ";"
os.system('clear')
varss = ['var1', 'var2', 'var3', 'var4']
swindle = bold + blue + bold + "~/DarkScript? "
ab = ''
#################
#ERROR STAEMENTS#
#################
def errors():
  if ('import') in sun:
    print(bold + red + red + bold +  'Syntax Error in: \n' + end + w + sun + '\n' + green + '   ^~~~~~~~\n' + red + bold + 'Try just "' + white + 'import' + red + bold +  '" next time.\n')
  elif ('a.') in sun:
    print(bold + red + red + bold +  'Module Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'Try importing the module of "' + end + w + 'a' + end + red + bold + '" next time' )
  elif ('%') in sun:
    print(bold + red + red + bold +  'Syntax Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'Try just "' + white + '%%' + red + bold +  '" next time for a comment or note.\n')
  elif ('//') in sun: 
    print(bold + red + red + bold +  'Syntax Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'Try just "' + white + '%%' + red + bold +  '" next time for a comment or note.\n')
  elif ('<!--') in sun: 
    print(bold + red + red + bold +  'Syntax Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'Try just "' + white + '%%' + red + bold +  '" next time for a comment or note.\n')
  elif ('#') in sun:
    print(bold + red + red + bold +  'Syntax Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'Try just "' + white + '%%' + red + bold +  '" next time for a comment or note.\n')
  elif ('console.random') in sun:
    print(bold + red + red + bold + 'Module Error in:\n' + end + w +  sun + green + '\n' +  '   ^~~~~~~~~' + red + bold + ' \nTry importing the module of "console" and "random" next time.\n')
  elif ('console') in sun:
    print(bold + red + red + bold + 'Module Error in:\n' + end + w +  sun + green + '\n' +  '   ^~~~~~~~~' + red + bold + ' \nTry importing the module of "' + end + w + 'console' + red + bold + '" next time.\n')
  elif ('random') in sun:
    print(bold + red + red + bold + 'Module Error in:\n' + end + w +  sun + green + '\n' +  '   ^~~~~~~~~' + red + bold + ' \nTry importing the module of "random" next time.\n')
  elif ('window.cls') in sun:
    print(bold + red + bold + 'Syntax Error in: \n' + end + w + sun + '\n' + green + '   ^~~~~~~~\n' + red + bold + ' Try just " ' + white + 'window.erase()' + red + bold +  ' " next time.\n')
  elif ('window.clear') in sun:
    print(bold + red + bold + 'Syntax Error in: \n' + end + w + sun + '\n' + green + '   ^~~~~~~~\n' + red + bold + ' Try just " ' + white + 'window.erase()' + red + bold +  ' " next time.\n')
  elif ('git') in sun:
    print(bold + red + bold + 'Syntax Error in: \n' + end + w + sun + '\n' + green + ' ^~~~~~~~\n' + red + bold + 'No git commands are availible for this language yet. Try a bash repl next time.\n')
  elif ('$') in sun:
    print(bold + red + bold + 'Command Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'There is no command name called that, try $patch next time\n')
  elif ('@') in sun:
    print(bold + red + 'Module Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'Try importing the module aScript and using "' + end + w + '@@' + red + bold + '". Or use "' + end + w + '%%' + red + bold + '" next time for comments.')
  elif ('@@') in sun:
    print(bold + red + bold + 'Module Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'Try importing the module aScript and using "' + end + w + '@@' + red + bold + '". Or use "' + end + w + '%%' + red + bold + '" next time for comments.')
  elif sun == "do":
    print(bold + red + bold + 'Syntax Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'Try using " ' + end + w + 'do {}' + red + bold + ' " next time for using the module of do.')
  elif sun == 'do {}':
    print(bold + red + bold + 'Name Error Error in: \n' + end + w + sun + '\n' + green + '^~~~~~~~\n' + red + bold + 'Try using " ' + end + w + 'do {var name}' + red + bold + ' " next time for using the module of do.')
  else:
    print(red + bold + 'Error in: \n' + end + red + sun + green + '\n^~~~~~~~~~~~' + red + bold + '\nNo suggestions found.\n')
########################
# END ERROR STATEMENTS #
########################
comm = 0
def banner():
  print(end + "┌────────────────────────────────────────┐");
  print("│                                        │");
  print("│          "+  green + bold +  "      DarkScript" + end +"              |" )
  print("|" +		end+  "                version 0.0.1           │")
  print("│                                        │");
  print("└────────────────────────────────────────┘");
  print()
  print(blue + bold + 'Welcome to an interactive DarkScript class! My name is zoom bot and I will be your coach. Type $tour into the console to start the tour of DarkScript!')
  print(end + green + bold + '\nCommand list: ')
  print('\n$tour')
  print(red + bold + 'Gives an interactive tour of DarkScript')
  print(green + bold + '\n$patch')
  print(red + bold + 'Shows the updates and patches made to DarkScript')
  print()
banner()
print()
con = 0
rand = 0
a = 0
while True:
    sun = input(blue + bold + '~/DarkScript? ' + w + bold)
    if sun == 'window.out window':
      print(w + '<Built in Function>')
    elif 'window.out(\'' in sun:
        spl_word = 'window.out(\''
        res = sun.partition(spl_word)[2]
        res = res.replace('$n', '\n') 
        res = res.replace('\')', '')
        print(res) 
    elif sun == 'window.out (var1)':
      try:
        var1 = var1.replace(';', ' ')
        print(var1)
      except:
        errors()
    elif sun == 'window.out (var2)':
      try:
        var2 = var2.replace(';', ' ')
        print(var2)
      except:
        errors()
    elif sun == 'window.out (var3)':
      try:
        var3 = var3.replace(';', ' ')
        print(var3)
      except:
        errors()
    elif sun == 'window.out var4':
      try:
        var4 = var4.replace(';', ' ')
        print(var4)
      except:
        errors()
    elif 'window.out("' in sun:
        spl_word = 'window.out("'
        res = sun.partition(spl_word)[2]
        res = res.replace('$n', '\n') 
        res = res.replace('")', '')
        print(res) 
    elif '%%' in sun:
      pass
    elif '@@' in sun:
      if a == 1:
        pass
      else:
        errors()
    elif sun == 'window.erase':
        os.system('clear')
        banner()

    elif sun == '$tour':
      os.system('python3 tour.py')
    elif sun == 'import':
        print('Import what?\n')
        sun = input('> ')
        if sun == 'random':
            print('Imported Random')
            rand = 1
            import random
        elif sun == 'console':
            con = 1
            print('Imported console')
        elif sun == 'aScript':
          a = 1
          print('Imported aScript')
        else:
            errors()
    elif sun == 'window.sleep':
        sun = input('. ')
        print('Sleeping for ' + str(sun) + ' seconds')
        time.sleep(int(sun))
        if ValueError in sun:
            print(red + 'ERROR')
    elif sun == "$patch":
      os.system('python3 patchNotes.py ')
    elif "a.show" in sun:
      if a == 1:
        spl_word = 'a.show '
        res = sun.partition(spl_word)[2] 
        print(res)  
      else:
        errors()
    elif sun == '':
      pass
    elif sun == "a.clear":
      if a == 1:
        os.system('clear')
        banner()
      else:
        errors()
    elif sun == 'window.create//var.int':
      
    elif sun == 'def {var}':
      try:
        var_name, value, ab = input(w + bold + '. ').split()
        if var_name in varss:
          if var_name == 'var1':
            if value == 'int':
              var1 = int(ab)
            elif value == 'string':
              var1 = str(ab)
          elif var_name == 'var2':
            if value == 'int':
              var2 = int(ab)
            elif value == 'string':
              var2 = str(ab)
          elif var_name == 'var3':
            if value == 'int':
              var1 = int(ab)
            elif value == 'string':
              var1 = str(ab)
          elif var_name == 'var4':
            if value == 'int':
              var1 = int(ab)
            elif value == 'string':
              var1 = str(ab)
      except:
        print(red + bold + 'ERROR') 
    elif sun == "do {math}":
        try:
          adder, sun1, sun2 =  [x for x in input('. ').split()] 
        except:
          print(red + bold + 'ERROR\nMUST HAVE 3 VALUES\nCAN ONLY HAVE INTIGERS')
          time.sleep(5)
          os.system('python3 main.py')
        try: 
          if adder == "+":
              sun = int(sun1) + int(sun2)
              print(bold + byellow + bold + str(sun))
          elif adder == "-":
              sun = int(sun1) - int(sun2)
              print(bold + byellow + bold + str(sun))
          elif adder == "/":
              sun = int(sun1) / int(sun2)
              print(bold + byellow + bold + str(sun))
          elif adder == "*":
              sun = int(sun1) * int(sun2)
              print(bold + byellow + bold + str(sun))
          elif adder == "//":
            sun = int(sun1) // int(sun2)
            print(bold + byellow + bold + str(sun))
        except:
          print(red + bold + 'ERROR\nCAN NOT HAVE DECIMALS\nCAN NOT HAVE STRINGS, ONLY INTIGERS')
    elif sun == 'window.While':
        print('What are we repeating?\n')
        sun = input('. ')
        while True:
            for i in range(100):
                print(sun)
            sun = input('. ')
            print(sun)
            if sun == 'stop':
                os.system('clear')
                break
            else:
                os.system('clear')
                break
    elif sun == 'console.python':
        if con == 1:
            print('Changing language to python....')
            time.sleep(2)
            print('Language changed to python')
            print(bold)
            break
        else:
            errors()
    elif sun == 'import all':
      import random, time, os
      rand = 1
      con = 1
      a = 1
      print('imported all')
    elif sun == 'create.int':
        sun = input(w + bold + '. ')
        try:
          varint = int(input())
          print(w + bold + 'Created varint')
        except:
           print(red + bold + 'ERROR\nMust me Intiger')
    elif sun == "console.random":
      if con and rand == 1:
        print('What is first the range?\n')
        sun1 = input('. ')
        print('What is the second range?\n')
        sun2 = input('. ')
        print('What will be printed after the first range?\n')
        sun3 = input('. ')
        print('What will be printed after the second range? ')
        sun4 = input('. ')
        print('What will be the else statement?')
        sun5 = input('. ')
        print('Compilling....')
        time.sleep(3)
        os.system('clear')
        sun = random.randint(int(sun1), int(sun2))
        if sun == sun1:
          print(sun3)
        elif sun == sun2:
          print(sun4)
        else:
          print(sun5)
      else:
        errors()
    else:
        errors()
