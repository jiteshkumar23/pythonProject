import pyautogui


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
        "Loghut-Dhikala": ("alt", "9"),
        "Bijrani FRH-Single Bed": ("alt", "p")
        # Add more room priorities here
    }

    keys = key_mapping.get(room_priority, None)
    if keys:
        print(f"roomPriority selected is {room_priority}")
        print(f"Keys pressed for {room_priority} are : {keys[0]} + {keys[1]}")
        pyautogui.hotkey(*keys)
    else:
        print("Invalid roomPriority")
