# Opens & reads a plain text file contents
# Encrypts file using the Caesar with the specific shift amount (to the right)
# Writes the changed ciphered text to new file
# Uses the modulus operator to make shift fall within range [0,25]
def caesar_encrypt(plaintext_file, ciphertext_file, shift):
    
    # Setting range for number of positions each letter moves forward
    shift = shift % 26
    
    # Opens & reads not yet encrypted file
    with open(plaintext_file, "r") as inFile:
        plainText = inFile.read()

    collected_text = [] # creates list to store new characters
    
    # Loop to go through each character in the collected text
    for letter in plainText:
        if letter.isalpha(): # If it's letter, it will be shifted
            if letter.isupper():
                startingChar = ord('A') # Assigns ASCII value 65
            else: # lowercase
                startingChar = ord('a') # Assigns ASCII value 97

            # Shift letters
            ciphered = (ord(letter) - startingChar + shift) % 26 + startingChar # Convert letter [(letter ASCII value) + ASCII value(67 or 97) + ('shift' value) % 26]
            collected_text.append(chr(ciphered)) # Changes it to new shifted letter
        else: 
            collected_text.append(letter) # Not a letter, no shift needed

    # Creates new encrypted output file
    with open(ciphertext_file, "w") as outFile:
        outFile.write("".join(collected_text))
        
    # Messsage prints only if no errors occur for instant confirmation
    print(f"Encryption successful! Output written to {ciphertext_file}")
    
# Calling/testing encrypting function
caesar_encrypt("liquid.txt", "encryptCaesar_output.txt", 3)
 