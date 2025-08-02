import time
import random

def menu():
  q = input("WHAT IS THE QUESTION: ")
  vb1 = random.randint(1, 10)
  vb2 = random.randint(1, 10)
  vb3 = random.randint(1, 10)
  vb4 = random.randint(1, 10)
  vb5 = random.randint(1, 10)
  vb1a = "Yes" if vb1 % 2 == 0 else "No"
  vb2a = "Yes" if vb2 % 2 == 0 else "No"
  vb3a = "Yes" if vb3 % 2 == 0 else "No"
  vb4a = "Yes" if vb4 % 2 == 0 else "No"
  vb5a = "Yes" if vb5 % 2 == 0 else "No"
  for countdown in range(5, 0, -1):
    print(countdown)
    time.sleep(1)
  print("VILLAGERTOPIA BANK TRUSTEE #1: " + vb1a)
  print("VILLAGERTOPIA BANK TRUSTEE #2: " + vb2a)
  print("VILLAGERTOPIA BANK TRUSTEE #3: " + vb3a)
  print("VILLAGERTOPIA BANK TRUSTEE #4: " + vb4a)
  print("VILLAGERTOPIA BANK TRUSTEE #5: " + vb5a)
  time.sleep(1)
  final = input("RETURN? (Y/N): ")
  if final.upper() == "Y":
    menu()
  elif final.upper() == "N":
    return

print("VILLAGERTOPIA BANK MENU")
time.sleep(1)
menu()
