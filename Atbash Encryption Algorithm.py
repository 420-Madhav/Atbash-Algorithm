#UI to Encipher or Decipher using the Atbash Algorithm

#defining function for Encryption
def madhavEncipher(plaintext):
    ciphertext = ""
    for c in range(len(plaintext)):
        char = plaintext[c]
        if (char.isupper()):
            ciphertext += chr(90-(ord(char)-65) % 26)
        elif char==" ":
            ciphertext += " "
        elif (char.islower()):
            ciphertext += chr(122-(ord(char)-97)%26)
        else:
            ciphertext += char
    return ciphertext
	
#defining function for Decryption
def madhavDecipher(ciphertext):
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if (char.isupper()):
            plaintext += chr(90-(ord(char)-65) % 26)
        elif char==" ":
            plaintext += " "
        elif (char.islower()):
            plaintext += chr(122-(ord(char)-97)%26)
        else:
            plaintext += char
    return plaintext

#importing tkinter module for creating GUI
import tkinter as tk
from tkinter import ttk
from tkinter import font

class MadhavCipher:	
    def __init__(self, root):

        self.plain_text = tk.StringVar(root, value="")
        self.cipher_text = tk.StringVar(root, value="")
        self.key = tk.IntVar(root)
# creates Tkinter window
# defining size of window 
        root.title("Madhav - Atbash Cipher Application")
        root.resizable(True,True)
            # window background
        root.configure(background='yellow')
        
        style = ttk.Style() 
        style.configure("TLabel", font = "Serif 25", padding=25)
        style.configure("TButton", font="Serif 15", padding=15)
        style.configure("TEntry", font="Serif 40", padding=25)

        self.plain_label = tk.Label(root, text="Plain Text", fg="Green", font = ('Helvetica', 12, 'bold'), bd = 16, anchor = "w").grid(row=1, column=1)
        self.plain_entry = tk.Entry(root,font = ('arial', 16, 'bold'), textvariable ='Msg', bd = 10, insertwidth = 4, bg = "blue", justify = 'right',width=32)
        self.plain_entry.grid(row=2, column=0, rowspan=2 , columnspan=2)
        self.plain_clear = tk.Button(root, text="Clear", fg="Black", command=lambda: self.clear('plain')).grid(row=4, column=1)

        self.cipher_label = tk.Label(root, text="Cipher text", fg="Red", font = ('Helvetica', 12, 'bold'), bd = 16, anchor = "w").grid(row=1, column=4)
        self.cipher_entry = tk.Entry(root, font = ('arial', 16, 'bold'), textvariable = 'Result', bd = 10, insertwidth = 4, bg = "blue", justify = 'left',width=32)
        self.cipher_entry.grid(row=2, column=4, rowspan=2 , columnspan=2)
        self.cipher_clear = tk.Button(root, text="Clear", fg="Black", command=lambda: self.clear('cipher')).grid(row=4, column=4)

# buttons to encrypt / decrypt
        self.encipher_button = tk.Button(root, text="ENCRYPT-->", fg='red', command=lambda: self.encipher_press()).grid(row=2, column=3)
        self.decipher_button = tk.Button(root, text="<--DECRYPT", fg='green', command=lambda: self.decipher_press()).grid(row=3, column=3)

    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        else:
            self.plain_entry.delete(0, 'end')

    def encipher_press(self):
        cipher_text = madhavEncipher(self.plain_entry.get())
        self.cipher_entry.delete(0, "end")
        self.cipher_entry.insert(0, cipher_text)

    def decipher_press(self):
        plain_text = madhavDecipher(self.cipher_entry.get())
        self.plain_entry.delete(0, "end")
        self.plain_entry.insert(0, plain_text)

#making the window work
root = tk.Tk()
Madhav = MadhavCipher(root)
root.mainloop()