import tkinter as tk
from tkinter.constants import TOP
from tkinter.font import BOLD
import france_to_dig as fr

class Main(tk.Frame):
    def __init__(self, root):
        self.init_main()

    def to_french(self):
        result = fr.to_dig(self.entry.get())
        self.lbl_result['text'] = result

    def init_main(self):
        self.lbl_top = tk.Label(root, text='Введите прописью число на французском от 0 до 1000', font=('Times New Roman', 14, BOLD))    
        self.lbl_top.pack(side=TOP, pady= 20)
        self.entry = tk.Entry(root, width=100, font=('Times New Roman', 14))
        self.entry.pack(side=TOP)
        self.btn = tk.Button(root, text='Перевод', font=('Times New Roman', 14, BOLD), command=self.to_french)
        self.btn.pack(side=TOP, pady=20) 
        self.lbl_result = tk.Label(root, text='', font=('Times New Roman', 20, BOLD), wraplength=700) 
        self.lbl_result.pack(side=TOP)


if __name__=='__main__':
    root = tk.Tk()
    app = Main(root)
    root.title('Перевод чисел прописью в римские')
    root.geometry('750x250+300+250')
    root.mainloop()