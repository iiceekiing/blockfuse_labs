import time

car_name = input("""
                 🚗 Welcome to Ice Car Collection.
                 Enter the name of your car: 
                 \n""")

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
    |   6. 'quit' to exit program.    |
    |_________________________________|
    >>> """).lower()

    # ---- MAIN MENU ----
    if option == "start" and not car_isOn:
        print("🔑 Turning on car...")
        time.sleep(1)
        print("✅ Car is now ON!")
        car_isOn = True

        # ---- DRIVING MENU ----
        while car_isOn:
            command = input(""" 
                   Select Drive Option Below:
                   --------------------------
                   1. 'D' to drive forward
                   2. 'R' to reverse
                   3. 'P' to park
                   4. 'off' to turn off car
                   5. 'exit' to return to Main Menu
                   >>> """).lower()

            if command == "d":
                print("🚙 Driving forward...")
            elif command == "r":
                print("↩️ Reverse gear engaged, driving backward...")
            elif command == "p":
                print("🅿️ Car is parked.")
            elif command == "off":
                print("🛑 Turning off car engine...")
                time.sleep(1)
                print("❌ Car is now OFF.")
                car_isOn = False
            elif command == "exit":
                print("↩️ Returning to Main Menu...")
                break
            else:
                print("⚠️ Invalid command. Try again.")

    elif option == "start" and car_isOn:
        print("⚠️ Car is already ON!")

    elif option == "d" or option == "r" or option == "p":
        if not car_isOn:
            print("⚠️ You need to START the car first!")
        else:
            print("✅ Please use the driving menu when the car is ON.")

    elif option == "off":
        if not car_isOn:
            print("⚠️ Car is already OFF.")
        else:
            print("🛑 Turning off car...")
            time.sleep(1)
            print("❌ Car is now OFF.")
            car_isOn = False

    elif option == "quit":
        print("�� Exiting program. Goodbye!")
        break

    else:
        print("❓ Invalid option, please try again.")

