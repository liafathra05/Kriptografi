import tkinter as tk
from tkinter import filedialog, messagebox
from vigenere_cipher import vigenere_cipher
from playfair_cipher import playfair_cipher
from hill_cipher import hill_cipher

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Enkripsi dan Dekripsi")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Masukkan Teks atau Unggah File").grid(row=0, column=0, sticky="w")
        self.input_text = tk.Text(self.root, height=10, width=50)
        self.input_text.grid(row=1, column=0, columnspan=2)

        tk.Label(self.root, text="Kunci (min 12 karakter)").grid(row=2, column=0, sticky="w")
        self.key_entry = tk.Entry(self.root, width=50)
        self.key_entry.grid(row=3, column=0, columnspan=2)

        tk.Label(self.root, text="Pilih Cipher").grid(row=4, column=0, sticky="w")
        self.cipher_choice = tk.StringVar(value="Vigenere")
        tk.OptionMenu(self.root, self.cipher_choice, "Vigenere", "Playfair", "Hill").grid(row=4, column=1, sticky="w")

        self.encrypt_button = tk.Button(self.root, text="Enkripsi", command=self.encrypt)
        self.encrypt_button.grid(row=5, column=0, pady=5)
        self.decrypt_button = tk.Button(self.root, text="Dekripsi", command=self.decrypt)
        self.decrypt_button.grid(row=5, column=1, pady=5)

        tk.Label(self.root, text="Output Text").grid(row=6, column=0, sticky="w")
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.grid(row=7, column=0, columnspan=2)

        self.upload_button = tk.Button(self.root, text="Unggah File", command=self.upload_file)
        self.upload_button.grid(row=8, column=0, pady=5)
        self.save_button = tk.Button(self.root, text="Simpan Output", command=self.save_output)
        self.save_button.grid(row=8, column=1, pady=5)

    def encrypt(self):
        text = self.input_text.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()
        cipher = self.cipher_choice.get()

        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus terdiri dari minimal 12 karakter.")
            return

        if cipher == "Vigenere":
            result = vigenere_cipher(text, key, encrypt=True)
        elif cipher == "Playfair":
            result = playfair_cipher(text, key, encrypt=True)
        elif cipher == "Hill":
            result = hill_cipher(text, key, encrypt=True)
        else:
            messagebox.showerror("Error", "Invalid cipher selection.")
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)

    def decrypt(self):
        text = self.input_text.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()
        cipher = self.cipher_choice.get()

        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus terdiri dari minimal 12 karakter.")
            return

        if cipher == "Vigenere":
            result = vigenere_cipher(text, key, encrypt=False)
        elif cipher == "Playfair":
            result = playfair_cipher(text, key, encrypt=False)
        elif cipher == "Hill":
            result = hill_cipher(text, key, encrypt=False)
        else:
            messagebox.showerror("Error", "Invalid cipher selection.")
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert(tk.END, content)

    def save_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.output_text.get("1.0", tk.END).strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()