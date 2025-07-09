#!/bin/bash

# Initial state
engine_on=false
speed=0
fuel=5
gear="P"

function status() {
  echo "==========================="
  echo "🚗 Engine: $( [ "$engine_on" = true ] && echo ON || echo OFF )"
  echo "🏁 Speed: ${speed} km/h"
  echo "⛽ Fuel: ${fuel}L"
  echo "⚙ Gear: $gear"
  echo "==========================="
}

function start_engine() {
  if [ "$engine_on" = true ]; then
    echo "⚠ Engine is already ON."
  elif [ "$fuel" -le 0 ]; then
    echo "❌ Cannot start engine. No fuel!"
  else
    engine_on=true
    echo "✅ Engine started."
  fi
}

function stop_engine() {
  if [ "$engine_on" = false ]; then
    echo "⚠ Engine is already OFF."
  else
    engine_on=false
    speed=0
    gear="P"
    echo "🛑 Engine stopped. Speed and gear reset."
  fi
}

function accelerate() {
  if [ "$engine_on" = false ]; then
    echo "❌ Start the engine first."
  elif [ "$fuel" -le 0 ]; then
    echo "⛽ Out of fuel!"
  elif [ "$gear" != "D" ]; then
    echo "⚠ You can only accelerate in Drive gear (D). Current gear: $gear"
  else
    speed=$((speed + 10))
    fuel=$((fuel - 1))
    echo "🚀 Accelerated! Speed: ${speed} km/h, Fuel left: ${fuel}L"
  fi
}

function brake() {
  if [ "$speed" -le 0 ]; then
    echo "🅿 Car already stopped."
  else
    speed=$((speed - 10))
    if [ "$speed" -lt 0 ]; then speed=0; fi
    echo "🛑 Braked. Speed now: ${speed} km/h"
  fi
}

function refuel() {
  read -p "⛽ How many liters to add? " add
  if [[ "$add" =~ ^[0-9]+$ ]]; then
    fuel=$((fuel + add))
    echo "✅ Refueled. Current fuel: ${fuel}L"
  else
    echo "❌ Invalid input. Please enter a number."
  fi
}

function shift_gear() {
  echo "Select gear:"
  echo "N - Neutral"
  echo "D - Drive"
  echo "R - Reverse"
  echo "P - Park"
  read -p "Enter gear (N/D/R/P): " new_gear
  new_gear=$(echo "$new_gear" | tr '[:lower:]' '[:upper:]') # convert to uppercase

  case "$new_gear" in
    N|D|R|P)
      gear="$new_gear"
      echo "✅ Gear shifted to $gear"
      ;;
    *)
      echo "❌ Invalid gear. Try again."
      ;;
  esac
}

# 🚦 Control loop
while true; do
  echo
  echo "Choose an action:"
  echo "1. Start Engine"
  echo "2. Stop Engine"
  echo "3. Accelerate"
  echo "4. Brake"
  echo "5. Refuel"
  echo "6. Shift Gear"
  echo "7. Show Status"
  echo "8. Quit"
  read -p "Enter choice [1-8]: " choice

  case $choice in
    1) start_engine ;;
    2) stop_engine ;;
    3) accelerate ;;
    4) brake ;;
    5) refuel ;;
    6) shift_gear ;;
    7) status ;;
    8) echo "👋 Exiting..."; break ;;
    *) echo "❌ Invalid option. Try again." ;;
  esac
done
