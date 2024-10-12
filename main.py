import tkinter as tk

alphabet_uppercase = [
    'A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś', 'T', 'U', 'W',
    'Y', 'Z', 'Ź', 'Ż', 'X', 'V'
]

alphabet_lowercase = [
    'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w',
    'y', 'z', 'ź', 'ż', 'x', 'v'
]

#FUNKCJA SPRAWDZAJĄCA CZY TEKST I KLUCZ SĄ WE WŁAŚCIWYM FORMACIE
def validate(input_text, input_key):
    if len(input_text) == 0:
        return 0

    try:
        number = int(input_key)
    except ValueError:
        return -1

    return 1

#FUNKCJA ZWRACAJĄCA NOWY, ZASZYFROWANY TEKST
def use_key(input_text, input_key, is_encrypt):
    new_text = ""

    if is_encrypt:
        for c in input_text:
            if c in alphabet_uppercase:
                c_new_idx = (alphabet_uppercase.index(c) + input_key) % len(alphabet_uppercase)
                new_text += alphabet_uppercase[c_new_idx]
            elif c in alphabet_lowercase:
                c_new_idx = (alphabet_lowercase.index(c) + input_key) % len(alphabet_lowercase)
                new_text += alphabet_lowercase[c_new_idx]
    else:
        for c in input_text:
            if c in alphabet_uppercase:
                c_new_idx = (alphabet_uppercase.index(c) - input_key) % len(alphabet_uppercase)
                new_text += alphabet_uppercase[c_new_idx]
            elif c in alphabet_lowercase:
                c_new_idx = (alphabet_lowercase.index(c) - input_key) % len(alphabet_lowercase)
                new_text += alphabet_lowercase[c_new_idx]
            else:
                new_text += c

    return new_text

#FUNKCJA OBŁUGUJĄCA SZYFROWANIE
def encrypt():
    input_text = encrypt_entry1.get()
    input_key = encrypt_entry2.get()

    if validate(input_text, input_key) == 0:
        encrypt_response.config(text="Wpisz tekst do zaszyfrowania!")
    elif validate(input_text, input_key) == -1:
        encrypt_response.config(text="Wpisz poprawny klucz!")
    else:
        input_key = int(input_key)
        encrypt_response.config(text=use_key(input_text, input_key, is_encrypt=True))

#FUNKCJA OBŁUGUJĄCA ODSZYFROWYWANIE
def decrypt():
    input_text = decrypt_entry1.get()
    input_key = decrypt_entry2.get()

    if validate(input_text, input_key) == 0:
        decrypt_response.config(text="Wpisz tekst do zaszyfrowania!")
    elif validate(input_text, input_key) == -1:
        decrypt_response.config(text="Wpisz poprawny klucz!")
    else:
        input_key = int(input_key)
        decrypt_response.config(text=use_key(input_text, input_key, is_encrypt=False))

#TWORZY GŁÓWNE OKNO
root = tk.Tk()
root.title("Szyfr Cezara")
root.geometry("800x400")

#STYLE
dark_blue_bg = '#0D1B2A'
light_blue_fg = '#E0E1DD'
button_bg = '#1B263B'
button_fg = '#E0E1DD'
entry_bg = '#415A77'
entry_fg = '#E0E1DD'
highlight_color = '#778DA9'

label_font = ('Helvetica', 12, 'bold')
entry_font = ('Helvetica', 10)
button_font = ('Helvetica', 11, 'bold')

root.configure(bg=dark_blue_bg)

#SZYFROWANIE
encrypt_box = tk.Frame(root, padx=10, pady=10, bd=2, relief="groove", bg=dark_blue_bg, highlightbackground=highlight_color, highlightthickness=1)
encrypt_box.pack(pady=10)

encrypt_label0 = tk.Label(encrypt_box, text="SZYFROWANIE:", font=label_font, bg=dark_blue_bg, fg=light_blue_fg)
encrypt_label0.grid(row=0, column=0, columnspan=2, pady=10)

encrypt_label1 = tk.Label(encrypt_box, text="Tekst do zaszyfrowania:", font=entry_font, bg=dark_blue_bg, fg=light_blue_fg)
encrypt_label1.grid(row=1, column=0, pady=10)

encrypt_entry1 = tk.Entry(encrypt_box, width=50, font=entry_font, bg=entry_bg, fg=entry_fg, bd=3, relief='sunken', insertbackground=light_blue_fg)
encrypt_entry1.grid(row=1, column=1, padx=10)

encrypt_label2 = tk.Label(encrypt_box, text="Klucz:", font=entry_font, bg=dark_blue_bg, fg=light_blue_fg)
encrypt_label2.grid(row=2, column=0, pady=10)

encrypt_entry2 = tk.Entry(encrypt_box, width=10, font=entry_font, bg=entry_bg, fg=entry_fg, bd=3, relief='sunken', insertbackground=light_blue_fg)
encrypt_entry2.grid(row=2, column=1)

encrypt_btn = tk.Button(encrypt_box, text="Szyfruj", command=encrypt, font=button_font, bg=button_bg, fg=button_fg, activebackground=highlight_color, relief='raised')
encrypt_btn.grid(row=3, column=0, columnspan=2, pady=15)

encrypt_response = tk.Label(encrypt_box, text="", font=entry_font, bg=dark_blue_bg, fg=light_blue_fg)
encrypt_response.grid(row=4, column=0, columnspan=2)

#DESZYFROWANIE
decrypt_box = tk.Frame(root, padx=10, pady=10, bd=2, relief="groove", bg=dark_blue_bg, highlightbackground=highlight_color, highlightthickness=1)
decrypt_box.pack(pady=10)

decrypt_label0 = tk.Label(decrypt_box, text="DESZYFROWANIE:", font=label_font, bg=dark_blue_bg, fg=light_blue_fg)
decrypt_label0.grid(row=0, column=0, columnspan=2, pady=10)

decrypt_label1 = tk.Label(decrypt_box, text="Tekst do odszyfrowania:", font=entry_font, bg=dark_blue_bg, fg=light_blue_fg)
decrypt_label1.grid(row=1, column=0, pady=10)

decrypt_entry1 = tk.Entry(decrypt_box, width=50, font=entry_font, bg=entry_bg, fg=entry_fg, bd=3, relief='sunken', insertbackground=light_blue_fg)
decrypt_entry1.grid(row=1, column=1, padx=10)

decrypt_label2 = tk.Label(decrypt_box, text="Klucz:", font=entry_font, bg=dark_blue_bg, fg=light_blue_fg)
decrypt_label2.grid(row=2, column=0, pady=10)

decrypt_entry2 = tk.Entry(decrypt_box, width=10, font=entry_font, bg=entry_bg, fg=entry_fg, bd=3, relief='sunken', insertbackground=light_blue_fg)
decrypt_entry2.grid(row=2, column=1)

decrypt_btn = tk.Button(decrypt_box, text="Odszyfruj", command=decrypt, font=button_font, bg=button_bg, fg=button_fg, activebackground=highlight_color, relief='raised')
decrypt_btn.grid(row=3, column=0, columnspan=2, pady=15)

decrypt_response = tk.Label(decrypt_box, text="", font=entry_font, bg=dark_blue_bg, fg=light_blue_fg)
decrypt_response.grid(row=4, column=0, columnspan=2)

#ODPALA APLIKACJE
root.mainloop()
