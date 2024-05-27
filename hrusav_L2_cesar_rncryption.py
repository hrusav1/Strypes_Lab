# cesar encryption


def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:

        if char.isalpha():
            shifted = ord(char) + shift

            if char.islower():
                encrypted_text += chr((shifted - ord('a')) % 26 + ord('a'))
        
            elif char.isupper():
                encrypted_text += chr((shifted - ord('A')) % 26 + ord('A'))
        
        else:
            encrypted_text += char

    return encrypted_text


# second option with maketrans
def caesar_encrypt_using_maketrans(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(translation_table)


# Example usage:
print("caesar_encrypt using char shift and maketrans")
text = "Hello, World!"
shift = 3
encrypted_text = caesar_encrypt_using_maketrans(text, shift)
print("Encrypted text:", encrypted_text)

text2 = "Hello, Worldasdasda!"
shift2 = 4
encrypted_text2 = caesar_encrypt(text2, shift2)
print("Encrypted text:", encrypted_text2)

# test for gpg
