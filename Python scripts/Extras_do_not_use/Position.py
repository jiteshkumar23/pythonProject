import pyautogui

# Get the current mouse position
print("Move your mouse cursor to the top-left corner of the region and press Enter...")
input()  # Wait for user input
left, top = pyautogui.position()
print(f"Left: {left}, Top: {top}")

print("Move your mouse cursor to the bottom-right corner of the region and press Enter...")
input()  # Wait for user input

right, bottom = pyautogui.position()
print(f"Right: {right}, Bottom: {bottom}")

# Calculate width and height
width = right - left
height = bottom - top

print(f"Width: {width}, Height: {height}")
