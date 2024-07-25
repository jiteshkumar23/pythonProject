import keyboard
from autoit import autoit

from CoreMethods import (nationalityDropDownDisplayed,
                         fillForm, debounce_key, firstPageFill)


def main():
    valueOfNationalityDropDownDisplayed = nationalityDropDownDisplayed()
    print(valueOfNationalityDropDownDisplayed)

    # print("Press Ctrl+Alt+X to continue...")
    # while not custom_hotkey():
    #     pass
    # print("Hotkey pressed! Continuing...")

    # Get user input before starting
    # get_user_input()

    while True:
        if keyboard.is_pressed("ctrl+alt+x"):
            print("Exiting the loop. Goodbye!")
            break
        elif keyboard.is_pressed("ctrl+alt+j"):
            print("Filling first page only")
            firstPageFill()
            debounce_key("ctrl+alt+j")  # Wait until the key is released
        elif keyboard.is_pressed("ctrl+alt+m"):
            print("Filling second page only")
            # Takes you to top of page very fast
            autoit.send("{HOME}")
            # Fill the form on second page
            fillForm()
            debounce_key("ctrl+alt+m")  # Wait until the key is released
        elif keyboard.is_pressed("ctrl+alt+p"):
            print("Filling First and second page")
            firstPageFill()
            # Takes you to top of page very fast
            autoit.send("{HOME}")
            # Fill the form on second page
            fillForm()
            debounce_key("ctrl+alt+p")  # Wait until the key is released


if __name__ == "__main__":
    main()
