import tkinter as tk
from tkinter import ttk
from googletrans import Translator


class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Translator by Muzammil")
        self.master.geometry("600x450")

        # Style configuration for a modern, colorful look
        style = ttk.Style()
        style.theme_use("clam")

        # Notebook and tabs
        style.configure("TNotebook", background="#333333", borderwidth=0)
        style.configure("TNotebook.Tab", background="#666666", foreground="#FFFFFF", padding=10)
        style.map("TNotebook.Tab", background=[("selected", "#FFCC00")], foreground=[("selected", "#000000")])

        # Labels
        style.configure("TLabel", background="#333333", foreground="#FFFFFF", font=("Helvetica", 12))

        # Buttons
        style.configure("TButton", font=("Helvetica", 12), padding=5)
        style.map("TButton", background=[("active", "#1C86EE"), ("!active", "#6495ED")],
                  foreground=[("active", "#FFFFFF"), ("!active", "#000000")])

        # Comboboxes
        style.configure("TCombobox", background="#1C86EE", foreground="#FFFFFF", font=("Helvetica", 12))

        # Frames
        style.configure("TFrame", background="#C2C2C2")

        # Create the Notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill="both")

        # Create tabs
        self.translate_tab = ttk.Frame(self.notebook)
        self.about_tab = ttk.Frame(self.notebook)

        # Add tabs to notebook
        self.notebook.add(self.translate_tab, text="Translate")
        self.notebook.add(self.about_tab, text="About")

        # Languages
        self.langs = [
            "English", "French", "German", "Italian", "Spanish",
            "Urdu", "Hindi", "Chinese", "Russian", "Arabic"
        ]
        self.lang_codes = {
            "English": "en", "French": "fr", "German": "de", "Italian": "it", "Spanish": "es",
            "Urdu": "ur", "Hindi": "hi", "Chinese": "zh", "Russian": "ru", "Arabic": "ar"
        }

        # Translate Tab
        self.create_translate_tab()

        # About Tab
        self.create_about_tab()

    def create_translate_tab(self):
        label1 = ttk.Label(self.translate_tab, text="Enter text to translate:")
        label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.textbox1 = tk.Text(self.translate_tab, height=6, bg="#444444", fg="#FFFFFF", insertbackground="white",
                                font=("Helvetica", 12))
        self.textbox1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        label2 = ttk.Label(self.translate_tab, text="Choose source language:")
        label2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.source_lang = ttk.Combobox(self.translate_tab, values=self.langs, state="readonly")
        self.source_lang.current(0)
        self.source_lang.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        label3 = ttk.Label(self.translate_tab, text="Choose destination language:")
        label3.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.dest_lang = ttk.Combobox(self.translate_tab, values=self.langs, state="readonly")
        self.dest_lang.current(1)
        self.dest_lang.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        self.button1 = ttk.Button(self.translate_tab, text="Translate", command=self.translate)
        self.button1.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        self.clear_button = ttk.Button(self.translate_tab, text="Clear", command=self.clear_text)
        self.clear_button.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

        label4 = ttk.Label(self.translate_tab, text="Translated text:")
        label4.grid(row=7, column=0, padx=10, pady=10, sticky="w")

        self.textbox2 = tk.Text(self.translate_tab, height=6, bg="#444444", fg="#FFFFFF", state="disabled",
                                insertbackground="white", font=("Helvetica", 12))
        self.textbox2.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.translate_tab.grid_columnconfigure(0, weight=1)
        self.translate_tab.grid_columnconfigure(1, weight=1)

    def create_about_tab(self):
        about_label = ttk.Label(self.about_tab, text=(
            "Language Translator App\n\n"
            "Version 1.0\n\n"
            "Developer by Muzzammil Hussain.\n\n"
            "Developed with Python, Tkinter, and googletrans.\n\n"
            "Translate between multiple languages with ease."
        ), justify="center", font=("Helvetica", 14, "bold"))
        about_label.pack(expand=True, padx=20, pady=20)

    def translate(self):
        translator = Translator()
        text = self.textbox1.get("1.0", tk.END)
        src_lang = self.lang_codes[self.source_lang.get()]
        dest_lang = self.lang_codes[self.dest_lang.get()]
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        self.textbox2.config(state="normal")
        self.textbox2.delete("1.0", tk.END)
        self.textbox2.insert(tk.END, translation.text)
        self.textbox2.config(state="disabled")

    def clear_text(self):
        self.textbox1.delete("1.0", tk.END)
        self.textbox2.config(state="normal")
        self.textbox2.delete("1.0", tk.END)
        self.textbox2.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
