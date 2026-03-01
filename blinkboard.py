import board
import digitalio
import time

# Internal LED object
_led = digitalio.DigitalInOut(board.LED)
_led.direction = digitalio.Direction.OUTPUT

# Global speed variable (seconds)
speed = 0.5

def on():
    """Turn the onboard LED on."""
    _led.value = True

def off():
    """Turn the onboard LED off."""
    _led.value = False

def toggle():
    """Toggle the onboard LED state."""
    _led.value = not _led.value

def blink(times=1):
    """
    Blink the onboard LED using the global 'speed' variable.

    Args:
        times (int): Number of times to blink
    """
    global speed
    for _ in range(times):
        on()
        time.sleep(speed)
        off()
        time.sleep(speed)