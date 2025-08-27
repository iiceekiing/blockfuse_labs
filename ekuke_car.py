import time

car_name = input("""
                 🚗 Welcome to Ice Car Collection.
                 Enter the name of your car: 
                 """)

car_isOn = False 

while True:
    option = input("""
    Select any option below to perform corresponding action.
    _________________________________
    |   1. 'start' to start your car. |
    |---------------------------------|
    |   2. 'D' to drive.              |
    |---------------------------------|
    |   3. 'R' to reverse.            |
    |   4. 'P' to park.               |
    |   5. 'off' to turn off your car.|
    |_________________________________|
     \n>>> """).lower()

    if option == "start" and car_isOn:
        print("Turning on car...")
        time.sleep(2)
        print("Car is now ON!")
        car_isOn = True

    elif option == "start" and car_isOn:
        print("⚠️ Car is already ON!")

    elif option == "d" and car_isOn:
        print("�� Driving forward...")

    elif option == "r" and car_isOn:
        print("↩️ Reversing...")

    elif option == "p" and car_isOn:
        print("🅿️ Car is parked.")

    elif option == "off" and car_isOn:
        print("🛑 Turning off car...")
        time.sleep(2)
        print("❌ Car is now OFF.")
        car_isOn = False

    elif option == "off" and not car_isOn:
        print("⚠️ Car is already OFF.")

    else:
        print("❓ Invalid option or car must be started first.")

