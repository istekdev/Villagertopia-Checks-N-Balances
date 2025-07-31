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
  cona = "Yes" if con1 % 2 == 0 else "No"
  con2a = "Yes" if con2 % 2 == 0 else "No"
  con3a = "Yes" if con3 % 2 == 0 else "No"
  jud1a = "Yes" if jud1 % 2 == 0 else "No"
  jud2a = "Yes" if jud2 % 2 == 0 else "No"
  jud3a = "Yes" if jud3 % 2 == 0 else "No"
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
