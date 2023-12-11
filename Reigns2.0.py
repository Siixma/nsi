# coding: utf-8

from tkinter import *
from tkinter.messagebox import *

fenetre = TK()

def nucleaire():
    if askyesno('Centrale Nucléaire', "Votre peuple a besoin d'énergie, voulez-vous investir dans l'énergie nucléaire pour répondre à leur besoin ?"):
        showinfo("Centrale Nucléaire", "Vous perdez de l'argent mais le peuple est plutôt satisfait !")
    else:
        showwarning("Centrale Nucléaire", "Attention, le peuple manifeste, vous devriez faire attention !")


def scandale():
    if askyesno('Scandale', "Une star vous critique, souhaitez-vous l'enfermer pour éviter des émeutes ?"):
        showwarning("Scandale", "Vous avez enfermé une star nationale pour vous avoir critiquer, le peuple crie à la dictature !")
    else:
        showinfo("Scandale", "Vous avez décidé de ne pas l'enfermer, le peuple réagit plutôt bien.")

#Button(text='Voulez-vous commencer ?', command=scandale).pack()

fenetre.mainloop()