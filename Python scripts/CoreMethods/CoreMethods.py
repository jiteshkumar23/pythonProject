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

from config import delay_correct, delay_error, pax_1, pax_2, pax_3, pax_4, pax_5, pax_6, \
    number_of_adults, nameOfSecondPerson, genderOfSecondPerson, \
    idNumberOfFirstPerson, idTypeOfFirstPerson, idTypeOfSecondPerson, idNumberOfSecondPerson, nameOfFirstPerson, \
    genderOfFirstPerson, countrySecondPerson, countryFirstPerson, ageOfFirstPerson, ageOfSecondPerson, \
    nameOfThirdPerson, genderOfThirdPerson, countryThirdPerson, idTypeOfThirdPerson, idNumberOfThirdPerson, \
    ageOfThirdPerson, nameOfFourthPerson, genderOfFourthPerson, countryFourthPerson, idTypeOfFourthPerson, \
    idNumberOfFourthPerson, ageOfFourthPerson, nameOfFifthPerson, genderOfFifthPerson, countryFifthPerson, \
    idTypeOfFifthPerson, idNumberOfFifthPerson, ageOfFifthPerson, nameOfSixthPerson, genderOfSixthPerson, \
    countrySixthPerson, idTypeOfSixthPerson, idNumberOfSixthPerson, ageOfSixthPerson, speed_first_page, \
    number_of_children, number_of_rooms, \
    room, mobileNumber, emailAddress, paymentMethod, card_number, Month, Year, CVV, NameOnCard, machine

from room_shortcuts import select_room_priority

global fifth
fifth = False

global image_directory, ok_image_path, firstPersonText_image_path, firstPersonText_image_path2, \
    identity_proof_type_image_path, iamforeigner_image_path, iamIndian_image_path, \
    ReservationsFor_image_path, success_image_path, indian_flag_image_path, \
    SelectPaymentOption_image_path, UPI_image_path, PayNow_image_path, email_image_path, \
    continue_image_path, contactdetails_image_path, showQR_image_path, \
    recommended_image_path, creditcard_image_path, payViaCard_image_path, \
    addANewCard_image_path,rooms_image_path

global indiaFlagX, identityDropDownX, Y1, Y2, Y3, Y4, Y5, Y6


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


def human_typing(text):
    for char in text:
        autoit.send(char)
        time.sleep(delay_correct)


def human_typing_age(text):
    for char in text:
        autoit.send(char)
        time.sleep(delay_correct + 0.1)


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


def fillForm():
    global fifth
    global indiaFlagX, identityDropDownX, Y1, Y2, Y3, Y4, Y5, Y6
    print("Machine being used is " + machine)
    if machine == "laptop":
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

    time.sleep(1.25)
    autoit.send("{HOME}")
    autoit.send("{HOME}")


    if int(number_of_adults) >= 1:
        location2 = find_image_on_screen_using_opencv(firstPersonText_image_path, 10)
        pyautogui.click(location2)

        fillPersonDetail(nameOfFirstPerson, genderOfFirstPerson, countryFirstPerson, indiaFlagX, Y1, identityDropDownX,
                         Y1,
                         idTypeOfFirstPerson,
                         idNumberOfFirstPerson, ageOfFirstPerson)

    if int(number_of_adults) >= 2:
        fillPersonDetail(nameOfSecondPerson, genderOfSecondPerson, countrySecondPerson, indiaFlagX, Y2,
                         identityDropDownX, Y2,
                         idTypeOfSecondPerson,
                         idNumberOfSecondPerson, ageOfSecondPerson)
    if int(number_of_adults) >= 3:

        fillPersonDetail(nameOfThirdPerson, genderOfThirdPerson, countryThirdPerson, indiaFlagX, Y3, identityDropDownX,
                         Y3,
                         idTypeOfThirdPerson, idNumberOfThirdPerson, ageOfThirdPerson)
    if int(number_of_adults) >= 4:
        fillPersonDetail(nameOfFourthPerson, genderOfFourthPerson, countryFourthPerson, indiaFlagX, Y4,
                         identityDropDownX, Y4,
                         idTypeOfFourthPerson, idNumberOfFourthPerson, ageOfFourthPerson)

    if int(number_of_adults) >= 5:
        fifth = True
        fillPersonDetail(nameOfFifthPerson, genderOfFifthPerson, countryFifthPerson, indiaFlagX, Y5, identityDropDownX,
                         Y5,
                         idTypeOfFifthPerson, idNumberOfFifthPerson, ageOfFifthPerson)

    if int(number_of_adults) >= 6:
        # fifth = False
        fillPersonDetail(nameOfSixthPerson, genderOfSixthPerson, countrySixthPerson, indiaFlagX, Y6, identityDropDownX,
                         Y6,
                         idTypeOfSixthPerson, idNumberOfSixthPerson, ageOfSixthPerson)


def fillPersonDetail(name, gender, country, indiaX, indiaY, identityProofX, identityProofY, idType, idNumber, age):
    autoit.send("{TAB}")
    if fifth:
        time.sleep(0.5)
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
            # autoit.send(country)
            time.sleep(0.5)
            autoit.send("{ESC}")
            # Wait for a moment before pressing Enter
            time.sleep(0.2)
            # Press Enter key
            autoit.send("{ENTER}")
            time.sleep(0.5)
            pyautogui.click(identityProofX, identityProofY)
        else:
            time.sleep(0.25)
            autoit.send("{TAB}")
    else:
        autoit.send("{TAB}")
        time.sleep(0.25)

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
    human_typing_age(age)


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

    # Press hotkey to select checkin
    pyautogui.hotkey('alt', 'i')

    speed_for_first_page(speed_first_page)

    # Press enter
    autoit.send("{ENTER}")

    speed_for_first_page(speed_first_page)

    # one tab to open the checkout date
    autoit.send("{TAB}")

    time.sleep(0.2)

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

    speed_for_first_page(speed_first_page)

    locationOfRooms = find_image_on_screen_using_opencv(rooms_image_path, 30)

    print("Rooms was displayed here -->"+str(locationOfRooms))

    select_room_priority(room)

    time.sleep(0.5)



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

def enterMobile():
    multiplePressUsingPyAutoGUI('tab', 3)
    human_typing(mobileNumber)
    time.sleep(0.1)
    multiplePressUsingPyAutoGUI('tab', 1)
    time.sleep(0.1)
    multiplePressUsingPyAutoGUI('enter', 1)


def payment():
    location = find_image_on_screen_using_opencv(SelectPaymentOption_image_path, 120)
    pyautogui.click(location)
    if paymentMethod == "upi":
        location2 = find_image_on_screen_using_opencv(UPI_image_path, 10)
        pyautogui.click(location2)
        location3 = find_image_on_screen_using_opencv(PayNow_image_path, 10)
        pyautogui.click(location3)
        location4 = find_image_on_screen_using_opencv(contactdetails_image_path, 20)
        time.sleep(1)
        pyautogui.click(location4)
        autoit.send("{TAB}")
        time.sleep(0.1)
        autoit.send("{TAB}")
        time.sleep(0.1)
        autoit.send("{TAB}")
        time.sleep(0.1)
        autoit.send(emailAddress)
        location5 = find_image_on_screen_using_opencv(continue_image_path, 10)
        pyautogui.click(location5)
        location6 = find_image_on_screen_using_opencv(showQR_image_path, 10)
        pyautogui.click(location6)
        location6b = find_image_on_screen_using_opencv(recommended_image_path, 10)
        pyautogui.click(location6b)

    elif paymentMethod == "creditcard":
        location7 = find_image_on_screen_using_opencv(creditcard_image_path, 10)
        pyautogui.click(location7)
        location8 = find_image_on_screen_using_opencv(PayNow_image_path, 10)
        pyautogui.click(location8)
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
    print("Machine being used is " + machine)
    global image_directory
    if machine == "laptop":
        image_directory = os.getcwd() + '\\images_laptop'
    elif machine == "desktop":
        image_directory = os.getcwd() + '\\images_desktop'

    print("Picking this image directory -->" + image_directory)
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