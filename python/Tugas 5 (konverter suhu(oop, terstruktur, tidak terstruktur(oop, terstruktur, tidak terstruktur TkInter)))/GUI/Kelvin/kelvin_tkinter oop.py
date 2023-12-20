from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

root = Tk()

class FrmKelvin:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='Kelvin:').grid(row=0, column=0,
                                                sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=2, column=0,
                                                   sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=3, column=0,
                                               sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=4, column=0,
                                              sticky=W, padx=5, pady=5)

        self.txtKelvin = Entry(mainFrame)
        self.txtKelvin.grid(row=0, column=1, padx=5, pady=5)

        self.txtCelcius = Entry(mainFrame)
        self.txtCelcius.grid(row=2, column=1, padx=5, pady=5)

        self.txtFahrenheit = Entry(mainFrame)
        self.txtFahrenheit.grid(row=3, column=1, padx=5, pady=5)

        self.txtReamur = Entry(mainFrame)
        self.txtReamur.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
                                command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def onHitung(self):
        try:
            # Input temperature in Kelvin
            temperature_kelvin = float(self.txtKelvin.get())

            # Convert to other scales
            temperature_celcius = temperature_kelvin - 273
            temperature_fahrenheit = (9/5) * (temperature_kelvin - 273) + 32
            temperature_reamur = (4/5) * (temperature_kelvin - 273)

            # Display results
            self.txtCelcius.delete(0, END)
            self.txtCelcius.insert(END, str(temperature_celcius))

            self.txtFahrenheit.delete(0, END)
            self.txtFahrenheit.insert(END, str(temperature_fahrenheit))

            self.txtReamur.delete(0, END)
            self.txtReamur.insert(END, str(temperature_reamur))


        except ValueError:
            # Handle invalid input
            print("Error. Invalid Number")

    def onKeluar(self, event=None):
        # Close the application
        self.parent.destroy()


if __name__ == '__main__':
    aplikasi = FrmKelvin(root, "Program Konversi Suhu Kelvin")
    root.mainloop()
