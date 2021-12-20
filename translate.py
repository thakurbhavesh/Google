import tkinter as tk
from tkinter import *
from tkinter import messagebox
from googletrans import Translator
import pyperclip

# Creating the Frontend by using Tkinter
app = tk.Tk()
app.title('BHAVESH SINGH Translator All Languages')
app.geometry('500x500')
app.configure(bg="lightgreen")

# String Variables
ent_var = StringVar()
out_var = StringVar()
lang_selec = StringVar()


# Class for Translation
class Trans():
    def trans(self):
        inn = ent_var.get()
        if inn != "":
            selected_language = lang_selec.get()

            if selected_language == "Arabic":
                out = Translator().translate(inn, dest='ar')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Chinese":
                out = Translator().translate(inn, dest='zh-TW')
                out_var.set(out.text)
                self.show()

            elif selected_language == "French":
                out = Translator().translate(inn, dest='fr')
                out_var.set(out.text)
                self.show()

            elif selected_language == "English":
                out = Translator().translate(inn, dest='en')
                out_var.set(out.text)
                self.show()

            elif selected_language == "German":
                out = Translator().translate(inn, dest='de')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Gujarati":
                out = Translator().translate(inn, dest='gu')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Hindi":
                out = Translator().translate(inn, dest='hi')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Japanese":
                out = Translator().translate(inn, dest='ja')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Kannada":
                out = Translator().translate(inn, dest='Kn')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Korean":
                out = Translator().translate(inn, dest='Kn')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Latin":
                out = Translator().translate(inn, dest='la')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Marathi":
                out = Translator().translate(inn, dest='mr')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Punjabi":
                out = Translator().translate(inn, dest='pa')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Russian":
                out = Translator().translate(inn, dest='ru')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Spanish":
                out = Translator().translate(inn, dest='es')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Tamil":
                out = Translator().translate(inn, dest='ta')
                out_var.set(out.text)
                self.show()

            elif selected_language == "Telugu":
                out = Translator().translate(inn, dest='te')
                out_var.set(out.text)
                self.show()

            else:
                messagebox.showerror("Error", "Language not available Currently. Please select from the given list")
        else:
            messagebox.showerror("Error", "Input Text Can't Be Empty")

    def show(self):
        # Toplayer for the output.
        top = Toplevel()
        top.title('Shiva Translator Made By Bhavesh Singh')
        top.geometry('500x550')
        top.configure(bg="orange")

        def copy():
            pyperclip.copy(out_var.get())
            # To copy the output directly to the clipboad.

        button = tk.Button(top, text='Copy', width=35, height=3, command=copy,
                           activebackground="lightgreen", activeforeground="black")
        button.place(relx=0.5, rely=0.7, anchor=CENTER)

        msg1 = tk.Label(top, text='Translation', )
        msg1.place(relx=0.5, rely=0.4, anchor=CENTER)

        user_pass = Entry(top,
                          textvariable=out_var, )
        user_pass.place(relx=0.5, rely=0.5, anchor=CENTER, width=400, height=50)


# Creating the object for the Trans Class
obj = Trans()

msg1 = tk.Label(app, text='Input text', )
msg1.place(relx=0.5, rely=0.1, anchor=S)

in_text = Entry(app, textvariable=ent_var)
in_text.place(relx=0.5, rely=0.2, anchor=CENTER, width=350, height=30)

msg2 = tk.Label(app, text='Language')
msg2.place(relx=0.5, rely=0.4, anchor=S)

# Creating the language selection.
languages = ["Hindi", "Telugu", "Spanish", "Russian", "Punjabi", "Marathi", "Latin", "Korean", "Kannada", "Japanese",
             "Tamil", "Gujarati", "German", "English", "French", "Chinese", "Arabic"]

# SpinBox to select the choice of the language.
lang_selec_box = Spinbox(app, values=languages, textvariable=lang_selec)
lang_selec_box.place(relx=0.5, rely=0.5, anchor=CENTER, width=350, height=30)

# Button to start the Trans function.
translate_button = tk.Button(app, text='Translate', width=35, height=3, command=obj.trans,
                             activebackground="dark grey", activeforeground="red")
translate_button.place(relx=0.5, rely=0.7, anchor=CENTER)

app.mainloop()


