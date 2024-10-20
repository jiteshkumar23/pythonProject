import os
import subprocess
import sys
import time

import keyboard
from autoit import autoit

from CoreMethods.CoreMethods import (fillForm, debounce_key, firstPageFill, enterMobile, payment, setImagePath)
from config import checkInDate, checkOutDate


def exit_program():
    print("r+4 keys pressed - Exiting... Goodbye!")
    os._exit(0)  # Exit the current process


def main():
    # valueOfNationalityDropDownDisplayed = nationalityDropDownDisplayed()
    setImagePath()
    print("CheckInDate -->"+checkInDate+"  and CheckOutDate-->"+checkOutDate)
    print("Press - r+1 - For filling first page only")
    print("Press - r+2 - For filling form and payment only")
    print("Press - r+3 - For filling  first page , form and payment")
    print("Press - r+4 - For exiting the script")

    # Add listener
    keyboard.add_hotkey('r+4', exit_program)

    # print("Press Ctrl+Alt+X to continue...")
    # while not custom_hotkey():
    #     pass
    # print("Hotkey pressed! Continuing...")

    # Get user input before starting
    # get_user_input()

    while True:
        # if keyboard.is_pressed("r+4"):
        #     print("Keys Pressed - r+4 - Exiting........... Goodbye!")
        #     break
        # elif keyboard.is_pressed("ctrl+alt+j"):
        if keyboard.is_pressed("r+1"):
            print("Keys Pressed - r+1 - Filling first page only")
            firstPageFill()
            debounce_key("r+1")  # Wait until the key is released
        elif keyboard.is_pressed("r+2"):
            print("Keys Pressed - r+2  -Filling second page only")
            # Takes you to top of page very fast
            autoit.send("{HOME}")
            # Fill the form on second page
            fillForm()
            enterMobile()
            payment()
            debounce_key("r+2")  # Wait until the key is released
        elif keyboard.is_pressed("r+3"):
            print("Keys Pressed - r+3 - Filling First and second page")
            firstPageFill()
            # Takes you to top of page very fast
            autoit.send("{HOME}")
            # Fill the form on second page
            fillForm()
            enterMobile()
            payment()
            debounce_key("r+3")  # Wait until the key is released


if __name__ == "__main__":
    main()
