def get_alphabet_start_and_end(char: str) -> (int, int):
    alphabets = [
        [65, 90],  # Латиница в верхнем регистре
        [97, 122],  # Латиница в нижнем регистре
        [1040, 1071],  # Кириллица в верхнем регистре
        [1072, 1103],  # Кириллица в нижнем регистре
    ]

    if char.isalpha():
        char = ord(char)
        try:
            alphabet = list([char in range(x, y + 1) for x, y in alphabets]).index(True)
            return alphabets[alphabet][0], alphabets[alphabet][1] - alphabets[alphabet][0] + 1
        except ValueError:
            raise UserWarning
    else:
        return 0


def char_ceaser(char: str, alphabet_start: int, alphabet_size: int, offset: int) -> str:
    return chr((ord(char) - alphabet_start + offset) % alphabet_size + alphabet_start)


def char_viginere(char: str, key: str, crypt: bool) -> str:
    char_start, char_size = get_alphabet_start_and_end(char)
    key_start, _ = get_alphabet_start_and_end(key)

    if crypt:
        key = ord(key) - key_start
    else:
        key = -(ord(key) - key_start)

    return char_ceaser(char, char_start, char_size, key)


def viginere(plaintext: str, keyword: str, crypt: bool) -> str:
    text_len, key_len = len(plaintext), len(keyword)
    keyword = (keyword * ((text_len // key_len) + 1))

    return ''.join([char_viginere(text, secret, crypt) for text, secret in zip(plaintext, keyword)])


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    return viginere(plaintext, keyword, True)


def decrypt_vigenere(plaintext: str, keyword: str) -> str:
    return viginere(plaintext, keyword, False)


print(encrypt_vigenere("PYTHON", "A"))
# 'PYTHON'
print(encrypt_vigenere("python", "a"))
# 'python'
print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
# 'LXFOPVEFRNHR'
print('------------------------')

print(decrypt_vigenere("PYTHON", "а"))
# 'PYTHON'
print(decrypt_vigenere("python", "a"))
# 'python'
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
# 'ATTACKATDAWN'
