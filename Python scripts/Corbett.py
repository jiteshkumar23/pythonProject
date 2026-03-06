import os
import time
import autoit
import keyboard


from CoreMethods.CoreMethods import (
    fillForm, debounce_key, firstPageFill, payment, setImagePath, roomSelection, otpBoxHandling,
    analyze_buttons
)
from config import checkInDate, checkOutDate


def exit_program():
    print("alt+q keys pressed - Exiting... Goodbye!")
    os._exit(0)  # Exit the current process


def handle_key_press():
    if keyboard.is_pressed("alt+1"):
        debounce_key("alt+1")
        print("Keys Pressed - alt+1 - Filling first page only")
        firstPageFill()
        return True
    elif keyboard.is_pressed("alt+2"):
        debounce_key("alt+2")
        print("Keys Pressed - alt+2  - Room Selection")
        roomSelection()
        return True
    elif keyboard.is_pressed("alt+3"):
        debounce_key("alt+3")
        print("Keys Pressed - alt+3  - Filling form only")
        autoit.send("{HOME}")  # Takes you to the top of the page very fast
        time.sleep(0.25)
        fillForm()
        return True
    elif keyboard.is_pressed("alt+4"):
        debounce_key("alt+4")  # Wait until the key is released
        print("Keys Pressed - alt+4 - payment")
        payment()
        return True
    # elif keyboard.is_pressed("alt+5"):
    #     print("Keys Pressed - alt+5 - mobile number")
    #     analyze_buttons()
    #     debounce_key("alt+5")  # Wait until the key is released
    #     return True
    elif keyboard.is_pressed("alt+w"):
        debounce_key("alt+w")
        print("Keys Pressed - alt+w - OTP Box Handling")
        otpBoxHandling()
        return True
    return False  # Indicate that no key was pressed


def print_instructions():
    print("Press - alt+1 - For filling first page only")
    print("Press - alt+2 - For Room Selection")
    print("Press - alt+3 - For filling form on second page")
    print("Press - alt+4 - For payment")
    print("Press - alt+w - For only OTP Box Handling")
    print("Press - alt+q - For exiting the script")


def main():
    setImagePath()
    print("CheckInDate -->" + checkInDate + "  and CheckOutDate -->" + checkOutDate)
    print_instructions()

    # Add listener for exiting the program
    keyboard.add_hotkey('alt+q', exit_program)

    while True:
        if handle_key_press():
            print_instructions()
        time.sleep(0.1)  # Small delay to prevent high CPU usage


if __name__ == "__main__":
    main()
