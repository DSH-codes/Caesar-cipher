
import customtkinter as ui




class App(ui.CTk):

    def __init__(self, geometry="400x600"):
        super().__init__()
        self.geometry(geometry)
        self.resizable(0, 0)
        self.title(f"{' ' * 42}CaesarCipher 0.1")




if __name__ == "__main__":

    app = App()
    app.mainloop()



