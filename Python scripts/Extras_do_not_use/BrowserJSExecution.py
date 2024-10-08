import pyautogui
import time

# Open the browser (assuming it's already open)
# Navigate to the browser window
time.sleep(5)

# Open the console with F12
pyautogui.press('f12')
time.sleep(2)

# Type JavaScript code
js_code = "alert('Hello, world!');"
pyautogui.typewrite(js_code)
time.sleep(1)

# Press Enter to execute the code
pyautogui.press('enter')
