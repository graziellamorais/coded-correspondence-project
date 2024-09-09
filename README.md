# coded-correspondence-project
This project involved implementing Caesar Cipher encryption and decryption in Python. I created functions to decode messages using known or brute-forced shift values and to encode messages with a specified shift.

## Project Goals:
This project involved using Python to work with Caesar Cipher encryption and decryption. The goal was to develop functions that could decode encrypted messages and encode new messages based on a given shift value.

## Approach:
Caesar Cipher:
The Caesar Cipher works by shifting each letter in a message by a specific number of positions in the alphabet. My objective was to write Python functions to handle both decoding and encoding of these messages.

## Decoding Messages:
I created a function to decode messages by shifting the letters in the opposite direction of the cipher’s shift value. This allowed me to reveal the original message when the shift (offset) was known.

## Brute Force Decoding:
For cases where the shift value wasn’t provided, I implemented a brute force approach. This involved trying all possible shifts (from 1 to 25) and printing the output for each shift. By reviewing the results, I could determine the correct decoding.

## Encoding Messages:
To send encrypted responses, I wrote a function that shifts the letters of my message by a given offset, creating an encoded message. This allowed me to continue the cryptography challenge with my pen pal.

## Key Python Concepts:
String manipulation
Loops and conditionals
Modular arithmetic (to handle letter shifting)
Brute force algorithms
