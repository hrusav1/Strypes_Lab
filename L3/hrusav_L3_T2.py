import sys


def create_shifted_alphabet(shift):
    
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return str.maketrans(alphabet, shifted_alphabet)


def vigenere_encrypt_cipher(text, key):
    encrypted_text = ""
    key_index = 0

    for char in text:
        
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char.lower()) - ord('a')
            translation_table = create_shifted_alphabet(shift)
            encrypted_text += char.translate(translation_table)
            key_index += 1
        
        else:
            encrypted_text += char
    
    return encrypted_text


if __name__ == "__main__":
    
    try:
        input_str = sys.argv[1]
        key_str = sys.argv[2]
        print(vigenere_encrypt_cipher(input_str, key_str))
    
    except (IndexError, ValueError):
        print("Example: python script.py 'Hello World' 'key'")
        sys.exit(1)


"""
# vigeneire cypher
def vigeneire_encrypt_cypher(text, key):
    encrypted_text = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char.lower()) - ord('a')

            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            key_index += 1

        else:
            encrypted_text += char
    return encrypted_text


# usage
text = "Hello my name is pesho!"
key = "viltrum"
encrypted_text_to_print = vigeneire_encrypt_cypher(text, key)
print("Encrypted text:", encrypted_text_to_print)

"""
