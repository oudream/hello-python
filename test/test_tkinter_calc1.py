# -*- coding: utf-8 -*-
# author: Cullen

# import the module

from tkinter import font
import tkinter as tk
from functools import partial
from pil import Image, ImageTk


def get_input(entry, argu):
    entry.insert(END, argu)


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, END)


def calc(entry):
    input = entry.get()
    output = str(eval(input.strip()))
    clear(entry)
    entry.insert(END, output)


def cal():
    root = tk()
    root.title("Calc")
    root.resizable(0, 0)

    entry_font = font.Font(size=12)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, sticky=N + W + S + E, padx=5, pady=5)

    button_font = tkFont.Font(size=10, weight=tkFont.BOLD)
    button_bg = '#D5E0EE'
    button_active_bg = '#E5E35B'

    myButton = partial(Button, root, bg=button_bg, padx=10, pady=3, activebackground=button_active_bg)

    button7 = myButton(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=1, column=0, pady=5)

    button8 = myButton(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=1, column=1, pady=5)

    button9 = myButton(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=1, column=2, pady=5)

    button10 = myButton(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=1, column=3, pady=5)

    button4 = myButton(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=2, column=0, pady=5)

    button5 = myButton(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=2, column=1, pady=5)

    button6 = myButton(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=2, column=2, pady=5)

    button11 = myButton(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=2, column=3, pady=5)

    button1 = myButton(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=3, column=0, pady=5)

    button2 = myButton(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=3, column=1, pady=5)

    button3 = myButton(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=3, column=2, pady=5)

    button12 = myButton(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=3, column=3, pady=5)

    button0 = myButton(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=4, column=0, columnspan=2, padx=3, pady=5, sticky=N + S + E + W)

    button13 = myButton(text='.', command=lambda: get_input(entry, '.'))
    button13.grid(row=4, column=2, pady=5)

    button14 = Button(root, text='/', bg=button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '/'))
    button14.grid(row=4, column=3, pady=5)

    button15 = Button(root, text='<-', bg=button_bg, padx=10, pady=3,
                      command=lambda: backspace(entry), activebackground=button_active_bg)
    button15.grid(row=5, column=0, pady=5)

    button16 = Button(root, text='C', bg=button_bg, padx=10, pady=3,
                      command=lambda: clear(entry), activebackground=button_active_bg)
    button16.grid(row=5, column=1, pady=5)

    button17 = Button(root, text='=', bg=button_bg, padx=10, pady=3,
                      command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=2, columnspan=2, padx=3, pady=5, sticky=N + S + E + W)

    root.mainloop()


if __name__ == '__main__':
    cal()