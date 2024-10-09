import pyautogui

print("Start")
# Press the TAB key 50 times
# pyautogui.press('tab', presses=50)
pyautogui.press('space', presses=100)
print("end")

# Declare a global variable
global_var = 42


def modify_global_variable():
    # Access the global variable
    global global_var
    print(f"Original global variable value: {global_var}")

    # Modify the global variable
    global_var += 10
    print(f"Updated global variable value: {global_var}")


# Call the method
modify_global_variable()
