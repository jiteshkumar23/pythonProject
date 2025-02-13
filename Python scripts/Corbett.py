import os
import subprocess
import sys
import time

import keyboard
from autoit import autoit

from CoreMethods.CoreMethods import (
    fillForm, debounce_key, firstPageFill, enterMobile, payment, setImagePath, roomSelection
)
from config import checkInDate, checkOutDate


def exit_program():
    print("r+5 keys pressed - Exiting... Goodbye!")
    os._exit(0)  # Exit the current process


def handle_key_press():
    if keyboard.is_pressed("r+1"):
        print("Keys Pressed - r+1 - Filling first page only")
        firstPageFill()
        debounce_key("r+1")  # Wait until the key is released
        return True
    elif keyboard.is_pressed("r+2"):
        print("Keys Pressed - r+2  - Room Selection")
        roomSelection()
        return True
    elif keyboard.is_pressed("r+3"):
        print("Keys Pressed - r+3  - Filling form only")
        autoit.send("{HOME}")  # Takes you to the top of the page very fast
        time.sleep(0.25)
        fillForm()
        debounce_key("r+3")  # Wait until the key is released
        return True
    elif keyboard.is_pressed("r+4"):
        print("Keys Pressed - r+4 - payment")
        payment()
        debounce_key("r+4")  # Wait until the key is released
        return True
    return False  # Indicate that no key was pressed


def print_instructions():
    print("Press - r+1 - For filling first page only")
    print("Press - r+2 - For Room Selection")
    print("Press - r+3 - For filling form on second page")
    print("Press - r+4 - For payment")
    print("Press - r+5 - For exiting the script")


def main():
    setImagePath()
    print("CheckInDate -->" + checkInDate + "  and CheckOutDate -->" + checkOutDate)
    print_instructions()

    # Add listener for exiting the program
    keyboard.add_hotkey('r+5', exit_program)

    while True:
        if handle_key_press():
            print_instructions()
        time.sleep(0.1)  # Small delay to prevent high CPU usage


if __name__ == "__main__":
    main()
