import datetime
import string
import pyautogui
import time
import random
import tkinter as tk
from tkinter import simpledialog
from autoit import autoit
from config import image_directory, delay_correct, delay_error, pax_1, pax_2, pax_3, pax_4, pax_5, pax_6, \
    firstPersonText_image_path, number_of_adults, nameOfSecondPerson, genderOfSecondPerson, \
    idNumberOfFirstPerson, idTypeOfFirstPerson, idTypeOfSecondPerson, idNumberOfSecondPerson, nameOfFirstPerson, \
    genderOfFirstPerson, countrySecondPerson, countryFirstPerson, ageOfFirstPerson, ageOfSecondPerson


def printDateTime():
    print(f"End time: {datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]}")


def multiplePressUsingPyAutoGUI(key, times):
    pyautogui.press(key, presses=times)


def speed_for_first_page(speed_first_page):
    time.sleep(speed_first_page)


def nationalityDropDownDisplayed():
    if (pax_1.lower() == "foreigner" or
            pax_2.lower() == "foreigner" or
            pax_3.lower() == "foreigner" or
            pax_4.lower() == "foreigner" or
            pax_5.lower() == "foreigner" or
            pax_6.lower() == "foreigner"):
        return True
    else:
        return False


def selectPaxDropdown(case_value):
    switch_dict = {
        'indian': 'i',
        'foreigner': 'f',
        'student': 'st',
        'senior citizen': 'se'
    }
    key = switch_dict.get(case_value.lower())
    if key:
        autoit.send(key)
        return True
    else:
        return False


def wait_for_image_and_click(image_path, timeout_duration=60, check_interval=0.001):
    timeout_end = time.time() + timeout_duration

    print(f"Waiting for {image_path} to appear on the screen...")

    while time.time() < timeout_end:
        try:
            # Locate the image on the screen
            location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)

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
            # Click in the center of the image location
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


def select_room_priority(room_priority):
    key_mapping = {
        "Bijrani": ("shift", "1"),
        "Gairal New": ("shift", "2"),
        "Halduparao": ("shift", "3"),
        "Jhirna": ("shift", "4"),
        "Morghati": ("shift", "5"),
        "Mudiapani": ("shift", "6"),
        "Pakhro": ("shift", "7"),
        "Rathuwadhab": ("shift", "8"),
        "Gairal Dormitory": ("shift", "9"),
        "Hutment-Dhikala": ("shift", "0"),
        "Cabin 4ABC-Dhikala": ("alt", "0"),
        "New-Dhikala": ("alt", "1"),
        "Annexi-Dhikala FRH-1/2/3/4/6": ("alt", "2"),
        "Annexi-Dhikala FRH- 5/7": ("alt", "3"),
        "Sarpduli FRH": ("alt", "4"),
        "Sarpduli Dormitory": ("alt", "5"),
        "Dhela": ("alt", "6"),
        "Sultan": ("alt", "7"),
        "Mailani": ("alt", "8"),
        "Loghut-Dhikala": ("alt", "9")
        # Add more room priorities here
    }

    keys = key_mapping.get(room_priority, None)
    if keys:
        print(f"roomPriority selected is {room_priority}")
        print(f"Keys pressed for {room_priority} are : {keys[0]} + {keys[1]}")
        pyautogui.hotkey(*keys)
    else:
        print("Invalid roomPriority")


def fillForm():
    if int(number_of_adults) >= 1:
        location2 = wait_for_image_and_click(firstPersonText_image_path)
        pyautogui.click(location2)
        fillPersonDetail(nameOfFirstPerson, genderOfFirstPerson, countryFirstPerson, 838, 396, 1007, 390,
                         idTypeOfFirstPerson,
                         idNumberOfFirstPerson, ageOfFirstPerson)

    if int(number_of_adults) >= 2:
        fillPersonDetail(nameOfSecondPerson, genderOfSecondPerson, countrySecondPerson, 838, 563, 1016, 556,
                         idTypeOfSecondPerson,
                         idNumberOfSecondPerson, ageOfSecondPerson)


def fillPersonDetail(name, gender, country, indiaX, indiaY, identityProofX, identityProofY, idType, idNumber, age):
    autoit.send("{TAB}")
    autoit_slow_type_with_error(name)
    autoit.send("{TAB}")
    if gender.lower() == 'female':
        autoit.send("f")
    elif gender.lower() == 'male':
        autoit.send("m")
    elif gender.lower() == 'transgender':
        autoit.send("t")

    time.sleep(0.05)
    # click_on_image_in_region(144, 306, 1609, 138, 'indian_flag.png')
    if nationalityDropDownDisplayed():
        if country.lower() != "india":
            pyautogui.click(indiaX, indiaY)
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(0.5)
            human_typing(country)
            time.sleep(0.5)
            autoit.send("{ESC}")
            # Wait for a moment before pressing Enter
            time.sleep(0.2)
            # Press Enter key
            autoit.send("{ENTER}")
            time.sleep(0.5)
            pyautogui.click(identityProofX, identityProofY)
        else:
            autoit.send("{TAB}")
            time.sleep(0.2)
    else:
        autoit.send("{TAB}")
        time.sleep(0.1)

    if idType.lower() == 'aadhar card':
        autoit.send("aad")
    elif idType.lower() == 'pan card':
        autoit.send("pan")
    elif idType.lower() == 'driving license':
        autoit.send("d")
    elif idType.lower() == 'passport':
        autoit.send("pas")
    elif idType.lower() == 'student id card':
        autoit.send("s")

    if nationalityDropDownDisplayed():
        if country.lower() != "india":
            autoit.send("{ENTER}")
    autoit.send("{TAB}")
    autoit_slow_type_numbers_with_error(idNumber)
    autoit.send("{TAB}")
    human_typing(age)
