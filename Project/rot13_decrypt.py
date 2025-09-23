# Reads the contents of ciphertext_file,
# decrypt it using the ROT-13 cipher,
# and write the resulting plaintext to plaintext_file.
def rot13_decrypt(ciphertext_file, plaintext_file):
    
    # open & reads deciphered file 
    with open(ciphertext_file, "r") as inFile:
        cipheredText = inFile.read()

    collected_text = [] # creates list to store new characters
    
    # Checks for letter and/or symbols in collected encrypted text
    for letter in cipheredText:
        if letter.isalpha(): # If it's a letter, it will shift by 13
            if letter.isupper(): # If uppercase
                startingChar = ord('A') # Gives numnerical upper case value
            else: # If lowercase
                startingChar = ord('a') # Gives numnerical lower case value
            
            # deciphering letters
            deciphered = (ord(letter) - startingChar + 13) % 26 + startingChar # Converts letter to number
            collected_text.append(chr(deciphered)) # Converts back to new shifted letter
        else: # If not a letter, leave unchanged
            collected_text.append(letter)
            
    # creating new deciphered file
    with open(plaintext_file, "w") as outFile:
        outFile.write("".join(collected_text))
    
    # Messsage prints only if no errors occur for instant confirmation
    print(f"Decryption successful! Output written to {plaintext_file}")
    
# Calling/testing decrypting Rot13 function
rot13_decrypt("encryptRot13_output.txt", "decryptRot13_output.txt")


