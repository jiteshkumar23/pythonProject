import pyautogui

# List available easing functions
tween_functions = [func for func in dir(pyautogui) if func.startswith('ease')]
print(tween_functions)
