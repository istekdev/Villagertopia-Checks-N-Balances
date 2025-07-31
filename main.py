import time
import random

def menu():
  q = input("WHAT IS THE QUESTION: ")
  a = input("WHAT IS YOUR DECISION (Y/N): ")
  if a.upper() == "Y":
    exa = "Yes"
  elif a.upper() == "N":
    exa = "No"
  else:
    exa = "ERR"
  con1 = random.randint(1, 10)
  con2 = random.randint(1, 10)
  con3 = random.randint(1, 10)
  jud1 = random.randint(1, 10)
  jud2 = random.randint(1, 10)
  jud3 = random.randint(1, 10)
  if con1 in [2, 4, 6, 8, 10]:
    cona = "Yes"
  elif con1 in [1, 3, 5, 7, 9]:
    cona = "No"
  elif con2 in [2, 4, 6, 8, 10]:
    con2a = "Yes"
  elif con2 in [1, 3, 5, 7, 9]:
    con2a = "No"
  elif con3 in [2, 4, 6, 8, 10]:
    con3a = "Yes"
  elif con3 in [1, 3, 5, 7, 9]:
    con3a = "No"
  elif jud1 in [2, 4, 6, 8, 10]:
    jud1a = "Yes"
  elif jud1 in [1, 3, 5, 7, 9]:
    jud1a = "No"
  elif jud2 in [2, 4, 6, 8, 10]:
    jud2a = "Yes"
  elif jud2 in [1, 3, 5, 7, 9]:
    jud2a = "No"
  elif jud3 in [2, 4, 6, 8, 10]:
    jud3a = "Yes"
  elif jud3 in [1, 3, 5, 7, 9]:
    jud3a = "No"
  else:
    print("ERR")
    time.sleep(1)
    menu()
  for countdown in range(5, 0, -1):
    print(countdown)
    time.sleep(1)
  print("CONGRESS REPRESENATIVE #1 VOTED: " + con1)
  print("CONGRESS REPRESENATIVE #2 VOTED: " + con2)
  print("CONGRESS SENATOR #1 VOTED: " + con3)
  print("JUDICIARY CHIEF JUSTICE VOTED: " + jud1)
  print("JUDICIARY JUSTICE #1 VOTED: " + jud2)
  print("JUDICIARY JUSTICE #2 VOTED: " + jud3)
  time.sleep(1)
  final = input("RETURN? (Y/N): ")
  if final.upper() == "Y":
    menu()
  elif final.upper() == "N":
    return

print("VILLAGERTOPIA MENU")
time.sleep(1)
menu()
