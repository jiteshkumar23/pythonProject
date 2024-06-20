import autoit
import time
import random
import string


def slow_type_with_error(text, delay=0.1):
    # Choose a random position to make a typing error
    error_position = random.randint(0, len(text) - 1)
    # Choose a random alphabet as the incorrect character
    wrong_character = random.choice(string.ascii_lowercase)

    for i, character in enumerate(text):
        if i == error_position:
            # Type the wrong random character
            autoit.send(wrong_character)
            time.sleep(delay)
            # Backspace to delete the wrong character
            autoit.send("{BACKSPACE}")
            time.sleep(delay)
        # Type the correct character
        autoit.send(character)
        time.sleep(delay)


time.sleep(5)
# autoit.mouse_wheel("up", 10)  # Scrolls up 10 'notches'

# Use the slow_type_with_error function to type "Jitesh Kumar"
slow_type_with_error("Jitesh Kumar", 0.1)

#autoit.send("{TAB}")
autoit.send("{TAB 3}")

slow_type_with_error("Mahesh Kumar", 0.1)


