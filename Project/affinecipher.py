alphabet = "abcdefghijklmnopqrstuvwxyz"

def affine_encrypt(plaintext_file, ciphertext_file, a, b):
    if a < 2 or a > 25 or a % 2 == 0:
        print("unable to encrypt")
        return
    encoded_alpha = ''
    for char in alphabet:
        encoded_alpha += alphabet[(a * alphabet.index(char)+b)%26]
    print(encoded_alpha)


def affine_decrypt(ciphertext_file, plaintext_file, a, b):
    if a < 2 or a > 25 or a % 2 == 0:
            print("unable to encrypt")
            return
    encoded_alpha = ''
    for char in alphabet:
        encoded_alpha += alphabet[(pow(a, -1, 26)*(alphabet.index(char)-b) % 26)]
    print(encoded_alpha)

affine_encrypt('word.txt', 'output.txt', 5 , 3 )
affine_decrypt('word.txt', 'output.txt', 5 , 3 )
