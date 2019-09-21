import os
morse_code = {     'A': '.-',     'B': '-...',
                       'C': '-.-.',   'D': '-..',    'E': '.',
                       'F': '..-.',   'G': '--.',    'H': '....',
                       'I': '..',     'J': '.---',   'K': '-.-',
                       'L': '.-..',   'M': '--',     'N': '-.',
                       'O': '---',    'P': '.--.',   'Q': '--.-',
                       'R': '.-.',    'S': '...',    'T': '-',
                       'U': '..-',    'V': '...-',   'W': '.--',
                       'X': '-..-',   'Y': '-.--',   'Z': '--..',
                       '1': '.----',  '2': '..---',  '3': '...--',
                       '4': '....-',  '5': '.....',  '6': '-....',
                       '7': '--...',  '8': '---..',  '9': '----.',
                       '0': '-----',  ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.',   '-': '-....-',
                       '(': '-.--.',  ')': '-.--.-' }

n = input()
r = []
#program to convert text into morse code
for i in n:
    if i == " ":
        r.append('|')
    else:
        r.append(morse_code.get(i.upper()))

r = " ".join(r)
print(r)

#morse to sound
import time
for i in r:
    time.sleep(0.25)
    if i == '.':
        print(1,end = " ")
        os.system("morsesound.wav")
    if i == '-':
        print(2,end = " ")
        os.system("morsecode-.wav")
    if i =='|':
        print(3, end=" ")
        time.sleep(0.7)
