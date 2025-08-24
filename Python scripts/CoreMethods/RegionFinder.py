import pyautogui
import keyboard
import time

def capture_position(key_label):
    print(f"Place your cursor and press '{key_label}'...")
    while True:
        if keyboard.is_pressed(key_label):
            pos = pyautogui.position()
            print(f"Captured ({pos.x}, {pos.y})")
            time.sleep(0.5)  # debounce
            return pos

# Step 1: Capture top-left
top_left = capture_position('a')

# Step 2: Capture bottom-right
bottom_right = capture_position('b')

# Step 3: Calculate region
x = top_left.x
y = top_left.y
width = bottom_right.x - top_left.x
height = bottom_right.y - top_left.y

region1 = (x, y, width, height)
print(f"\n✅ Region captured: region1 = {region1}")