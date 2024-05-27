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
text = "Hello, World!"
key = "keys"
encrypted_text_to_print = vigeneire_encrypt_cypher(text, key)
print("Encrypted text:", encrypted_text_to_print)
