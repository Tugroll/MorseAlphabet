import tkinter as tk
from tkinter import messagebox

class MorsKodCevirici:
    def __init__(self, root):
        self.root = root
        self.root.title("Mors Kodu Çevirici")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Mors Sözlükleri
        self.morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            ' ': '/'  # Boşluk için
        }
        self.reverse_morse_dict = {value: key for key, value in self.morse_dict.items()}

        # UI Elemanlarını Oluştur
        self.create_widgets()

    def create_widgets(self):
        """Arayüz bileşenlerini oluşturur."""
        # Metin → Mors
        tk.Label(self.root, text="Metin Girin:", font=("Arial", 12)).pack()
        self.text_input = tk.Entry(self.root, width=40)
        self.text_input.pack()

        self.morse_output = tk.StringVar()
        tk.Button(self.root, text="Mors Koduna Çevir", command=self.convert_to_morse).pack()
        tk.Label(self.root, textvariable=self.morse_output, font=("Arial", 12, "bold"), fg="blue").pack()

        # Mors → Metin
        tk.Label(self.root, text="Mors Kodu Girin:", font=("Arial", 12)).pack()
        self.morse_input = tk.Entry(self.root, width=40)
        self.morse_input.pack()

        self.text_output = tk.StringVar()
        tk.Button(self.root, text="Metne Çevir", command=self.convert_to_text).pack()
        tk.Label(self.root, textvariable=self.text_output, font=("Arial", 12, "bold"), fg="green").pack()

    def coded(self, text):

        text = text.upper()
        return " ".join(self.morse_dict[char] for char in text if char in self.morse_dict)

    def decoded(self, mors_code):

        try:
            words = mors_code.split(" / ")
            desifre_kod = []
            for word in words:
                desifre_kelime = "".join(self.reverse_morse_dict[char] for char in word.split())
                desifre_kod.append(desifre_kelime)
            return " ".join(desifre_kod)
        except KeyError:
            return "Hatalı Mors Kodu!"

    def convert_to_morse(self):

        text = self.text_input.get()
        if text:
            self.morse_output.set(self.coded(text))
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir metin girin!")

    def convert_to_text(self):

        morse = self.morse_input.get()
        if morse:
            self.text_output.set(self.decoded(morse))
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir Mors kodu girin!")

# Ana Program
if __name__ == "__main__":
    root = tk.Tk()
    app = MorsKodCevirici(root)
    root.mainloop()

