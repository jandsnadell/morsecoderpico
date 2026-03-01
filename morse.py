# morse.py

# Morse dictionary for decoding
_MORSE_DICT = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
    ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z",

    "-----": "0", ".----": "1", "..---": "2",
    "...--": "3", "....-": "4", ".....": "5",
    "-....": "6", "--...": "7", "---..": "8",
    "----.": "9",

    "......": " ", ".......": "eeeeeeeeeeeeeeeeeee" # word separator
}

# Reverse dictionary for encoding (letter → Morse)
_ENCODE_DICT = {v: k for k, v in _MORSE_DICT.items() if v != " "}


def decode_letter(morse_code: str) -> str:
    """Decode a single Morse code letter"""
    return _MORSE_DICT.get(morse_code, "?")


def decode_message(data) -> str:
    """
    Decode Morse code into a text string.
    Accepts:
    - String: "... --- ..." (use ' / ' for word separation)
    - Flat list: ["...", "---", "..."]
    - Nested list: [["...", "---", "..."], [".-", ".-."]]
    Returns a single string.
    """
    def decode_letters(letters):
        return "".join(decode_letter(l) for l in letters)

    if isinstance(data, str):
        words = data.split(" / ")
        return " ".join(decode_letters(word.split()) for word in words)

    if isinstance(data, list):
        if data and isinstance(data[0], list):
            return " ".join(decode_letters(word) for word in data)
        else:
            return decode_letters(data)

    return "?"


def encode_letter(char: str) -> str:
    """Encode a single letter or number into Morse code"""
    char = char.upper()
    if char == " ":
        return "......"  # fixed space
    return _ENCODE_DICT.get(char, "?")


def encode_message(text: str) -> str:
    """
    Convert text to Morse code.
    Letters separated by space, words separated by ' / '.
    Unknown characters become '?'.
    """
    morse_words = []
    for word in text.split():
        letters = [encode_letter(c) for c in word]
        morse_words.append(" ".join(letters))
    return " / ".join(morse_words)


# --- Example usage ---
if __name__ == "__main__":
    text = "SOS 123"
    morse = encode_message(text)
    print("Text:", text)
    print("Morse:", morse)
    print("Decoded back:", decode_message(morse))