morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # Boşlukları ayırmak için
}

reverse_morse_dict = {value : key for key,value in morse_dict.items()}


def coded(text):
    text = text.upper()
    return " ".join(morse_dict[char] for char in text if char in morse_dict)

mor_code = "... .. -.- - .. .-. / --. .. -"

def decoded(mors_code):
    words = mors_code.split("/")

    desifre_kod = []

    for word in words:
        desifre_kelime = " ".join(reverse_morse_dict[char] for char in word.split())
        desifre_kod.append(desifre_kelime)

    print(desifre_kod)





decoded(mor_code)





