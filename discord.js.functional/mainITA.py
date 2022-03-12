import tkinter as tk

window = tk.Tk()
window.geometry("1645x920")
window.title("Discord.js semplifcato")
window.resizable(True, False)
window.configure(background="blue")

#Tests

#def first_print():
#   text = "Hello"
#    text_output = tk.Label(window, text=text, bg="Blue", font=("Comic Sans MS", 16))
#    text_output.grid(row=0, column=1)

#first_button = tk.Button(text="Saluta!", command=first_print, bg="blue")
#irst_button.grid(row=0, column=0)

def inizi_bot():
     textINit = "Usa nel terminale il commando: node index.js"
     textINit_output = tk.Label(window, text=textINit, bg="blue", font=("Supermercado", 16))
     textINit_output.grid(row=0, column=1)

def inst_dsJS():
     textInst = "Usa nel terminale il commando: npm i discord.js"
     textInst_output = tk.Label(window, text=textInst, bg="blue", font=("Supermercado", 16))
     textInst_output.grid(row=0, column=3)
     
def initnodeJS():
     textInitnode = "Usa nel terminale il commando: npm init"
     textInitnode_output = tk.Label(window, text=textInitnode, bg="blue", font=("Supermercado",16))
     textInitnode_output.grid(row=1, column=0)
     
text = "Discord.js semplificato di MINzer"
text = tk.Label(window, text=text, bg="Blue", font=("Comic Sans MS", 16))
text.grid(row=0, column=0)

init_bot = tk.Button(window, text="Inizializza il bot", bg="Blue", font=("Comic Sans MS",16), command=inizi_bot)
init_bot.grid(row=0, column=1)

inst_lib = tk.Button(window, text="Installa la libreria discord.js", bg="Blue", font=("Comic Sans MS",16), command=inst_dsJS)
inst_lib.grid(row=0, column=3)

inst_lib = tk.Button(window, text="Inizializza node.js", bg="Blue", font=("Comic Sans MS",16), command=initnodeJS)
inst_lib.grid(row=1, column=0)

text2 = "Usa la modalità a schermo intero per una miglior esperienza"
text2 = tk.Label(window, text=text2, bg="Blue", font=("Comic Sans MS", 16))
text2.grid(row=2, column=0)

if __name__ == "__main__":
    window.mainloop()