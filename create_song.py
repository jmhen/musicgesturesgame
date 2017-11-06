import pyautogui, pymsgbox, time
time.sleep(1)
instrumentList = ["a","b","c","d"]
file = pymsgbox.prompt("eg.7-4")



#open the file selected

pyautogui.moveTo(997,1062,0.5)
pyautogui.click()
pyautogui.hotkey("ctrl","o")
pyautogui.typewrite("Song"+file)
pyautogui.hotkey("enter")


#save piano file

pyautogui.hotkey('ctrl', 'alt', 'e')
pyautogui.moveTo(268,420,0.2)
pyautogui.click()
pyautogui.typewrite(instrumentList[0])
pyautogui.hotkey("enter")
time.sleep(1)

#save violin file
pyautogui.moveTo(241,249,0.2)
pyautogui.rightClick()
pyautogui.moveTo(350,465,0.2)
pyautogui.click()
pyautogui.moveTo(781,503,0.2)
pyautogui.click()
pyautogui.moveTo(1205,573,0.2)
pyautogui.click()
pyautogui.moveTo(1224,585,0.2)
pyautogui.click()
pyautogui.hotkey("enter")
pyautogui.moveTo(1200,827,0.2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'alt', 'e')
pyautogui.moveTo(268,420,0.2)
pyautogui.click()
pyautogui.typewrite(instrumentList[1])
pyautogui.hotkey("enter")
time.sleep(1)

#save guitar file
pyautogui.moveTo(241,249,0.2)
pyautogui.rightClick()
pyautogui.moveTo(350,465,0.2)
pyautogui.click()
pyautogui.moveTo(781,503,0.2)
pyautogui.click()
pyautogui.moveTo(1222,556,0.2)
pyautogui.click()
pyautogui.moveTo(1244,597,0.2)
pyautogui.click()
pyautogui.hotkey("enter")
pyautogui.moveTo(1200,827,0.2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'alt', 'e')
pyautogui.moveTo(268,420,0.2)
pyautogui.click()
pyautogui.typewrite(instrumentList[2])
pyautogui.hotkey("enter")
time.sleep(1)

#save trumpet file
pyautogui.moveTo(241,249,0.2)
pyautogui.rightClick()
pyautogui.moveTo(350,465,0.2)
pyautogui.click()
pyautogui.moveTo(781,503,0.2)
pyautogui.click()
pyautogui.moveTo(1203,467,0.2)
pyautogui.click()
pyautogui.moveTo(1244,524,0.2)
pyautogui.click()
pyautogui.hotkey("enter")
pyautogui.moveTo(1200,827,0.2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'alt', 'e')
pyautogui.moveTo(268,420,0.2)
pyautogui.click()
pyautogui.typewrite(instrumentList[3])
pyautogui.hotkey("enter")
time.sleep(1)


