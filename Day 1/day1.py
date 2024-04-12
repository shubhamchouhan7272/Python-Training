import pywhatkit
import time
import pyautogui

pywhatkit.sendwhatmsg('+919753641357','Hey Bro!, How are you? ',14,10)

time.sleep(10)

send_button_coordinate = (1859,963)

pyautogui.moveTo(send_button_coordinate, duration=0.5)

pyautogui.click()