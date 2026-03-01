import board
import digitalio
import time
import morse
import blinkboard
import examplemodule


def clear():
    print("\n" * 40)


def dot():
    blinkboard.speed = 0.2
    blinkboard.blink(1)


def dash():
    blinkboard.speed = 0.5
    blinkboard.blink(1)


# ------------------------
# Encode Mode
# ------------------------

def en():
    try:
        while True:
            encodetime = input("Text? ('.' to return) ")

            if encodetime == ".":
                return

            encoded = morse.encode_message(encodetime)
            print("Encoded:", encoded)

            for char in encoded:
                if char == ".":
                    dot()
                elif char == "-":
                    dash()
                elif char == " ":
                    time.sleep(0.3)
                elif char == "/":
                    time.sleep(0.7)

            clear()

    except KeyboardInterrupt:
        print("\nStopped. Returning to menu.\n")
        return


# ------------------------
# Decode Mode
# ------------------------

def de():

    DOT_THRESHOLD = 0.3
    LETTER_PAUSE = 1.2
    WORD_PAUSE = 2.5
    DEBOUNCE = 0.2

    button = digitalio.DigitalInOut(board.GP22)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

    morsecode = []
    sentence = ""
    press_start = None
    last_release_time = None
    last_letter_time = None
    last_printed_sentence = ""

    print("Decoding... Press Ctrl+C to return.\n")

    try:
        while True:
            now = time.monotonic()

            if not button.value:
                if press_start is None:
                    press_start = now
                    time.sleep(DEBOUNCE)

                while not button.value:
                    time.sleep(0.01)

                duration = time.monotonic() - press_start

                if duration < DOT_THRESHOLD:
                    morsecode.append(".")
                else:
                    morsecode.append("-")

                press_start = None
                last_release_time = now
                last_letter_time = now

            if last_release_time is not None:
                if (now - last_release_time) > LETTER_PAUSE and morsecode:
                    letter_str = "".join(morsecode)
                    letter = morse.decode_letter(letter_str)
                    sentence += letter
                    morsecode = []
                    last_release_time = None

            if last_letter_time is not None:
                if (now - last_letter_time) > WORD_PAUSE:
                    if sentence and not sentence.endswith(" "):
                        sentence += " "
                    last_letter_time = None

            if sentence != last_printed_sentence:
                print("\r" + sentence, end="")
                last_printed_sentence = sentence

            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nStopped. Returning to menu.\n")
        return


# ------------------------
# Menu
# ------------------------

def menu():
    while True:
        clear()
        print("1: Encode with blinks")
        print("2: Decode with button")
        print("Ctrl+C to quit program\n")

        try:
            menuselect = int(input("Selection: "))

            if menuselect == 1:
                en()
            elif menuselect == 2:
                de()
            else:
                print("Error: Not a menu number")
                time.sleep(1)

        except KeyboardInterrupt:
            menu()
            break


menu()