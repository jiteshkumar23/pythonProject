import sys

import pyautogui
import time
import os
import logging
from datetime import datetime
from autoit import autoit

from CoreMethods import (autoit_slow_type_numbers_with_error, autoit_slow_type_with_error, get_user_input,
                         wait_for_image_and_click, human_typing, speed_for_first_page, nationalityDropDownDisplayed,
                         selectPaxDropdown, select_room_priority, fillForm)
from config import image_directory, speed_first_page, number_of_adults, pax_1, pax_2, pax_3, pax_4, pax_5, pax_6, \
    number_of_rooms, number_of_children, ok_image_path


def main():
    valueOfNationalityDropDownDisplayed = nationalityDropDownDisplayed()
    print(valueOfNationalityDropDownDisplayed)

    # Get user input before starting
    get_user_input()

    fillForm()
    #
    # # Call the function to wait for the image and click on it
    # location = wait_for_image_and_click(ok_image_path)
    # print(location)
    # # click on location of ok button again
    # pyautogui.click(location)
    #
    # speed_for_first_page(speed_first_page)
    #
    # # two tabs to open the checkin date
    # autoit.send("{TAB 2}")
    #
    # speed_for_first_page(speed_first_page)
    #
    # # Press hotkey to select checkin
    # # pyautogui.hotkey('shift', 'w')
    #
    # speed_for_first_page(speed_first_page)
    #
    # # Press enter
    # autoit.send("{ENTER}")
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to open the checkout date
    # autoit.send("{TAB}")
    #
    # speed_for_first_page(speed_first_page)
    #
    # # Press hotkey to select checkout date
    # # pyautogui.hotkey('shift', 'w')
    #
    # speed_for_first_page(speed_first_page)
    #
    # # Press enter
    # autoit.send("{ENTER}")
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to select rooms
    # autoit.send("{TAB}")
    #
    # speed_for_first_page(speed_first_page)
    #
    # # select the number of rooms
    # autoit.send(number_of_rooms)
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to open the adults dropdown
    # autoit.send("{TAB}")
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to select Adults
    # autoit.send(number_of_adults)
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to open the children dropdown
    # autoit.send("{TAB}")
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to select children
    # autoit.send(number_of_children)
    #
    # speed_for_first_page(speed_first_page)
    #
    # if int(number_of_adults) >= 1:
    #     # one tab to open the pax1 dropdown and select
    #     autoit.send("{TAB}")
    #     selectPaxDropdown(pax_1.lower())
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to open the pax2 dropdown and select
    # if int(number_of_adults) >= 2:
    #     # one tab to open the pax1 dropdown and select
    #     autoit.send("{TAB}")
    #     selectPaxDropdown(pax_2.lower())
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to open the pax3 dropdown and select
    # if int(number_of_adults) >= 3:
    #     # one tab to open the pax1 dropdown and select
    #     autoit.send("{TAB}")
    #     selectPaxDropdown(pax_3.lower())
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to open the pax4 dropdown and select
    # if int(number_of_adults) >= 4:
    #     # one tab to open the pax1 dropdown and select
    #     autoit.send("{TAB}")
    #     selectPaxDropdown(pax_4.lower())
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to open the pax5 dropdown and select
    # if int(number_of_adults) >= 5:
    #     # one tab to open the pax1 dropdown and select
    #     autoit.send("{TAB}")
    #     selectPaxDropdown(pax_5.lower())
    #
    # speed_for_first_page(speed_first_page)
    #
    # # one tab to open the pax6 dropdown and select
    # if int(number_of_adults) >= 6:
    #     # one tab to open the pax1 dropdown and select
    #     autoit.send("{TAB}")
    #     selectPaxDropdown(pax_6.lower())
    #
    # speed_for_first_page(speed_first_page)
    #
    # # tab and enter
    # autoit.send("{TAB}")
    # autoit.send("{ENTER}")
    #
    # speed_for_first_page(speed_first_page)
    # # sleep for 1 second
    # time.sleep(1)
    #
    # select_room_priority("Bijrani")
    #
    # time.sleep(1)
    #
    # # Takes you to top of page very fast
    # autoit.send("{HOME}")
    #
    # # fillForm()
    #


if __name__ == "__main__":
    main()
