import tkinter as tk

interfaz = tk.Tk()
interfaz.geometry("400x350")
interfaz.title("promedio")
interfaz.configure(background= '#26a69a')
var=tk.DoubleVar()

c1 = tk.Label(interfaz, text= "Ingrese Calificación 1", bg="#5c6bc0", fg="white")
c1.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
n1 = tk.Entry(interfaz)
n1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

c2 = tk.Label(interfaz, text= "Ingrese Calificación 2", bg="#5c6bc0", fg="#f5f5f5")
c2.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
n2 = tk.Entry(interfaz)
n2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

c3 = tk.Label(interfaz, text= "Ingrese Calificación 3", bg="#5c6bc0", fg="#f5f5f5")
c3.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
n3 = tk.Entry(interfaz)
n3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

c4 = tk.Label(interfaz, text= "Ingrese Nota Examen final", bg="#5c6bc0", fg="white")
c4.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
n4 = tk.Entry(interfaz)
n4.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

c5 = tk.Label(interfaz, text= "Ingrese Nota trabajo final", bg="#5c6bc0", fg="white")
c5.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
n5 = tk.Entry(interfaz)
n5.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)


def promedio():
    c1 = float(n1.get()) + float(n2.get()) + float(n3.get())
    c1 = c1 / 3 * float(0.55)
    c4 = float(n4.get()) * float(0.30)
    c5 = float(n5.get()) * float(0.15)
    cf = c1 + c4 + c5

    return var.set(cf)

resultado= tk.Label(interfaz, textvariable = var, padx = 5, pady= 5, width = 50)
resultado.pack()
boton1 = tk.Button(interfaz, text= "Resultado", bg = "#ef5350", command = promedio)
boton1.pack(side= tk.TOP)

interfaz.mainloop()