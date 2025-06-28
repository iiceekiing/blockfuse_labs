#!/bin/bash

echo "AVAILABLE COMMANDS"
echo "start: to start your car"
echo "stop: to stop car engine"
echo "exit: to quit execution"
echo "-help: to display available commands"
echo "enter the name of your car"
read car

#read -p "Enter the name of your favourite car to start cruising:  " car
echo "very good taste to pick $car"

SHOULD_EXECUTE=true
ENGINE_IS_ON=false
DRIVE=false
PARKED=false
REVERSE=false

while $SHOULD_EXECUTE;
do
    echo -n "Enter Command: "
    read COMMAND

    if [[ $COMMAND == "start" && $ENGINE_IS_ON == false ]]; then
        ENGINE_IS_ON=true
        echo "🚗 Starting your $car..."
        echo "✅ your $car is now ON"

        echo ""
        echo "⚙️ Select Drive Option:"
        echo "D: to drive forward"
        echo "P: to park"
        echo "R: to reverse"

    elif [[ $COMMAND == "start" && $ENGINE_IS_ON == true ]]; then
        echo "⚠️ Engine is Already ON"

    elif [[ $COMMAND == "stop" && $ENGINE_IS_ON == false ]]; then
        echo "⚠️ Engine is Already OFF"

    elif [[ $COMMAND == "stop" && $ENGINE_IS_ON == true ]]; then
        ENGINE_IS_ON=false
        echo "🛑 Stopping engine..."
        echo "✅ Engine is now OFF"

    elif [[ $COMMAND == "-help" ]]; then
        echo "AVAILABLE COMMANDS"
        echo "start: to start engine"
        echo "stop: to stop engine"
        echo "exit: to quit execution"
        echo "-help: to display available commands"
        echo "D: to drive"
        echo "P: to park"
        echo "R: to reverse"

    elif [[ $COMMAND == "exit" ]]; then
        echo "👋 Goodbye!"
        SHOULD_EXECUTE=false

    elif [[ $ENGINE_IS_ON == true && $COMMAND == "D" ]]; then
        echo "🚘 Driving forward..."

    elif [[ $ENGINE_IS_ON == true && $COMMAND == "D" ]]; then
        echo "🚘 already driving, stop car to start driving again..."

    elif [[ $ENGINE_IS_ON == true && $COMMAND == "P" ]]; then
        echo "🅿️ Vehicle parked."

    elif [[ $ENGINE_IS_ON == true && $COMMAND == "R" ]]; then
        echo "🔄 Reversing vehicle..."

    elif [[ $ENGINE_IS_ON == false && ( $COMMAND == "D" || $COMMAND == "P" || $COMMAND == "R" ) ]]; then
        echo "⚠️ You need to start the engine first."

    elif [[ $COMMAND == "D" && $DRIVE == true ]]; then
	echo "car is already in drive mode, stop engine to start driving again!"

    else
        echo "❌ Invalid command. Type '-help' for assistance."
    fi
done

