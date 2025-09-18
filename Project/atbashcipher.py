alphabet = "abcdefghijklmnopqrstuvwxyz"

def atbash_encrypt(plaintext_file,ciphertext_file):
    """
    reads the contents of plaintext_file, encrpts it using the atbash cipher, and writes the resulting ciphertext to ciphertext_file.
    """

    encoded_alpha = ''
    for char in alphabet:
        encoded_alpha += alphabet[-(alphabet.index(char.lower())+1)]
    print(encoded_alpha)


def atbash_decrypt(ciphertext_file, plaintext_file):
    """
    Reads the contents of ciphertext_file, decrypts it using the Atbash cipher,
    and writes the resulting plaintext to plaintext_file.
    """
    encoded_alpha = ''
    for char in alphabet[::-1]:
        encoded_alpha += alphabet[-(alphabet.index(char.lower())+1)]
    print(encoded_alpha)

atbash_encrypt('words.txt', 'output.txt')
atbash_decrypt('words.txt', 'output.txt')