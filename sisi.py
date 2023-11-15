import tkinter as tk
class App():
    def __init__(self):
        ventana=tk.Tk()
        ventana.title("platelink")
        ventana.geometry("400x400")
        ventana.configure(bg = "red")

        self.ta = tk.Text(ventana, height=5, width=10)
        self.ta.place(x=50, y=50)

        self.btn = tk.Button(ventana, text="Aceptar", command=self.addtext)
        self.btn.place(x=200, y=50)
        
        ventana.mainloop()
    
    
    def addtext(self):
        self.ta.insert(tk.END, "qweqewqwe")
        

Objeto_ventana = App() 