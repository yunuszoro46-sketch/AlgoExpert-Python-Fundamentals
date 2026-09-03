def caesar_cipher(string, offset):
    encoded_chars = []
    for char in string:
        # Shift character backwards by offset with wrapping around 'a' to 'z'
        shifted_char = chr((ord(char) - ord('a') - offset) % 26 + ord('a'))
        encoded_chars.append(shifted_char)
    return "".join(encoded_chars)
