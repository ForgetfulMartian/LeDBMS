def encrypt_caesar(plaintext, shift):
    """Encrypts the plaintext using the Caesar Cipher.

        uses:
        plaintext (str): The text to be encrypted.
        shift (int): The number of positions each letter should be shifted by.

        Gives the encrypted text (ciphertext).
    """
    ciphertext = ""

    for char in plaintext:

        if char.isalpha():
            shift %= 26
            char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """Decrypts the ciphertext using the Caesar Cipher.
    Uses:
        ciphertext (str): The text to be decrypted.
        shift (int): The number of positions each letter was shifted by.
    Gives:
        str: The decrypted text (plaintext).
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift %= 26
            char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        plaintext += char
    return plaintext


print(encrypt_caesar("Bababoi", 12))


def encrypt_monoalphabetic(plaintext: str, key: str) -> str:
    """Encrypts the plaintext using a monoalphabetic cipher.
    Args:
        plaintext (str): The text to be encrypted.
        key (str): The key representing the mapping of each letter to a different letter/symbol.
    Returns:
        str: The encrypted text (ciphertext).
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            char = key[ord(char) - ord('A')]
        ciphertext += char
    return ciphertext


def decrypt_monoalphabetic(ciphertext: str, key: str) -> str:
    """Decrypts the ciphertext using a monoalphabetic cipher.
    Args:
        ciphertext (str): The text to be decrypted.
        key (str): The key representing the mapping of each letter to a different letter/symbol.
    Returns:
        str: The decrypted text (plaintext).
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            char = chr(key.index(char) + ord('A'))
        plaintext += char
    return plaintext


def encrypt_vigenere(plaintext: str, key: str) -> str:
    """Encrypts the plaintext using the Vigenere Cipher.
    Args:
        plaintext (str): The text to be encrypted.
        key (str): The encryption key.
    Returns:
        str: The encrypted text (ciphertext).
    """
    key = key.upper()
    key_length = len(key)
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        ciphertext += char
    return ciphertext

def RC4_Encrypt(key, data):
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]  # Convert key to list of integers
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = 0
    j = 0
    out = []
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
        out.append(chr(ord(char) ^ k))
    return ''.join(out)


def RC4_Decrypt(key, ciphertext):
    return RC4_Encrypt(key, ciphertext)

def encrypt_vigenere(plaintext: str, key: str) -> str:
    """Encrypts the plaintext using the Vigenere Cipher.
    Args:
        plaintext (str): The text to be encrypted.
        key (str): The encryption key.
    Returns:
        str: The encrypted text (ciphertext).
    """
    key = key.upper()
    key_length = len(key)
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext: str, key: str) -> str:
    """Decrypts the ciphertext using the Vigenere Cipher.
    Args:
        ciphertext (str): The text to be decrypted.
        key (str): The encryption key.
    Returns:
        str: The decrypted text (plaintext).
    """
    key = key.upper()
    key_length = len(key)
    plaintext = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        plaintext += char
    return plaintext

