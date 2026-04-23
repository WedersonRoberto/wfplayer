import tkinter as tk
def clicar():
    print("Play")
janela = tk.Tk()
janela.title("WFPLAYER")
janela.geometry("300x200")


botao = tk.Button(
    janela,
    text = "PLAY",
    command=clicar,
    font=("Arial",16),
    bg="black",
    fg="white", 
    width=5,
    height=1)
botao.place(relx=0.5,rely=0.92,anchor="center")    
janela.mainloop()