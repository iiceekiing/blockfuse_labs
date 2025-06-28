#!/bin/bash

echo "Welcome to BlockFuse Labs"
echo "Enter '-help' for help"
echo "Enter 'exit' to terminate program"

while true; do
    read -p "Please enter student score: " score

    # Exit condition
    if [[ "$score" == "exit" ]]; then
        echo "Goodbye!"
        break

    # Help command
    elif [[ "$score" == "-help" ]]; then
        echo "👉 Enter a number between 0 and 100 to get the grade."
        echo "👉 Type 'exit' to quit the program."
        continue

    # Not a number
    elif ! [[ "$score" =~ ^-?[0-9]+$ ]]; then
        echo "❌ Invalid input. Please enter a valid score (a number)."
        continue

    fi  # <-- This closes the 'elif' block above

    # Convert to number
    score=$((score))

    # Negative input
    if [ "$score" -lt 0 ]; then
        echo "⚠ Input is too low to be considered a score."
        continue

    # Over 100
    elif [ "$score" -gt 100 ]; then
        echo "🚫 This is a very useless input. Score must not be greater than 100."
        continue
    fi

    # Grading system
    if [ "$score" -ge 70 ]; then
        echo "✅ Grade: A"
    elif [ "$score" -ge 60 ]; then
        echo "✅ Grade: B"
    elif [ "$score" -ge 50 ]; then
        echo "✅ Grade: C"
    elif [ "$score" -ge 40 ]; then
        echo "✅ Grade: D"
    elif [ "$score" -ge 30 ]; then
        echo "✅ Grade: E"
    else
        echo "❌ Grade: F"
    fi
done
