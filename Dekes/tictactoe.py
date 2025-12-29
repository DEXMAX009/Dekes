from tkinter import *

window = Tk()
window.title("Крестики-нолики")
window.geometry("300x300")

current_player = "X"

def click(btn):
    global current_player
    btn["text"] = current_player
    btn["state"] = "disabled"   # блокируем кнопку

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# кнопки
btn1 = Button(window, text="", font=("Arial", 20), width=5, height=2,
              command=lambda: click(btn1))
btn2 = Button(window, text="", font=("Arial", 20), width=5, height=2,
              command=lambda: click(btn2))
btn3 = Button(window, text="", font=("Arial", 20), width=5, height=2,
              command=lambda: click(btn3))

btn4 = Button(window, text="", font=("Arial", 20), width=5, height=2,
              command=lambda: click(btn4))
btn5 = Button(window, text="", font=("Arial", 20), width=5, height=2,
              command=lambda: click(btn5))
btn6 = Button(window, text="", font=("Arial", 20), width=5, height=2,
              command=lambda: click(btn6))

btn7 = Button(window, text="", font=("Arial", 20), width=5, height=2,
              command=lambda: click(btn7))
btn8 = Button(window, text="", font=("Arial", 20), width=5, height=2,
              command=lambda: click(btn8))
btn9 = Button(window, text="", font=("Arial", 20), width=5, height=2,
              command=lambda: click(btn9))

# размещение
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)

btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

window.mainloop()

