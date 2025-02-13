import time

import pyautogui

time.sleep(5)  # Wait for 5 seconds (adjust as needed)

# Define the region of interest (left, top, width, height)
region = (251, 440, 1403, 142)

# Print debug information
print(f"Capturing screenshot of region: {region}")

# Capture a screenshot of the region
screenshot2 = pyautogui.screenshot(region=region)

# # Save the screenshot to a file
screenshot2.save('screenshot.png')
#
# print("Screenshot saved as 'screenshot.png'")

# Print debug information
print("Searching for image 'indian_flag.png' within the captured region...")

try:
    # Locate the image 'indian_flag.png' within the specified region on the screen
    image_location = pyautogui.locateOnScreen('firstpersonText.png', region=region)

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
