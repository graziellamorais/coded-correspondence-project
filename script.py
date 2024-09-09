'''
Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 

For example, if I chose an offset of 3 and a message of "hello", I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"! Now I can send you my message and the offset and you can decode it by shifting each letter 3 places to the right. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer encoded message that you have to decode yourself!
    
    xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
    
This message has an offset of 10. Can you decode it?
'''

alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
alphabet = []

# Transforming string into list
for c in alphabet_string:
    alphabet.append(c)

# Function to decode a message received
def caesar_cipher_decode(message, offset):
    decoded_message = ''
    message_lower = message.lower()
    # Looping through the message
    for char in message_lower:
        if char.islower():
            # Finding the index of the character in the alphabet
            index = alphabet.index(char)
            # Calculating the new shifted index
            shifted_index = (index + offset) % 26  # Subtracting offset and wrapping around with modulo 26
            # Appending the corresponding letter from alphabet to the decoded message
            decoded_message += alphabet[shifted_index]
        else:
            # If it's not a letter (like space or punctuation), add it as is
            decoded_message += char
    
    return decoded_message

# The encoded message
encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

# Offset for decoding
offset = 10

# Decoding the message and printing it
decoded_message = caesar_cipher_decode(encoded_message, offset)
print(decoded_message)


# Function to encode a message
def caesar_cipher_encode(message, offset):
    encoded_message = ''
    message_lower = message.lower()
    for char in message_lower:
        if char.islower():
            index = alphabet.index(char)
            shifted_index = (index - offset) % 26
            encoded_message += alphabet[shifted_index]
        else:
            encoded_message += char
    return encoded_message

message = 'Hello there! This is so interesting... I am doing well, thanks!'
offset = 10
encoded_message_test = caesar_cipher_encode(message, offset)
print(encoded_message_test)



'''
You're getting the hang of this! Okay here are two more messages, the first one is coded just like before with an offset of ten, and it contains a hint for decoding the second message!

First message:
    
    jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.
        
Second message:
    
    bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!
'''

# New messages received
first_message = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
second_message = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'

first_message_decoded = caesar_cipher_decode(first_message, offset)
print(first_message_decoded)

offset = 14
second_message_decoded = caesar_cipher_decode(second_message, offset)
print(second_message_decoded)


'''
Hello again friend! I knew you would love the Caesar Cipher, it's a cool, simple way to encrypt messages. 
Did you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift? 
That's all changed with computers! Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.
            
To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. 
It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of the shift. 
You'll have to brute force it yourself.
            
Here's the coded message:
            
    vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
            
Good luck!
'''

third_message = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'

# Function to try different offsets
def brute_force_caesar_cipher(message):
    for shift in range(1, 26):
        print(f"Trying shift value {shift}:")
        print(caesar_cipher_decode(message, shift))
        print('')

# Brute force decoding
brute_force_caesar_cipher(third_message)


'''
Salutations! As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, and us crypto-enthusiasts have had to get more creative and use more complicated ciphers. This next cipher I'm going to teach you is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso (cool name eh?) in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
            
The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.
           
Consider the message:
           
    barry is the spy

If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
           
    dog
               
Now we repeat the keyword over and over to generate a keyword phrase that is the same length as the message we want to code. So if we want to code the message "barry is the spy" our keyword phrase is "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth.

              message:    b  a  r  r  y    i  s    t  h  e    s  p  y
                
       keyword phrase:    d  o  g  d  o    g  d    o  g  d    o  g  d
                 
resulting place value:    24 12 11 14 10   2  15   5  1  1    4  9  21
      
So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us a place value of 24, which is "y". Remember to loop back around when we reach either end of the alphabet! Then continue the trend: we shift "a" by the place value of "o", 14, and get "m", we shift "r" by the place value of "g", 6, and get "l", shift the next "r" by 3 places and get "o", and so forth. Once we complete all the shifts we end up with our coded message:
            
    ymlok cp fbb ejv
                
As you can imagine, this is a lot harder to crack without knowing the keyword! So now comes the hard part. I'll give you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:
            
    txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!
                
and the keyword to decode my message is 
            
    friends
                
Because that's what we are! Good luck friend!
'''
