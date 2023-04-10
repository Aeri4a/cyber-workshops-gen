import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #Variables
        self.fontSettings = ("Montserrat", 25, "normal")

        self.title("Password Generator & Tester | Cybero")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        #Grid
        containerUp = tk.Frame(master=self)
        containerUp.grid(column=0, row=0)

        containerDown = tk.Frame(master=self)
        containerDown.grid(column=0, row=1)

        #Sections - tiles
        self.tile1 = tk.Frame(master=containerUp, width=500, height=420, bg="#272727")
        self.tile1.grid(column=0, row=0)

        self.tile2 = tk.Frame(master=containerUp, width=300, height=420, bg="#e9e9e9")
        self.tile2.grid(column=1, row=0)

        self.tile3 = tk.Frame(master=containerDown, width=800, height=80, bg="#000")
        self.tile3.grid()

        #def create_ui(self):
            


if __name__ == "__main__":
    app = App()
    app.mainloop()