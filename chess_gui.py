import tkinter as tk
from tkinter.constants import TOP
from tkinter.font import BOLD
import chess_script as ch

class Main(tk.Frame):
    def __init__(self, root):
        self.init_main()

    def to_french(self):
        result = ch.Combine(self.entry1.get(), self.entry2.get())
        self.lbl_result['text'] = result

    def init_main(self):
        self.lbl_top = tk.Label(root, text='Введите две строки', font=('Times New Roman', 14, BOLD))    
        self.lbl_top.pack(side=TOP, pady= 20)
        self.entry1 = tk.Entry(root, width=100, font=('Times New Roman', 14))
        self.entry1.pack(side=TOP, pady= 5)
        self.entry2 = tk.Entry(root, width=100, font=('Times New Roman', 14))
        self.entry2.pack(side=TOP)
        self.btn = tk.Button(root, text='Перевод', font=('Times New Roman', 14, BOLD), command=self.to_french)
        self.btn.pack(side=TOP, pady=20) 
        self.lbl_result = tk.Label(root, text='', font=('Times New Roman', 20, BOLD)) 
        self.lbl_result.pack(side=TOP)


if __name__=='__main__':
    root = tk.Tk()
    app = Main(root)
    root.title('Строка в строку')
    root.geometry('550x250+300+250')
    root.mainloop()
