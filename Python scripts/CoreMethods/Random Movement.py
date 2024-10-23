import pyautogui
import random
import time


def random_mouse_move(duration):
    width, height = pyautogui.size()  # Get the screen size

    for _ in range(duration):
        x = random.randint(0, width)  # Random x-coordinate
        y = random.randint(0, height)  # Random y-coordinate
        pyautogui.moveTo(x, y, duration=0.2)  # Move the mouse to the coordinates
        time.sleep(0.2)  # Wait a bit before the next move


def draw_random_shape():
    width, height = pyautogui.size()  # Get screen size
    num_sides = random.randint(3, 8)  # Choose a random number of sides between 3 and 8
    side_length = random.randint(50, 150)  # Random length for the sides
    angle = 360 / num_sides  # Calculate the angle for the shape

    start_x = random.randint(0, width - side_length)
    start_y = random.randint(0, height - side_length)
    pyautogui.moveTo(start_x, start_y)

    for _ in range(num_sides):
        pyautogui.dragRel(side_length, 0, duration=0.5)  # Move right
        pyautogui.dragRel(0, side_length, duration=0.5)  # Move down
        pyautogui.moveRel(0, -side_length, duration=0.2)  # Move up
        pyautogui.moveRel(-side_length, 0, duration=0.2)  # Move left
        pyautogui.dragRel(int(side_length * random.uniform(-1, 1)), int(side_length * random.uniform(-1, 1)),
                          duration=0.5)  # Move randomly to add shape variation


# Example usage:
duration = 2  # Duration for random movement
draw_random_shape()  # Draw a random shape
random_mouse_move(duration)  # Perform random mouse movement
