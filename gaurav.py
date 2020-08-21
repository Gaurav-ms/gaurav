import os
print(" \t\t\t\t\t welcome to my chatbot")
while True:
      p=input("Please enter your choice sir: ")
      if (("run" in p) or ("execute" in p)) and ("chrome" in p):
        os.system("chrome")
      elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
        os.system("notepad")
      elif (("run" in p) or ("execute" in p)) and (("calculator" in p) or ("calc" in p)):
        os.system("calc")
      elif (("run" in p) or ("execute" in p)) and ("player" in p):
        os.system("wmplayer")
      elif (("run" in p) or ("execute" in p)) and (("adobe" in p) or ("reader" in p)):
        os.system("AcroRd32")
      elif (("run" in p) or ("execute" in p)) and ("vlc" in p):
        os.system("vlc")
      elif (("run" in p) or ("execute" in p)) and ("virtualbox" in p):
        os.system("virtualbox")
      elif (("run" in p) or ("execute" in p)) and (("mozilla" in p) or ("firefox" in p)):
        os.system("firefox")
      elif (("exit" in p) or ("quit" in p)):
        break
      else:
        print("oops.........this doesn't support")  
      
      
                   	