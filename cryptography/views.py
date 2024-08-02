from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64

@csrf_exempt
def encrypt_decrypt(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', '')
        operation = data.get('operation')
        algorithm = data.get('algorithm')
        key = data.get('key', '')

        result = process_text(text, operation, algorithm, key)
        return JsonResponse({'result': result})

    return render(request, 'cryptography/templates/encrypt_decrypt.html')

def process_text(text, operation, algorithm, key):
    if algorithm == 'caesar':
        shift = int(key) if key.isdigit() else 0
        return caesar_cipher(text, shift, operation == 'encrypt')
    elif algorithm == 'vigenere':
        return vigenere_cipher(text, key, operation == 'encrypt')
    elif algorithm == 'base64':
        return base64_encode_decode(text, operation == 'encrypt')
    elif algorithm == 'rot13':
        return rot13(text)
    elif algorithm == 'morse':
        if operation == 'encrypt':
            return text_to_morse(text)
        elif operation == 'decrypt':
            return morse_to_text(text)
    return ''

# Morse code functions here (text_to_morse, morse_to_text)

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + (shift if encrypt else -shift)) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def vigenere_cipher(text, key, encrypt=True):
    result = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_shift = ord(key[key_index % key_length]) - 65
            shifted = (ord(char) - ascii_offset + (key_shift if encrypt else -key_shift)) % 26
            result += chr(shifted + ascii_offset)
            key_index += 1
        else:
            result += char
    return result

def base64_encode_decode(text, encode=True):
    if encode:
        return base64.b64encode(text.encode()).decode()
    else:
        try:
            return base64.b64decode(text).decode()
        except:
            return "Error: Invalid Base64 string"

def rot13(text):
    return caesar_cipher(text, 13)

# Morse Code functions
def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('')  # For characters not in the dictionary
    return ' '.join(morse_code)

def morse_to_text(morse_code):
    REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
    morse_code = morse_code.strip().split(' ')
    text = []
    for code in morse_code:
        if code in REVERSE_MORSE_CODE_DICT:
            text.append(REVERSE_MORSE_CODE_DICT[code])
        else:
            text.append('')  # For invalid Morse code
    return ''.join(text)

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' / '
}
