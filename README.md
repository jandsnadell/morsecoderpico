# morsecoderpico
My project of a morse code translator for a Raspberry Pi Pico.
# Required libraries
I am using my own libraries, blinkboard and morse.
# All parts
 This only requires a button (2 pin), a USB cable, two male to male wires, a breadboard, and a Pico.
# What it does
This project translates into morse code and blinks it with the onboard light. It also shows the morse code.
It also translates out of morse code using a button and a very simple circuit.
# Installation
(1) Download as ZIP

(2) Extract and take the UF2 file and put it on your Pico. (drive name RPI-RP2).

(3) The Pico will reboot and the new drive name should be CIRCUITPY.

(4) Open menu.py in your CircuitPython IDE of choice, and change the interpreter to CircuitPython.

(5) Go into menu.py, and find line 65. Change the GPIO pin number to the one you would like to use (in my case, GP22).

(6) Run once your circuit has been assembled.
# Circuit Assembly
(1) Put your breadboard on a desk, or any flat surface. 

(2) Take the two wires and put them in the breadboard on (VERY IMPORTANT) a GPIO pin, and a ground pin (shown as GND). 

(3) Wire up to the button with the two wires touching the two pins. Find a way to get them mounted (perhaps instead of jumpers, just solder the wires).

(4) Make sure however way you decide to have it, that theou light is visible and you can use the button.

(5) Run the script with your installed setup.
# Troubleshooting
If your script runs an error like 

Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
ImportError: no module named 'examplemodule', 

make sure the interpreter you're using on your IDE is "CircuitPython (General), IF it has it.
If not, find an IDE that does. 
If it runs the same error, but the module is "morse", or "blinkboard", make sure morse.py, and blinkboard.py are in your CIRCUITPY drive. 

If the rest works, but the button doesn't, check that the wires are in the right pins, and your script knows it.

 
