alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
alphacaps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']


def encrypt_caesar(plaintext: str, shift: int = 3):
    ciphertext = ""

    for i in plaintext:
        if i in alpha:
            index = (ord(i) - 97 + shift) % 26
            ciphertext += alpha[index]
        elif i in alphacaps:
            index = (ord(i) - 65 + shift) % 26
            ciphertext += alphacaps[index]
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(plaintext: str, shift: int = 3):
    return encrypt_caesar(plaintext, -shift)


if __name__ == '__main__':
    phrase = "Python3.6"
    number = 3
    print('Исходник:  ', phrase)

    phrase = encrypt_caesar(phrase, number)
    print('Шифр:      ', phrase)

    phrase = decrypt_caesar(phrase, number)
    print('Дешифровка:', phrase)