import datetime
import os
import random
import string
import time
import tkinter as tk
from datetime import datetime
from tkinter import simpledialog
import cv2
import keyboard
import numpy as np
import pyautogui
from autoit import autoit
from pynput import mouse
import time

from config import delay_correct, pax_1, pax_2, pax_3, pax_4, pax_5, pax_6, \
    number_of_adults, nameOfSecondPerson, genderOfSecondPerson, \
    idNumberOfFirstPerson, idTypeOfFirstPerson, idTypeOfSecondPerson, idNumberOfSecondPerson, nameOfFirstPerson, \
    genderOfFirstPerson, countrySecondPerson, countryFirstPerson, ageOfFirstPerson, ageOfSecondPerson, \
    nameOfThirdPerson, genderOfThirdPerson, countryThirdPerson, idTypeOfThirdPerson, idNumberOfThirdPerson, \
    ageOfThirdPerson, nameOfFourthPerson, genderOfFourthPerson, countryFourthPerson, idTypeOfFourthPerson, \
    idNumberOfFourthPerson, ageOfFourthPerson, nameOfFifthPerson, genderOfFifthPerson, countryFifthPerson, \
    idTypeOfFifthPerson, idNumberOfFifthPerson, ageOfFifthPerson, nameOfSixthPerson, genderOfSixthPerson, \
    countrySixthPerson, idTypeOfSixthPerson, idNumberOfSixthPerson, ageOfSixthPerson, speed_first_page, \
    number_of_children, number_of_rooms, \
    room, mobileNumber, emailAddress, paymentMethod, card_number, Month, Year, CVV, NameOnCard, machine, checkInDate, \
    checkOutDate, UPI_ADDRESS, randomness_profile, typingGap

from room_shortcuts import select_room_priority

fifth = False
currentPerson = 0

global image_directory, ok_image_path, firstPersonText_image_path, firstPersonText_image_path2, \
    identity_proof_type_image_path, iamforeigner_image_path, iamIndian_image_path, \
    ReservationsFor_image_path, success_image_path, indian_flag_image_path, \
    SelectPaymentOption_image_path, UPI_image_path, PayNow_image_path, email_image_path, \
    continue_image_path, contactdetails_image_path, showQR_image_path, \
    recommended_image_path, creditcard_image_path, payViaCard_image_path, \
    addANewCard_image_path, rooms_image_path, tiger_image_path, proceedAfterTiger_image_path, UPIQR_AfterTiger_image_path, \
    showQR_AfterTiger_image_path, UPI_ID_image_path, UPI_ID_Image2_image_path, gender_dropdown_image_path, \
    id_details_image_path, age_image_path, fullname_image_path, mobile_image_path

global indiaFlagX, identityDropDownX, Y1, Y2, Y3, Y4, Y5, Y6


def printDateTime():
    print(f"End time: {datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]}")


def multiplePressUsingPyAutoGUI(key, times):
    print("pressing " + " " + key + " " + str(times))
    pyautogui.press(key, presses=times)


def speed_for_first_page(speed):
    time.sleep(speed)


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


def allForeigners():
    if (pax_1.lower() == "foreigner" and
            pax_2.lower() == "foreigner" and
            pax_3.lower() == "foreigner" and
            pax_4.lower() == "foreigner" and
            pax_5.lower() == "foreigner" and
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


def wait_for_image1_or_image2_and_click(image_path, image_path2, timeout_duration=60, check_interval=0.001):
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
            try:
                location = pyautogui.locateCenterOnScreen(image_path2, grayscale=True)
                if location is not None:
                    print(f"Image found at {location}, clicking on it...")
                    pyautogui.click(location)
                    break
            except pyautogui.ImageNotFoundException:
                print(f"Image not found: {image_path2}")

        # Wait for the specified interval before checking again
        time.sleep(check_interval)
    else:
        print("Timeout reached. Image not found.")

    print("Task completed.")
    return location


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


def human_typing(text):
    for char in text:
        autoit.send(char)
        time.sleep(random.uniform(0.05, typingGap))


def human_typing_other(text):
    for char in text:
        autoit.send(char)
        time.sleep(random.uniform(0.05, 0.08))


# def autoit_slow_type_with_error(text):
#     # Choose a random position to make a typing error
#     error_position = random.randint(0, len(text) - 1)
#     # Choose a random alphabet as the incorrect character
#     wrong_character = random.choice(string.ascii_lowercase)
#
#     for i, character in enumerate(text):
#         if i == error_position:
#             # Type the wrong random character
#             autoit.send(wrong_character)
#             # Backspace to delete the wrong character
#             time.sleep(delay_error)
#             autoit.send("{BACKSPACE}")
#             time.sleep(delay_correct)
#         # Type the correct character
#         autoit.send(character)
#         # pyautogui.press(character)
#         time.sleep(delay_correct)

def autoit_slow_type_with_error(text):
    if len(text) <= 4:
        for character in text:
            autoit.send(character)
            time.sleep(random.uniform(0.05, 0.2))
        return

    # Choose a few random positions to make typing errors
    num_errors = random.randint(1, 4)  # Randomly decide how many errors to make
    error_positions = random.sample(range(len(text)), num_errors)
    error_chars = string.ascii_lowercase + string.ascii_uppercase
    for i, character in enumerate(text):
        if i in error_positions:
            # Choose a random wrong character
            wrong_character = random.choice(error_chars)
            # Type the wrong random character
            autoit.send(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(random.uniform(0.2, 0.5))  # Random delay for error
            autoit.send("{BACKSPACE}")
            time.sleep(random.uniform(0.2, 0.4))  # Random delay for correction
        # Type the correct character
        autoit.send(character)
        time.sleep(random.uniform(0.05, 0.2))  # Random delay for typing speed


def typing_text_with_random_delays(text, random_numbers, random_numbers3):
    text = text.lower()
    count = len(text)
    new_random = random_number_between_min_and_max(1, count)

    for i in range(new_random - 1):
        pyautogui.typewrite(text[i])
        time.sleep(random.uniform(0.01, 0.10))

    if randomness_profile == 3 and currentPerson in random_numbers3:
        error_chars = string.ascii_lowercase
        wrong_character1 = random.choice(error_chars)
        autoit.send(wrong_character1)
        time.sleep(random.uniform(0.1, 0.2))
        autoit.send(wrong_character1)
        time.sleep(random.uniform(0.5, 0.6))
        autoit.send("{BACKSPACE}")
        time.sleep(random.uniform(0.1, 0.2))
        autoit.send("{BACKSPACE}")
        time.sleep(random.uniform(0.1, 0.2))

    if (randomness_profile == 4 or randomness_profile == 5) and currentPerson in random_numbers:
        time.sleep(random.uniform(1, 1.5))

    for i in range(new_random - 1, count):
        pyautogui.typewrite(text[i])
        time.sleep(random.uniform(0.01, 0.10))

    time.sleep(random.uniform(0.01, 0.10))


def generate_3_random_numbers():
    return random.sample(range(1, 7), 3)


def generate_3_random_numbers_2():
    return random.sample(range(1, 7), 3)


def generate_1_random_number():
    return random.sample(range(1, 7), 1)


def typing_text_with_random_delays_IDNumber(text, currentPerson, random_numbers2):
    text = text.lower()
    count = len(text)
    for i in range(count):
        pyautogui.typewrite(text[i])
        time.sleep(random.uniform(0.01, 0.10))
        if i == 3 and (randomness_profile == 2 or randomness_profile == 5) and currentPerson in random_numbers2:
            time.sleep(random.uniform(1, 1.5))
    time.sleep(random.uniform(0.01, 0.10))


def random_number_between_min_and_max(min_val, max_val):
    return random.randint(min_val, max_val)


def pyautogui_slow_type_with_error(text):
    delay_correct = 0.1  # Adjust these values to fine-tune typing speed
    delay_error = 0.3

    # Choose a random position to make a typing error
    error_position = random.randint(0, len(text) - 1)
    # Choose a random alphabet as the incorrect character
    wrong_character = random.choice('abcdefghijklmnopqrstuvwxyz')

    for i, character in enumerate(text):
        if i == error_position:
            # Type the wrong random character
            pyautogui.typewrite(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(delay_error)
            pyautogui.press('backspace')
            time.sleep(delay_correct)

        # Random slight delay before typing the next correct character
        random_delay = delay_correct + random.uniform(-0.05, 0.05)
        pyautogui.typewrite(character)
        time.sleep(random_delay)

        # Occasional longer pause to simulate thinking/hesitating
        if random.random() < 0.1:  # 10% chance of a pause
            time.sleep(random.uniform(0.11, 0.22))


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
            time.sleep(0.25)
            autoit.send("{BACKSPACE}")
            time.sleep(delay_correct)
            # Additional delay for the correction
        # Type the correct character
        autoit.send(character)
        time.sleep(delay_correct)


def fillForm():
    global fifth
    global currentPerson
    global indiaFlagX, identityDropDownX, Y1, Y2, Y3, Y4, Y5, Y6
    random_numbers = generate_3_random_numbers()
    random_numbers2 = generate_3_random_numbers_2()
    random_numbers3 = generate_1_random_number()
    print(random_numbers)
    print(random_numbers2)
    print(random_numbers3)
    if machine == "laptop":
        region1 = (251, 279, 1403, 142)
        region2 = (251, 440, 1403, 142)
        region3 = (251, 605, 1403, 142)
        region4 = (251, 768, 1403, 142)
        region5 = (251, 897, 1403, 142)
        region6 = (251, 498, 1403, 142)
        indiaFlagX = 861
        identityDropDownX = 1054
        Y1 = 332
        Y2 = 494
        Y3 = 656
        Y4 = 815
        Y5 = 981
        Y6 = 569
    elif machine == "desktop":
        indiaFlagX = 602
        identityDropDownX = 767
        Y1 = 298
        Y2 = 430
        Y3 = 559
        Y4 = 687
        Y5 = 426
        Y6 = 554
    elif machine == "rohit":
        indiaFlagX = 602
        identityDropDownX = 767
        Y1 = 260
        Y2 = 394
        Y3 = 524
        Y4 = 649
        Y5 = 412
        Y6 = 536
    elif machine == "pradeeplaptop":
        indiaFlagX = 861
        identityDropDownX = 1054
        Y1 = 332
        Y2 = 530
        Y3 = 701
        Y4 = 860
        Y5 = 991
        Y6 = 585
    time.sleep(1.25)
    autoit.send("{HOME}")
    autoit.send("{HOME}")

    if int(number_of_adults) >= 1:
        currentPerson = 1
        fillPersonDetail(nameOfFirstPerson, genderOfFirstPerson, countryFirstPerson, indiaFlagX, Y1, identityDropDownX,
                         Y1,
                         idTypeOfFirstPerson,
                         idNumberOfFirstPerson, ageOfFirstPerson, currentPerson, random_numbers, random_numbers2,
                         random_numbers3, region1)

    if int(number_of_adults) >= 2:
        currentPerson = 2
        fillPersonDetail(nameOfSecondPerson, genderOfSecondPerson, countrySecondPerson, indiaFlagX, Y2,
                         identityDropDownX, Y2,
                         idTypeOfSecondPerson,
                         idNumberOfSecondPerson, ageOfSecondPerson, currentPerson, random_numbers, random_numbers2,
                         random_numbers3, region2)
    if int(number_of_adults) >= 3:
        currentPerson = 3
        fillPersonDetail(nameOfThirdPerson, genderOfThirdPerson, countryThirdPerson, indiaFlagX, Y3, identityDropDownX,
                         Y3,
                         idTypeOfThirdPerson, idNumberOfThirdPerson, ageOfThirdPerson, currentPerson, random_numbers,
                         random_numbers2, random_numbers3, region3)
    if int(number_of_adults) >= 4:
        currentPerson = 4
        fillPersonDetail(nameOfFourthPerson, genderOfFourthPerson, countryFourthPerson, indiaFlagX, Y4,
                         identityDropDownX, Y4,
                         idTypeOfFourthPerson, idNumberOfFourthPerson, ageOfFourthPerson, currentPerson, random_numbers,
                         random_numbers2, random_numbers3, region4)

    if int(number_of_adults) >= 5:
        currentPerson = 5
        fifth = True
        fillPersonDetail(nameOfFifthPerson, genderOfFifthPerson, countryFifthPerson, indiaFlagX, Y5, identityDropDownX,
                         Y5,
                         idTypeOfFifthPerson, idNumberOfFifthPerson, ageOfFifthPerson, currentPerson, random_numbers,
                         random_numbers2, random_numbers3, region5)

    if int(number_of_adults) >= 6:
        currentPerson = 6
        # fifth = False
        fillPersonDetail(nameOfSixthPerson, genderOfSixthPerson, countrySixthPerson, indiaFlagX, Y6, identityDropDownX,
                         Y6,
                         idTypeOfSixthPerson, idNumberOfSixthPerson, ageOfSixthPerson, currentPerson, random_numbers,
                         random_numbers2, random_numbers3, region6)
    pyautogui.scroll(-2500)
    enterMobile()

def playback_mouse_movements(fileName):
    mouse_movements = []
    with open(fileName, 'r') as file:
        for line in file:
            mouse_movements.append(eval(line.strip()))

    # Playback the mouse movements
    controller = mouse.Controller()
    start_time = mouse_movements[0][-1]

    for movement in mouse_movements:
        action, x, y, *rest, timestamp = movement
        delay = timestamp - start_time

        # Sleep to synchronize the playback
        if delay > 0:
            time.sleep(delay)

        if action == 'move':
            controller.position = (x, y)
        elif action == 'click':
            button = mouse.Button[rest[0]]
            pressed = rest[1]
            if pressed:
                controller.press(button)
            else:
                controller.release(button)
        elif action == 'scroll':
            dx, dy = rest[0], rest[1]
            controller.scroll(dx, dy)

        start_time = timestamp


def fillPersonDetail(name, gender, country, indiaX, indiaY, identityProofX, identityProofY, idType, idNumber, age,
                     currentPerson, random_numbers, random_numbers2, random_numbers3, region):
    print(currentPerson)
    if not (machine == "laptop" and currentPerson >= 5):
        pyautogui.click(find_image_on_screen_using_opencv_in_region(fullname_image_path, 10, region=region))
        # fullname_location = pyautogui.locateOnScreen(fullname_image_path, region=region, confidence=0.7)
        # pyautogui.click(fullname_location)

    wait_for_alt_q()
    time.sleep(0.1)
    # typing_text_with_random_delays(name, random_numbers, random_numbers3)
    # type_text(name.lower())
    human_typing(name.lower())

    gender_dropdown_location = pyautogui.locateOnScreen(gender_dropdown_image_path, region=region, confidence=0.7)

    # wait for alt+q
    wait_for_alt_q()

    # Mouse movement
    move_mouse_to_center(gender_dropdown_location)

    # Click
    pyautogui.click(gender_dropdown_location)

    if gender.lower() == 'female':
        autoit.send("f")
    elif gender.lower() == 'male':
        autoit.send("m")
    elif gender.lower() == 'transgender':
        autoit.send("t")

    time.sleep(0.05)
    autoit.send("{ENTER}")

    # click_on_image_in_region(144, 306, 1609, 138, 'indian_flag.png')
    # if nationalityDropDownDisplayed():
    #     if country.lower() != "india":
    #         pyautogui.click(indiaX, indiaY)
    #         pyautogui.hotkey('ctrl', 'f')
    #         time.sleep(0.5)
    #         human_typing(country)
    #         # autoit.send(country)
    #         time.sleep(0.5)
    #         autoit.send("{ESC}")
    #         # Wait for a moment before pressing Enter
    #         time.sleep(0.2)
    #         # Press Enter key
    #         autoit.send("{ENTER}")
    #         time.sleep(0.75)
    #         pyautogui.click(identityProofX, identityProofY)
    #     else:
    #         time.sleep(0.25)
    #         autoit.send("{TAB}")
    # else:
    #     time.sleep(0.25)

    identity_proof_type_location = pyautogui.locateOnScreen(identity_proof_type_image_path, region=region,
                                                            confidence=0.7)
    wait_for_alt_q()

    # Mouse movement
    move_mouse_to_center(identity_proof_type_location)

    pyautogui.click(identity_proof_type_location)
    time.sleep(0.2)
    print(idType)
    if idType.lower() == 'aadhar card':
        autoit.send("aad")
    elif idType.lower() == 'pan card':
        autoit.send("pan")
    elif idType.lower() == 'driving license':
        autoit.send("d")
    elif idType.lower() == 'passport':
        autoit.send("pas")
        print("sent pas")
    elif idType.lower() == 'student id card':
        autoit.send("s")

    time.sleep(0.1)
    autoit.send("{ENTER}")

    # if nationalityDropDownDisplayed():
    #     if country.lower() != "india":
    #         autoit.send("{ENTER}")
    # time.sleep(0.25)
    # autoit.send("{TAB}")
    # autoit_slow_type_numbers_with_error(idNumber)
    id_details_location = pyautogui.locateOnScreen(id_details_image_path, region=region, confidence=0.7)
    wait_for_alt_q()
    # Mouse movement
    move_mouse_to_center(id_details_location)

    pyautogui.click(id_details_location)
    #typing_text_with_random_delays_IDNumber(idNumber, currentPerson, random_numbers2)
    #type_text(idNumber.lower())
    human_typing(idNumber.lower())

    age_location = pyautogui.locateOnScreen(age_image_path, region=region, confidence=0.9)
    wait_for_alt_q()
    # Mouse movement
    print("Mouse movement for age for person no " + str(currentPerson))
    move_mouse_to_center(age_location)
    pyautogui.click(age_location)
    human_typing_other(age)
    time.sleep(random.uniform(0.05, 1))
    if machine == "laptop" and currentPerson >= 4:
        autoit.send("{TAB}")


def custom_hotkey():
    # Define your desired hotkey combination
    return keyboard.is_pressed("ctrl+alt+x")  # Example: Ctrl+Alt+X


def debounce_key(key):
    # Wait for key release
    while keyboard.is_pressed(key):
        pass


def firstPageFill():
    # Call the function to wait for the image and click on it
    # location = wait_for_image_and_click(ok_image_path)
    # if allForeigners():
    #     pyautogui.click(find_image_on_screen_using_opencv_and_click(iamforeigner_image_path, 2))
    #
    # else:
    #     pyautogui.click(find_image_on_screen_using_opencv_and_click(iamIndian_image_path, 2))
    pyautogui.click(find_image_on_screen_using_opencv(ok_image_path, 600))

    speed_for_first_page(speed_first_page)

    pyautogui.click(find_image_on_screen_using_opencv(ReservationsFor_image_path, 10))

    # two tabs to open the checkin date
    autoit.send("{TAB 2}")

    time.sleep(0.2)

    # Next Month Handling for checkInDate
    print(days_difference_with_checkInDate(checkInDate))
    multiplePressUsingPyAutoGUI('right', days_difference_with_checkInDate(checkInDate))
    # autoit.send("{RIGHT 31}")

    time.sleep(0.1)

    # Press hotkey to select checkin
    pyautogui.hotkey('alt', 'i')

    speed_for_first_page(speed_first_page)

    # Press enter
    autoit.send("{ENTER}")

    speed_for_first_page(speed_first_page)

    # one tab to open the checkout date
    autoit.send("{TAB}")

    time.sleep(0.2)

    # Next Month Handling for checkInDate
    print(days_difference_with_checkInDate_checkOutDate(checkInDate, checkOutDate))
    multiplePressUsingPyAutoGUI('right', days_difference_with_checkInDate_checkOutDate(checkInDate, checkOutDate))

    time.sleep(0.1)

    # Press hotkey to select checkout date
    pyautogui.hotkey('alt', 'o')

    speed_for_first_page(speed_first_page)

    # Press enter
    autoit.send("{ENTER}")

    speed_for_first_page(speed_first_page)

    # one tab to select rooms
    autoit.send("{TAB}")

    speed_for_first_page(speed_first_page)

    # select the number of rooms
    autoit.send(number_of_rooms)

    speed_for_first_page(speed_first_page)

    # one tab to open the adults dropdown
    autoit.send("{TAB}")

    speed_for_first_page(speed_first_page)

    # one tab to select Adults
    autoit.send(number_of_adults)

    speed_for_first_page(speed_first_page)

    # one tab to open the children dropdown
    autoit.send("{TAB}")

    speed_for_first_page(speed_first_page)

    # one tab to select children
    autoit.send(number_of_children)

    speed_for_first_page(speed_first_page)

    if int(number_of_adults) >= 1:
        # one tab to open the pax1 dropdown and select
        autoit.send("{TAB}")
        selectPaxDropdown(pax_1.lower())

    speed_for_first_page(speed_first_page)

    # one tab to open the pax2 dropdown and select
    if int(number_of_adults) >= 2:
        # one tab to open the pax1 dropdown and select
        autoit.send("{TAB}")
        selectPaxDropdown(pax_2.lower())

    speed_for_first_page(speed_first_page)

    # one tab to open the pax3 dropdown and select
    if int(number_of_adults) >= 3:
        # one tab to open the pax1 dropdown and select
        autoit.send("{TAB}")
        selectPaxDropdown(pax_3.lower())

    speed_for_first_page(speed_first_page)

    # one tab to open the pax4 dropdown and select
    if int(number_of_adults) >= 4:
        # one tab to open the pax1 dropdown and select
        autoit.send("{TAB}")
        selectPaxDropdown(pax_4.lower())

    speed_for_first_page(speed_first_page)

    # one tab to open the pax5 dropdown and select
    if int(number_of_adults) >= 5:
        # one tab to open the pax1 dropdown and select
        autoit.send("{TAB}")
        selectPaxDropdown(pax_5.lower())

    speed_for_first_page(speed_first_page)

    # one tab to open the pax6 dropdown and select
    if int(number_of_adults) >= 6:
        # one tab to open the pax1 dropdown and select
        autoit.send("{TAB}")
        selectPaxDropdown(pax_6.lower())

    speed_for_first_page(speed_first_page)

    # tab and enter
    autoit.send("{TAB}")

    speed_for_first_page(speed_first_page)

    multiplePressUsingPyAutoGUI('down', 2)

    speed_for_first_page(speed_first_page)

    autoit.send("{ENTER}")

    locationOfRooms = find_image_on_screen_using_opencv(rooms_image_path, 10)

    print("Rooms was displayed here -->" + str(locationOfRooms))
    print("Rooms selection process can be started now")


def find_image_on_screen_using_opencv(template_path1, timeout, threshold=0.7):
    template = cv2.imread(template_path1, 0)
    w, h = template.shape[::-1]
    start_time = time.time()

    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to numpy array and then to grayscale
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if the match value is above the threshold
        if max_val >= threshold:
            # Return the location of the matched region
            return max_loc[0], max_loc[1], w, h

        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            return None

        time.sleep(0.5)


def find_image_on_screen_using_opencv_in_region(template_path1, timeout, region, threshold=0.7):
    template = cv2.imread(template_path1, 0)
    w, h = template.shape[::-1]
    start_time = time.time()

    while True:
        # Capture a screenshot of the specified region
        screenshot = pyautogui.screenshot(region=region)

        # Convert screenshot to numpy array and then to grayscale
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if the match value is above the threshold
        if max_val >= threshold:
            # Calculate the absolute position of the matched region
            abs_x = max_loc[0] + region[0]
            abs_y = max_loc[1] + region[1]
            return abs_x, abs_y, w, h

        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            return None


def enterMobile():
    # multiplePressUsingPyAutoGUI('tab', 3)
    wait_for_alt_q()
    time.sleep(0.1)
    mobile_location = pyautogui.locateOnScreen(mobile_image_path, confidence=0.7)
    pyautogui.click(mobile_location)
    human_typing(mobileNumber)
    time.sleep(0.1)
    multiplePressUsingPyAutoGUI('tab', 1)
    time.sleep(0.2)
    multiplePressUsingPyAutoGUI('enter', 1)


def payment():
    location = find_image_on_screen_using_opencv(SelectPaymentOption_image_path, 300)
    pyautogui.click(location)
    if paymentMethod == "upi" or paymentMethod == "upi_id":
        location2 = find_image_on_screen_using_opencv(UPI_image_path, 60)
        pyautogui.click(location2)
        print("clicked on UPI")
        # location3 = find_image_on_screen_using_opencv(PayNow_image_path, 60)
        # pyautogui.click(location3)
        time.sleep(0.1)
        autoit.send("{TAB}")
        time.sleep(0.1)
        autoit.send("{ENTER}")
        print("clicked on Pay Now button")
        find_any_of_two_images_on_screen_using_opencv(contactdetails_image_path, tiger_image_path, 600)
        time.sleep(0.5)
        result2 = find_any_of_two_images_on_screen_using_opencv(contactdetails_image_path, tiger_image_path, 60)
        print(str(result2))
        image_name, x_image, y_image, w_image, h_image = result2
        location4 = int(x_image), int(y_image), w_image, h_image

        if image_name == "Image 1":
            print("Image 1 was displayed")
            pyautogui.click(location4)
            autoit.send("{TAB}")
            time.sleep(0.1)
            autoit.send("{TAB}")
            time.sleep(0.1)
            autoit.send("{TAB}")
            time.sleep(0.1)
            # autoit.send(emailAddress)
            human_typing(emailAddress)
            time.sleep(0.2)
            autoit.send("{TAB}")
            autoit.send("{ENTER}")
            if paymentMethod == "upi":
                location6 = find_image_on_screen_using_opencv(showQR_image_path, 10)
                print("show QR was displayed")
                pyautogui.click(location6)
                location6b = find_image_on_screen_using_opencv(recommended_image_path, 10)
                pyautogui.click(location6b)
            elif paymentMethod == "upi_id":
                location6 = find_image_on_screen_using_opencv(UPI_ID_image_path, 10)
                print("UPI_ID was displayed")
                pyautogui.click(location6)
                time.sleep(0.1)
                location7 = find_image_on_screen_using_opencv(UPI_Number_FirstImage_image_path, 10)
                pyautogui.click(location7)
                # autoit.send("{TAB}")
                time.sleep(0.1)
                autoit.send("{TAB}")
                time.sleep(0.1)
                pyautogui.typewrite(UPI_ADDRESS)
                time.sleep(0.25)
                autoit.send("{TAB}")
                time.sleep(0.1)
                autoit.send("{ENTER}")

        elif image_name == "Image 2":
            print("Image 2 was displayed")
            pyautogui.click(location4)
            autoit.send("{TAB}")
            time.sleep(0.1)
            autoit.send("{TAB}")
            time.sleep(0.1)
            autoit.send("{TAB}")
            time.sleep(0.1)
            # autoit.send(emailAddress)
            human_typing(emailAddress)
            location5 = find_image_on_screen_using_opencv(proceedAfterTiger_image_path, 10)
            pyautogui.click(location5)
            location6 = find_image_on_screen_using_opencv(UPIQR_AfterTiger_image_path, 10)
            pyautogui.click(location6)
            if paymentMethod == "upi":
                location6b = find_image_on_screen_using_opencv(showQR_AfterTiger_image_path, 10)
                pyautogui.click(location6b)
            elif paymentMethod == "upi_id":
                location6b = find_image_on_screen_using_opencv(UPI_ID_Image2_image_path, 10)
                pyautogui.click(location6b)
                time.sleep(0.25)
                # pyautogui.typewrite(UPI_ADDRESS)
                # autoit.send(UPI_ADDRESS)
                human_typing(UPI_ADDRESS)
                time.sleep(0.1)
                autoit.send("{TAB}")
                time.sleep(0.1)
                autoit.send("{ENTER}")

    elif paymentMethod == "creditcard":
        location7 = find_image_on_screen_using_opencv(creditcard_image_path, 10)
        pyautogui.click(location7)
        # location8 = find_image_on_screen_using_opencv(PayNow_image_path, 10)
        # pyautogui.click(location8)
        time.sleep(0.1)
        autoit.send("{TAB}")
        time.sleep(0.1)
        autoit.send("{ENTER}")
        print("clicked on Pay Now button")
        location9 = find_image_on_screen_using_opencv(contactdetails_image_path, 20)
        time.sleep(1)
        pyautogui.click(location9)
        autoit.send("{TAB}")
        time.sleep(0.1)
        autoit.send("{TAB}")
        time.sleep(0.1)
        autoit.send("{TAB}")
        time.sleep(0.1)
        human_typing(emailAddress)
        location10 = find_image_on_screen_using_opencv(continue_image_path, 10)
        pyautogui.click(location10)
        location11 = find_image_on_screen_using_opencv(payViaCard_image_path, 10)
        pyautogui.click(location11)
        location12 = find_image_on_screen_using_opencv(addANewCard_image_path, 10)
        pyautogui.click(location12)
        autoit.send("{TAB}")
        time.sleep(0.1)
        human_typing(card_number)
        time.sleep(0.1)
        autoit.send("{TAB}")
        human_typing(Month)
        time.sleep(0.05)
        human_typing(Year)
        time.sleep(0.05)
        autoit.send("{TAB}")
        human_typing(CVV)
        time.sleep(0.05)
        autoit.send("{TAB}")
        human_typing(NameOnCard)
        time.sleep(0.1)
        location12 = find_image_on_screen_using_opencv(continue_image_path, 10)
        pyautogui.click(location12)


def setImagePath():
    global image_directory
    if machine == "laptop" or machine == "pradeeplaptop":
        image_directory = os.getcwd() + '\\images_laptop'
    elif machine == "desktop" or machine == "rohit":
        image_directory = os.getcwd() + '\\images_desktop'

    global ok_image_path
    ok_image_path = os.path.join(image_directory, 'ok.png')

    global firstPersonText_image_path
    firstPersonText_image_path = os.path.join(image_directory, 'firstpersonText.png')

    global firstPersonText_image_path2
    firstPersonText_image_path2 = os.path.join(image_directory, 'firstpersonText2.png')

    global identity_proof_type_image_path
    identity_proof_type_image_path = os.path.join(image_directory, 'identity_proof_type.png')

    global iamforeigner_image_path
    iamforeigner_image_path = os.path.join(image_directory, 'iamforeigner.png')

    global iamIndian_image_path
    iamIndian_image_path = os.path.join(image_directory, 'iamIndian.png')

    global ReservationsFor_image_path
    ReservationsFor_image_path = os.path.join(image_directory, 'ReservationsFor.png')

    global success_image_path
    success_image_path = os.path.join(image_directory, 'success.png')

    global indian_flag_image_path
    indian_flag_image_path = os.path.join(image_directory, 'indian_flag.png')

    global SelectPaymentOption_image_path
    SelectPaymentOption_image_path = os.path.join(image_directory, 'SelectPaymentOption.png')

    global UPI_image_path
    UPI_image_path = os.path.join(image_directory, 'UPI.png')

    global PayNow_image_path
    PayNow_image_path = os.path.join(image_directory, 'PayNow.png')

    global email_image_path
    email_image_path = os.path.join(image_directory, 'email.png')

    global continue_image_path
    continue_image_path = os.path.join(image_directory, 'continue.png')

    global contactdetails_image_path
    contactdetails_image_path = os.path.join(image_directory, 'contactdetails.png')

    global showQR_image_path
    showQR_image_path = os.path.join(image_directory, 'showQR.png')

    global recommended_image_path
    recommended_image_path = os.path.join(image_directory, 'recommended.png')

    global creditcard_image_path
    creditcard_image_path = os.path.join(image_directory, 'credit_debit_card.png')

    global payViaCard_image_path
    payViaCard_image_path = os.path.join(image_directory, 'payViaCard.png')

    global addANewCard_image_path
    addANewCard_image_path = os.path.join(image_directory, 'addANewCard.png')

    global rooms_image_path
    rooms_image_path = os.path.join(image_directory, 'rooms.png')

    global tiger_image_path
    tiger_image_path = os.path.join(image_directory, 'tiger.png')

    global proceedAfterTiger_image_path
    proceedAfterTiger_image_path = os.path.join(image_directory, 'proceedAfterTiger.png')

    global UPIQR_AfterTiger_image_path
    UPIQR_AfterTiger_image_path = os.path.join(image_directory, 'UPIQR_AfterTiger.png')

    global showQR_AfterTiger_image_path
    showQR_AfterTiger_image_path = os.path.join(image_directory, 'showQR_AfterTiger.png')

    global UPI_ID_image_path
    UPI_ID_image_path = os.path.join(image_directory, 'UPI_ID.png')

    global UPI_ID_Image2_image_path
    UPI_ID_Image2_image_path = os.path.join(image_directory, 'UPI_ID_Image2.png')

    global UPI_Number_FirstImage_image_path
    UPI_Number_FirstImage_image_path = os.path.join(image_directory, 'UPI_Number_FirstImage.png')

    global gender_dropdown_image_path
    gender_dropdown_image_path = os.path.join(image_directory, 'gender_dropdown.png')

    global id_details_image_path
    id_details_image_path = os.path.join(image_directory, 'id_details.png')

    global age_image_path
    age_image_path = os.path.join(image_directory, 'age.png')

    global fullname_image_path
    fullname_image_path = os.path.join(image_directory, 'fullname.png')

    global mobile_image_path
    mobile_image_path = os.path.join(image_directory, 'mobile.png')


def check_current_month(checkInDatePassed):
    input_month = datetime.strptime(checkInDatePassed, "%Y-%m-%d").month
    current_month = datetime.now().month
    return input_month == current_month


def days_difference_with_checkInDate(checkOutDate1):
    # Define the dates
    current_date = datetime.now()
    compare_date = datetime(2024, 11, 15)

    # Get the higher date
    higher_date = max(current_date, compare_date)

    # Parse checkOutDate
    checkOutDate1 = datetime.strptime(checkOutDate1, "%Y-%m-%d")

    # Calculate the difference in days
    difference_in_days = abs((checkOutDate1 - higher_date).days)
    return difference_in_days + 1


def days_difference_with_checkInDate_checkOutDate(checkInDate1, checkOutDate1):
    # Convert strings to datetime objects if they aren't already
    if isinstance(checkInDate1, str):
        checkInDate1 = datetime.strptime(checkInDate1, "%Y-%m-%d")
    if isinstance(checkOutDate1, str):
        checkOutDate1 = datetime.strptime(checkOutDate1, "%Y-%m-%d")

    # Calculate the difference in days and ensure it's positive
    difference_in_days = abs((checkOutDate1 - checkInDate1).days) - 1
    return difference_in_days


import cv2
import pyautogui
import time


def find_any_of_two_images_on_screen_using_opencv(template_path1, template_path2, timeout, threshold=0.7):
    template1 = cv2.imread(template_path1, 0)
    template2 = cv2.imread(template_path2, 0)
    w1, h1 = template1.shape[::-1]
    w2, h2 = template2.shape[::-1]
    start_time = time.time()

    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()
        # Convert screenshot to numpy array and then to grayscale
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # Perform template matching for the first image
        res1 = cv2.matchTemplate(screenshot, template1, cv2.TM_CCOEFF_NORMED)
        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)

        # Perform template matching for the second image
        res2 = cv2.matchTemplate(screenshot, template2, cv2.TM_CCOEFF_NORMED)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)

        # Check if the first image match value is above the threshold
        if max_val1 >= threshold:
            # Take action for the first image
            return ("Image 1", max_loc1[0], max_loc1[1], w1, h1)

        # Check if the second image match value is above the threshold
        if max_val2 >= threshold:
            # Take action for the second image
            return ("Image 2", max_loc2[0], max_loc2[1], w2, h2)

        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            return None

        time.sleep(0.1)


def roomSelection():
    speed_for_first_page(speed_first_page)
    autoit.send("{F3}")
    time.sleep(0.1)
    print(room)
    autoit.send(room)
    time.sleep(0.1)
    autoit.send("{ESC}")
    time.sleep(0.2)
    autoit.send("{TAB}")
    time.sleep(0.1)
    autoit.send("{ENTER}")


def find_image_in_region(left, top, width, height, image):
    # Define the region of interest (left, top, width, height)
    region = (left, top, width, height)
    # Print debug information
    print(f"Capturing screenshot of region: {region}")

    # Capture a screenshot of the region
    screenshot = pyautogui.screenshot(region=region)

    # Print debug information
    print(f"Searching for image '{image}' within the captured region...")

    try:
        # Locate the image within the specified region on the screen
        image_location = pyautogui.locateOnScreen(image, region=region)

        if image_location is not None:
            # Get the center of the image location
            center = pyautogui.center(image_location)
            print(f"Image found at {center}")
            return center
        else:
            print("Image not found in the specified region.")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def move_and_click_image(image_path, confidence=0.7, duration=0.0, left=0, top=0, width=0, height=0):
    # Locate the image on the screen
    # location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    # location = find_image_on_screen_using_opencv(image_path, 10)
    location = find_image_in_region(left, top, width, height, image_path)
    print(location)
    if location is not None:
        # Move the mouse smoothly to the target location
        # pyautogui.moveTo(location.x, location.y, duration=duration)
        pyautogui.moveTo(location.x, location.y, 0.0)
        # Perform the click
        pyautogui.click()
        return True
    else:
        print("Image not found on the screen.")
        return False


def wait_for_alt_q():
    print("Waiting for 'Alt + Q' to be pressed...")
    # Block until "Alt + Q" is pressed
    keyboard.wait('alt+q')
    print("'Alt + Q' was pressed!")


def type_character(char):
    if char.isalnum():  # Check if character is alphanumeric
        pyautogui.press(char)
    else:
        if char == ' ':
            pyautogui.press('space')
        elif char == '\n':
            pyautogui.press('enter')


def type_text(text):
    for char in text:
        type_character(char)
        # Simulate random delay between key presses
        # time.sleep(random_number_between_min_and_max(10, 30) / 1000.0)
        # time.sleep(random_number_between_min_and_max(45, 70) / 1000.0)
        time.sleep(random.uniform(0.05, 0.20))


def move_mouse_to_center(gender_dropdown_location, duration=0.2):
    center_x = gender_dropdown_location.left + gender_dropdown_location.width / 2
    center_y = gender_dropdown_location.top + gender_dropdown_location.height / 2
    pyautogui.moveTo(center_x, center_y, duration=duration)
    print(f"Mouse moved to ({center_x}, {center_y}).")
