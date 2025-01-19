# Enigma

This is a Python program that simulates the Enigma machine, a cipher device used during World War II for encrypting and decrypting messages. This implementation allows you to select rotors, configure initial rotor positions, and encrypt plaintext input.

## Features

- **Rotor selection:** Choose from 5 predefined rotors.
- **Initial rotor positions:** Set the starting positions for all three rotors.
- **Text encryption and decryption:** Encode or decode messages using the simulated Enigma mechanism.
- **Reflector simulation:** Includes a reflector for bi-directional encryption.
- **Alphabet and symbols support:** The program supports letters, numbers, and common punctuation marks.

## Usage

### Prerequisites

- Python 3.x is required to run this program.

### Running the Program

1. Clone or download the repository.
2. Open a terminal and navigate to the directory containing `Enigma.py`.
3. Run the script using:
   ```bash
   python Enigma.py

## Steps to Encrypt/Decrypt a Message

1. **Select Rotors**  
   Choose three unique rotors from the list:  
   - Rotor 1  
   - Rotor 2  
   - Rotor 3  
   - Rotor 4  
   - Rotor 5  

2. **Set Rotor Positions**  
   Provide initial positions for each rotor (values between `0` and `25`).

3. **Input Text**  
   Enter the text to encrypt or decrypt. Only English letters, numbers, and certain symbols are allowed.

4. **View Output**  
   The program will output the encrypted or decrypted message.


## Example

### Input

```bash
Select 3 Rotors
1. Rotor 1
2. Rotor 2
3. Rotor 3
4. Rotor 4
5. Rotor 5

Enter a number 1 - 5 to select rotor No.1 : 1
Enter a number 1 - 5 to select rotor No.2 : 2
Enter a number 1 - 5 to select rotor No.3 : 3

Set Rotor 1 (0-25): 5
Set Rotor 2 (0-25): 10
Set Rotor 3 (0-25): 15

Plain Text : HELLO WORLD
Encrypted/Decrypted message: KXFQJ GJSMX
```

## How It Works

### Rotors

Each rotor maps an input letter to an output letter based on a predefined permutation. The rotors rotate after encoding each letter, dynamically altering the cipher.

### Reflector

The reflector reverses the signal back through the rotors to ensure symmetry in encryption and decryption. This feature enables both encoding and decoding with the same configuration.

### Encoding Process

1. A letter is passed through the rotors in the forward direction.

2. The reflected signal is passed through the rotors in the reverse direction.

3. The rotors rotate after encoding each letter, ensuring a dynamic cipher for each character.

## Notes

- Ensure the input text contains only valid characters. Invalid characters will terminate the program.

- The selected rotors must be unique during selection.

- Rotor positions must be integers between `0` and `25`.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.