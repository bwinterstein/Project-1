# Reads the contents of plaintext_file,
# encrypt it using the ROT-13 cipher,
# and write the resulting ciphertext to ciphertext_file.
def rot13_encrypt(plaintext_file, ciphertext_file):
    
    # open & reads file 
    with open(plaintext_file, "r") as inFile:
        plainText = inFile.read()
        
    collected_text = [] # creates list to store new characters
    
    # Checks for letter and/or symbols in collected text
    for letter in plainText: # If it's a letter, it will shift by 13
        if letter.isalpha(): # If uppercase
            if letter.isupper():
                startingChar = ord('A') # Gives numnerical upper case value
            else:
                startingChar = ord('a') # Gives numnerical lower case value
            
            # ciphering letters
            ciphered = (ord(letter) - startingChar + 13) % 26 + startingChar # Converts letter to number
            collected_text.append(chr(ciphered)) # Converts back to new shifted letter
        else: # If not a letter, leave unchanged
            collected_text.append(letter)
            
    # creating new ciphered file
    with open(ciphertext_file, "w") as outFile:
        outFile.write("".join(collected_text))
        
    # Messsage prints only if no errors occur for instant confirmation
    print(f"Encryption successful! Output written to {ciphertext_file}")
    
# Calling/testing encrypting Rot13 function
rot13_encrypt("liquid.txt", "encryptRot13_output.txt")

