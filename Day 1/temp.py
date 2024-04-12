import pyautogui
import time

print("move the mouse")

time.sleep(5)

x, y = pyautogui.position()

print(f"send button coordinate : x={x},y={y}")