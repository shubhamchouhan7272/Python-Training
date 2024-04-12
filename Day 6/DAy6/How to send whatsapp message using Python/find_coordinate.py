import pyautogui
import time

print("Move the mouse to the send button and wait for a few seconds...")
time.sleep(5)  # Give yourself time to position the mouse

# Get current mouse coordinates
x, y = pyautogui.position()

print(f"Send button coordinates: x={x}, y={y}")
