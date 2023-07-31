from playsound import playsound
import time

translate_dict = {

    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'

}

# message = input("Enter the message you want to Translate - ")
# morse_message = " ".join(translate_dict[c] for c in message.upper())

# print(morse_message)


# def play_morse(text_message):

#     for x in text_message:
#         if x == '.':
#             playsound("short_beep.mp3")
#             time.sleep(0.3)
#         elif x == '-':
#             playsound("long.mp3")
#             time.sleep(0.3)
#         elif x == '/' or " ":
            
#             time.sleep(0.6)


# play_morse(morse_message)


reverse_dict = {v:k for k,v in translate_dict.items()}
reverse_message = input("Enter message in morse code - ")
text_reverse_message = "".join(reverse_dict[c] for c in reverse_message.split(" "))
print(text_reverse_message)






