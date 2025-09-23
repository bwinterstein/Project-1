# Opens & reads an encrypted text file contents
# Decrypts file using the Caesar with the specific shift amount (to the right)
# Writes the changed deciphered text to new file
# Uses the modulus operator to make shift fall within range [0,25]
def caesar_decrypt(ciphertext_file, plaintext_file, shift):
    
    # Setting range for number of positions each letter moves backward
    shift = shift % 26
    
    # Opens & reads previously created encrypted file
    with open(ciphertext_file, "r") as inFile:
        cipherText = inFile.read()

    collected_text = [] # creates list to store new characters
    
    # Loop to go through each character in the collected text
    for letter in cipherText:
        if letter.isalpha(): # If it's letter, it will be shifted
            if letter.isupper():
                startingChar = ord('A') # Assigns ASCII value 65
            else: # lowercase
                startingChar = ord('a') # Assigns ASCII value 97

            # Subtract the shift instead of adding
            deciphered = (ord(letter) - startingChar - shift) % 26 + startingChar # Convert letter [(letter ASCII value) - ASCII value(67 or 97) - ('shift' value) % 26]
            collected_text.append(chr(deciphered)) # Changes it to new shifted letter
        else:
            collected_text.append(letter) # Not a letter, no shift needed
    
    # Creates new decrypted output file
    with open(plaintext_file, "w") as outFile:
        outFile.write("".join(collected_text))
        
    # Messsage prints only if no errors occur for instant confirmation
    print(f"Decryption successful! Output written to {plaintext_file}")
    
# Calling/testing decrypting function
caesar_decrypt("encryptCaesar_output.txt", "decryptCaesar_output.txt", 3)

