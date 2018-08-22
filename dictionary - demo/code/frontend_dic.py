import dictionary as dt
from tkinter import *
from tkinter import messagebox

class Window(object):
    '''Clase que inicia la ventana del Diccionario'''
    def __init__(self,window):
        self.window = window
        self.window.wm_title('Dictionario 1.0')
        self.window.resizable(False, False)


        lbl1 = Label(window, text='Ingrese una palabra:')
        lbl1.grid(row=0,column=0,pady=5,padx=(3,0))

        self.en1_text = StringVar()
        self.en1 = Entry(window,width=20,textvariable=self.en1_text)
        self.en1.focus_set()
        self.en1.grid(row=0,column=1)

        sb1 = Scrollbar(window)
        sb1.grid(row=2,column=10,rowspan=5,sticky=N+S+W+E)


        self.txt1 = Text(window,width=50,height=5,yscrollcommand=sb1.set)

        self.txt1.grid(row=2,column=0,columnspan=10,rowspan=5,pady=10)

        sb1.configure(command=self.txt1.yview)
        btn1 = Button(window,text='Buscar',width=12,command=self.get_data)
        btn1.grid(row=0,column=2)
        btn2 = Button(window,text='Cerrar',width=12,command=window.destroy)
        btn2.grid(row=0,column=3)


    def get_data(self):
        self.txt1.delete('1.0',END)
        dict = dt.Diccionario()
        data = dict.dict(self.en1_text.get())
        if data[1]==False:
            answer = messagebox.askyesno("Atencion",data[0])
            if answer == True:
                self.en1.delete(0,END)
                self.en1.insert(END,data[2])
                self.get_data()
            elif answer == False:
                messagebox.showinfo("Information","Intenta nuevamente con otra palabra.")
        else:
            if type(data[0]) == list:
                for k in data[0]:
                    self.txt1.insert(END,k+'\n')
            else:
                sef.txt1.insert(END,data[0])



window = Tk()
Window(window)
window.mainloop()
