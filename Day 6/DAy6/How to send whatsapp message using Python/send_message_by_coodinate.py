import pywhatkit
import pyautogui
import time

# Send the message using pywhatkit
pywhatkit.sendwhatmsg('+917067179450', 'Good Morning boss', 10, 51)

# Wait for the delay to ensure the message is sent before clicking the send button
time.sleep(10)

# Replace these coordinates with the coordinates of the send button
# You can obtain these coordinates using the method mentioned before
send_button_coordinates = (1327, 697)  # Example coordinates

# Move the mouse to the send button and click
pyautogui.moveTo(send_button_coordinates, duration=0.5)
pyautogui.click()

