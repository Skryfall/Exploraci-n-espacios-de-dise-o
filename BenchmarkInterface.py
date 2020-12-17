import tkinter as tk
import os
#sudo apt-get install python3-tk

root = tk.Tk()
root.geometry("1000x300")
root.title('Ejecutador de Benchmarks para SPEC y PARSEC')
v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python
param = tk.IntVar()
param.set(10)

benchmarks = {1: '429.mcf', 2 : '456.hmmer', 3 : "458.sjeng", 4 : "blackscholes" ,  5 :"freqmine" , 6: "swaptions"}
params = {10: 'cacheline', 11: 'l1d_assoc', 12 : "l1d_size", 13 : "l1i_assoc" ,  14 :"l1i_size" , 15: "l2_assoc", 16: "l2_size"}

def ShowChoice():
    return
    #print(benchmarks.get(v.get()))

def ShowParam():
    return
    #print(params.get(param.get()))

def ejecutar():
    print('----------------------------------ejecutar---------------------------')
    print(benchmarks.get(v.get()))
    #v.get() el benchmark a correr
    print(params.get(param.get()))
    #param.get el parametro a variar
    print('-------------------------------------------------------------')
    os.system("python3 SPEC/SPEC/"+benchmarks.get(v.get())+"/stats/"+params.get(param.get())+"/graphics.py ")

tk.Label(root, text="""Seleccione el Benchmark a Utilizar:""", justify = tk.RIGHT, padx = 20, font=("Courier", 10)).grid(row=0, column=1)

row = 0
i = row + 1

columna = 0
specLabel = tk.Label(root, text="SPEC:").grid(row=i, column=columna)
i = i + 1

tk.Radiobutton(root,text="429.mcf", padx = 20, variable=v, command=ShowChoice, value=1,).grid(row=i, column=columna)
i = i + 1
print(i)
tk.Radiobutton(root,text="456.hmmer", padx = 20, variable=v, command=ShowChoice,value=2, ).grid(row=i, column=columna)
i = i + 1
print(i)
tk.Radiobutton(root,text="458.sjeng", padx = 20, variable=v, command=ShowChoice,value=3).grid(row=i, column=columna)
i = i + 1

j = row + 1
columna = 2
parsecLabel = tk.Label(root, text="PARSEC:").grid(row=j, column=columna)

j =j+ 1

tk.Radiobutton(root,text="blackscholes", padx = 20, variable=v, command=ShowChoice, value=4).grid(row=j, column=columna)
j =j+ 1
print(i)
tk.Radiobutton(root,text="freqmine", padx = 20, variable=v, command=ShowChoice,value=5).grid(row=j, column=columna)
j =j+ 1
print(i)
tk.Radiobutton(root,text="swaptions", padx = 20, variable=v, command=ShowChoice,value=6).grid(row=j, column=columna)
j =j+ 1



tk.Label(root, text="""Seleccione el parametro que quiere variar:""", justify = tk.RIGHT, padx = 20, font=("Courier", 10)).grid(row=j, column=0)
j = j + 1

columnaAtributos = 0
tk.Radiobutton(root,text="l1d_size", padx = 20, variable=param, command=ShowParam,value=12,).grid(row=j, column=columnaAtributos)
columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="l1i_size", padx = 20, variable=param, command=ShowParam,value=14,).grid(row=j, column=columnaAtributos)
columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="l2_size", padx = 20, variable=param, command=ShowParam,value=16,).grid(row=j, column=columnaAtributos)
columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="l1d_assoc", padx = 20, variable=param, command=ShowParam,value=11,).grid(row=j, column=columnaAtributos)
columnaAtributos = 0
j = j + 1
tk.Radiobutton(root,text="l1i_assoc", padx = 20, variable=param, command=ShowParam,value=13,).grid(row=j, column=columnaAtributos)
columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="l2_assoc", padx = 20, variable=param, command=ShowParam,value=15,).grid(row=j, column=columnaAtributos)
columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="cacheline", padx = 20, variable=param, command=ShowParam,value=10,).grid(row=j, column=columnaAtributos)

columnaAtributos = columnaAtributos + 1

j = j + 1
exitButton = tk.Button(root, text="Ejecutar", command=ejecutar, bg='red').grid(row=j + 1, column=1)

root.mainloop()