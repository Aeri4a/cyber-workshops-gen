import tkinter as tk
import customtkinter as ctk
import secrets

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #VARS
        self.fontBig = ("Arial", 30, "normal")
        self.fontMedium = ("Arial", 22, "normal")
        self.fontSmall = ("Arial", 20, "normal")

        self.title("Password Generator & Tester | Cybero")
        self.iconbitmap("assets\logo.ico")
        self.geometry("800x500")
        self.resizable(width=False, height=False)
        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=3)

        #CONTAINERS
        self.containerUpLeft = ctk.CTkFrame(self, corner_radius=0, fg_color="#272727") 
        self.containerUpLeft.grid(row=0, column=0, sticky="nswe")
        self.containerUpLeft.grid_rowconfigure(0, weight=2)
        self.containerUpLeft.grid_rowconfigure(1, weight=1)
        self.containerUpLeft.grid_rowconfigure(2, weight=1)
        self.containerUpLeft.grid_rowconfigure(3, weight=1)
        self.containerUpLeft.grid_rowconfigure(4, weight=2)
        self.containerUpLeft.grid_rowconfigure(5, weight=2)
        self.containerUpLeft.grid_columnconfigure(0, weight=1)
        self.containerUpLeft.grid_columnconfigure(1, weight=3)

        self.containerUpRight = ctk.CTkFrame(self, corner_radius=0, fg_color="#2b2a2a")
        self.containerUpRight.grid(row=0, column=1, sticky="nswe")

        self.containerDown = ctk.CTkFrame(self, corner_radius=0, fg_color="#1c1c1c")
        self.containerDown.grid(row=1, column=0, columnspan=2, sticky="nswe")
        self.containerDown.grid_columnconfigure(0, weight=1)
        self.containerDown.grid_rowconfigure(0, weight=1)

        #LEFT SIDE
        self.titleLeft = ctk.CTkLabel(self.containerUpLeft, text="Password", font=self.fontBig, bg_color="#11dbae", text_color="#1c1c1c")
        self.titleLeft.grid(row=0, column=0, columnspan=2, sticky="nswe")

        self.alphabetCheck = tk.BooleanVar(value=1)
        self.alphabet = ctk.CTkSwitch(self.containerUpLeft, text="Alphabet", font=self.fontSmall, variable=self.alphabetCheck, progress_color="#11dbae")
        self.alphabet.grid(row=1, column=0, sticky="ws", padx="50")

        self.digitsCheck = tk.BooleanVar(value=0)
        self.digits = ctk.CTkSwitch(self.containerUpLeft, text="Digits", font=self.fontSmall, variable=self.digitsCheck, progress_color="#11dbae")
        self.digits.grid(row=2, column=0, sticky="ws", padx="50")

        self.specialCheck = tk.BooleanVar(value=0)
        self.special = ctk.CTkSwitch(self.containerUpLeft, text="Special chars", font=self.fontSmall, variable=self.specialCheck, progress_color="#11dbae")
        self.special.grid(row=3, column=0, sticky="ws", padx="50")

        #CHARS
        self.charNumberLabel = ctk.CTkLabel(self.containerUpLeft, text="Char number", font=self.fontSmall)
        self.charNumberLabel.grid(row=1, column=1, sticky="s")

        self.passwordLength = tk.IntVar(value=8)
        self.charNumberValue = ctk.CTkLabel(self.containerUpLeft, textvariable=self.passwordLength, font=self.fontSmall)
        self.charNumberValue.grid(row=2, column=1)

        self.charNumberSlider = ctk.CTkSlider(self.containerUpLeft, from_=3, to=30, number_of_steps=30, variable=tk.IntVar(value=8), command=self.change_slider, progress_color="#11dbae", button_color="#11dbae", button_hover_color="#10c099")
        self.charNumberSlider.grid(row=3, column=1)

        #GEN BUTTON
        self.genButton = ctk.CTkButton(self.containerUpLeft, width=400, height=60, text="Generate", cursor="hand2", font=self.fontBig, command=self.generate_password, text_color="#1c1c1c", fg_color="#11dbae", hover_color="#10c099")
        self.genButton.grid(row=4, column=0, columnspan=2, sticky="s")

        #INPUT/OUTPUT
        self.password = tk.StringVar()
        self.genResult = ctk.CTkEntry(self.containerUpLeft, width=400, height=80, font=self.fontMedium, border_color="#11dbae", fg_color="#1c1c1c", justify="center", textvariable=self.password)
        self.genResult.grid(row=5, column=0, columnspan=2)
        self.password.trace("w", lambda *args: self.character_limit())


        #INFO BOX
        self.info = tk.StringVar(value="")
        self.infoBox = ctk.CTkLabel(self.containerDown, textvariable=self.info, font=self.fontSmall)
        self.infoBox.grid(row=0, column=0, sticky="we", padx=10, pady=10)


    def character_limit(self):
        if len(self.password.get()) > 0:
            self.password.set(self.password.get()[:30])

    def change_slider(self, value):
        self.passwordLength.set(int(value))

    def generate_password(self):
        #snip ^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,20}$
        lettersBIG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lettersSMALL = lettersBIG.lower()
        digits = "0123456789"
        symbols = "!@#$%^&*"

        combine = ""

        if not self.alphabetCheck.get() and not self.digitsCheck.get() and not self.specialCheck.get():
            self.info.set("You have to choose at least one option!")
            return

        if self.alphabetCheck.get():
            combine += lettersBIG
            combine += lettersSMALL
        if self.digitsCheck.get():
            combine += digits
        if self.specialCheck.get():
            combine += symbols
        
        length = self.passwordLength.get()
        output = "".join(secrets.choice(combine) for i in range(length))
        self.password.set(output)
        self.info.set("")


if __name__ == "__main__":
    app = App()
    app.mainloop()