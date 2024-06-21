import string
import pyautogui
import time
import random
import os
import tkinter as tk
from tkinter import simpledialog
from autoit import autoit
from config import image_directory

delay_correct = 0.1
delay_error = 0.5


def wait_for_image_and_click(image_path, timeout_duration=60, check_interval=0.5):
    # Calculate the timeout end time
    timeout_end = time.time() + timeout_duration

    print(f"Waiting for {image_path} to appear on the screen...")

    while time.time() < timeout_end:
        try:
            # Locate the image on the screen
            location = pyautogui.locateCenterOnScreen(image_path)

            # If the image is found, click on it and break the loop
            if location is not None:
                print(f"Image found at {location}, clicking on it...")
                pyautogui.click(location)
                break
        except pyautogui.ImageNotFoundException:
            # Handle the case where the image is not found
            print(f"Image not found: {image_path}")

        # Wait for the specified interval before checking again
        time.sleep(check_interval)
    else:
        print("Timeout reached. Image not found.")

    print("Task completed.")
    return location


def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    user_input = None

    while user_input != "1":
        user_input = simpledialog.askstring("Input", "Enter 1 to continue:")
        if user_input is None:  # User closed the dialog
            print("User cancelled the input.")
            root.destroy()
            exit()

    root.destroy()  # Close the popup


def click_on_image_in_region(left, top, width, height, image):
    time.sleep(1)
    # Define the region of interest (left, top, width, height)
    region = (left, top, width, height)
    # Print debug information
    print(f"Capturing screenshot of region: {region}")

    # Capture a screenshot of the region
    screenshot = pyautogui.screenshot(region=region)

    # Print debug information
    print("Searching for image 'indian_flag.png' within the captured region...")

    try:
        # Locate the image 'indian_flag.png' within the specified region on the screen
        image_location = pyautogui.locateOnScreen(image, region=region)

        if image_location is not None:
            # Click on the center of the image location
            center = pyautogui.center(image_location)
            pyautogui.click(center)
            print("Image found and clicked.")
        else:
            print("Image not found in the specified region.")
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def human_typing(text, delay_range=(0.0, delay_correct)):
    for char in text:
        autoit.send(char)
        delay = random.uniform(delay_range[0], delay_range[1])
        time.sleep(delay)


def autoit_slow_type_with_error(text):
    # Choose a random position to make a typing error
    error_position = random.randint(0, len(text) - 1)
    # Choose a random alphabet as the incorrect character
    wrong_character = random.choice(string.ascii_lowercase)

    for i, character in enumerate(text):
        if i == error_position:
            # Type the wrong random character
            autoit.send(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(delay_error)
            autoit.send("{BACKSPACE}")
            time.sleep(delay_correct)
        # Type the correct character
        autoit.send(character)
        time.sleep(delay_correct)


def autoit_slow_type_numbers_with_error(numbers):
    # Choose a random position to make a typing error
    error_position = random.randint(0, len(numbers) - 1)
    # Choose a random digit as the incorrect character
    wrong_character = random.choice(string.digits)

    for i, character in enumerate(numbers):
        if i == error_position:
            # Type the wrong random character
            autoit.send(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(delay_error)
            autoit.send("{BACKSPACE}")
            time.sleep(delay_correct)
            # Additional delay for the correction
        # Type the correct character
        autoit.send(character)
        time.sleep(delay_correct)


def main():
    # Path to the image you want to wait for and click on
    ok_image_path = os.path.join(image_directory, 'ok.png')
    firstpersonText_image_path = os.path.join(image_directory, 'firstpersonText.png')
    identity_proof_type_image_path = os.path.join(image_directory, 'identity_proof_type.png')

    # Get user input before starting
    get_user_input()

    # Call the function to wait for the image and click on it
    # location = wait_for_image_and_click(ok_image_path)
    # click on location of ok button again
    # pyautogui.click(location)

    # two tabs to open the checkin date
    # autoit.send("{TAB 2}")

    # Press "Shift" and "W" together
    # pyautogui.hotkey('shift', 'w')

    # Takes you to top of page very fast
    autoit.send("{HOME}")

    location2 = wait_for_image_and_click(firstpersonText_image_path)
    pyautogui.click(location2)
    autoit.send("{TAB}")
    autoit_slow_type_with_error("Jack Dawson")
    autoit.send("{TAB}")
    autoit.send("f")
    time.sleep(0.1)
    # click_on_image_in_region(144, 306, 1609, 138, 'indian_flag.png')
    pyautogui.click(838, 396)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.1)
    human_typing("australia")
    time.sleep(1)
    autoit.send("{ESC}")
    # Wait for a moment before pressing Enter
    time.sleep(0.2)

    # Press Enter key
    autoit.send("{ENTER}")
    time.sleep(0.6)

    pyautogui.click(1007, 390)
    time.sleep(0.2)
    autoit.send("pan")
    autoit.send("{ENTER}")
    autoit.send("{TAB}")
    autoit_slow_type_numbers_with_error("834563895999")
    autoit.send("{TAB}")
    human_typing("33")


if __name__ == "__main__":
    main()
