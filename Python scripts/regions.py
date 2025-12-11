from config import machine

# Region settings based on machine type
if machine == "laptop":
    region1 = (244, 254, 1410, 108)
    region2 = (244, 375, 1410, 109)
    region3 = (244, 505, 1410, 109)
    region4 = (244, 636, 1410, 109)
    region5 = (244, 767, 1410, 109)
    region6 = (244, 892, 1410, 109)
elif machine == "desktop":
    region1 = (110, 197, 1131, 91)
    region2 = (110, 298, 1131, 91)
    region3 = (110, 403, 1131, 91)
    region4 = (110, 508, 1131, 91)
    region5 = (110, 609, 1131, 91)
    region6 = (110, 370, 1131, 91)
elif machine == "rohit":
    region1 = (110, 197, 1131, 91)
    region2 = (110, 298, 1131, 91)
    region3 = (110, 403, 1131, 91)
    region4 = (110, 500, 1131, 91)
    region5 = (110, 354, 1131, 91)
    region6 = (110, 485, 1131, 91)
elif machine == "pradeeplaptop":
    region1 = (110, 197, 1131, 91)
    region2 = (110, 298, 1131, 91)
    region3 = (110, 403, 1131, 91)
    region4 = (110, 500, 1131, 91)
    region5 = (110, 354, 1131, 91)
    region6 = (110, 485, 1131, 91)