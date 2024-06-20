import time

import pyautogui

time.sleep(5)
# Get the current mouse cursor position
x, y = pyautogui.position()

# Print the coordinates
print(f"Current mouse position - X: {x}, Y: {y}")
