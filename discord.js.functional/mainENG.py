import tkinter as tk

window = tk.Tk()
window.geometry("1645x920")
window.title("Discord.js semplificated")
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
     textINit = "Use in the terminal the command: node index.js"
     textINit_output = tk.Label(window, text=textINit, bg="blue", font=("Supermercado", 16))
     textINit_output.grid(row=0, column=1)

def inst_dsJS():
     textInst = "Use in the terminal the command: npm i discord.js"
     textInst_output = tk.Label(window, text=textInst, bg="blue", font=("Supermercado", 16))
     textInst_output.grid(row=0, column=3)

text = "Discord.js semplificated by MINzer"
text = tk.Label(window, text=text, bg="Blue", font=("Comic Sans MS", 16))
text.grid(row=0, column=0)

init_bot = tk.Button(window, text="Init the bot", bg="Blue", font=("Comic Sans MS",16), command=inizi_bot)
init_bot.grid(row=0, column=1)

inst_lib = tk.Button(window, text="Install the discord.js library", bg="Blue", font=("Comic Sans MS",16), command=inst_dsJS)
inst_lib.grid(row=0, column=2)

if __name__ == "__main__":
    window.mainloop()