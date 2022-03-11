import tkinter as tk

window = tk.Tk()
window.geometry("980x720")
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

text = "Discord.js semplificated by MINzer"
text = tk.Label(window, text=text, bg="Blue", font=("Comic Sans MS", 16))
text.grid(row=50, column=50)

init_bot = tk.Button(window, text="Init the bot", bg="Blue", font=("Comic Sans MS",16), command=inizi_bot)
init_bot.grid(row=0, column=0)

if __name__ == "__main__":
    window.mainloop()