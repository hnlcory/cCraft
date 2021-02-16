import pyautogui, time

time.sleep(10)
print('LETS GOOOOOO')
f= open('assets/bee.txt','r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
  
  
  
  