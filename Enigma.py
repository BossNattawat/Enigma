import string

class Enigma:
    def __init__(self, rotor_1, rotor_2, rotor_3, reflector, set_rotor_1, set_rotor_2, set_rotor_3):
        self.rotors = [rotor_1, rotor_2, rotor_3]
        self.reflector = reflector
        self.alphabet = string.ascii_uppercase
        self.position = [set_rotor_1, set_rotor_2, set_rotor_3]
        
    def rotate_rotors(self):
        
        # Rotate the first rotor by 1 position
        self.position[0] = (self.position[0] + 1) % 26
        
        # Check if the first rotor has completed a full rotation (back to 0)
        if self.position[0] == 0:
            # rotate the second rotor by 1 position
            self.position[1] = (self.position[1] + 1) % 26
            
            # Check if the second rotor has also completed a full rotation
            if self.position[1] == 0:
                # rotate the third rotor by 1 position
                self.position[2] = (self.position[2] + 1) % 26
    
    def encode_letter(self, letter):
        # Find the initial index of the letter in the alphabet
        index = self.alphabet.index(letter)
        
        # Pass the letter forward through each rotor with the current rotor positions
        for i, rotor in enumerate(self.rotors):
            shift = self.position[i]
            index = (rotor[(index + shift) % 26] - shift) % 26
        
        # Reflect the index with the reflector
        index = self.reflector[index]
        
        # Pass the letter backward through each rotor, starting from the last rotor
        for i, rotor in reversed(list(enumerate(self.rotors))):
            shift = self.position[i]
            index = (rotor.index((index + shift) % 26) - shift) % 26
        
        # Rotate the rotors after each letter is encoded
        self.rotate_rotors()
        
        # Return the encrypted letter, finding it by index in the alphabet
        return self.alphabet[index]
    
    def encrypt_text(self, text):
        encrypt_text = ""
        
        # Loop through each character in the input text
        for letter in text:
            if letter in self.alphabet:
                encrypt_text += self.encode_letter(letter)
            else:
                encrypt_text += letter
                
        # Return the full encrypted message
        return encrypt_text
    
rotor_1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
rotor_2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
rotor_3 = [1, 4, 11, 13, 12, 3, 7, 17, 0, 5, 10, 16, 9, 14, 8, 6, 25, 24, 23, 22, 21, 20, 19, 18, 15, 2]
reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

def main():

    while(True):
        
        try:
            print()
            set_rotor_1 = int(input("Set Rotor 1 (0-25): "))
            set_rotor_2 = int(input("Set Rotor 2 (0-25): "))
            set_rotor_3 = int(input("Set Rotor 3 (0-25): "))
            print()
            
            if not (0 <= set_rotor_1 < 26 and 0 <= set_rotor_2 < 26 and 0 <= set_rotor_3 < 26):
                raise ValueError
        except ValueError:
            print("Rotor positions must be integers between 0 and 25.")
            continue
        
        enigma_machine = Enigma(rotor_1, rotor_2, rotor_3, reflector, set_rotor_1, set_rotor_2, set_rotor_3)
        
        ascii = string.ascii_uppercase
        
        plain_text = input("Plain Text : ").upper()
        
        for letter in plain_text:
            if letter not in ascii and letter != " ":
                print("The input must be English Alphabet")
                return
        break
    
    encrypted_message = enigma_machine.encrypt_text(plain_text)
    
    print("Encrypted/Decrypted message:", encrypted_message)
    print()

if __name__ == "__main__":
    main()