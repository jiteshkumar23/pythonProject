import pyautogui
import random
import string


def fast_type_with_error_pyautogui(text):
    # Choose a random position to make a typing error
    error_position = random.randint(0, len(text) - 1)
    # Choose a random alphabet as the incorrect character
    wrong_character = random.choice(string.ascii_lowercase)

    for i, character in enumerate(text):
        if i == error_position:
            # Type the wrong random character
            pyautogui.write(wrong_character)
            # Backspace to delete the wrong character
            pyautogui.press('backspace')
        # Type the correct character
        pyautogui.write(character)


# Use the fast_type_with_error_pyautogui function to type "Jitesh Kumar"
fast_type_with_error_pyautogui("Jitesh Kumar")
