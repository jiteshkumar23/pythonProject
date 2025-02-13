import pyautogui
import time

# Move the mouse to the specified coordinates (x, y) over 1 second
pyautogui.moveTo(100, 100, duration=1)
time.sleep(1)

# Move the mouse relative to its current position (50 pixels right and 50 pixels down) over 1 second
pyautogui.moveRel(50, 50, duration=1)
time.sleep(1)

# Click at the current position
pyautogui.click()

# Scroll up 500 units
pyautogui.scroll(500)

# Scroll down 500 units
pyautogui.scroll(-500)



