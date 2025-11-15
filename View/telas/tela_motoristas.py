import customtkinter as ctk
from tkinter import ttk

class TelaMotoristas:
    def __init__(self, master):
        self.master = master
        self.frame = ctk.CTkFrame(master,fg_color='lightblue')  # sempre crie um frame interno
        self.frame.pack(fill="both", expand=True)
        self.frame.columnconfigure(0,weight=1)
        self.widgets()


    def widgets(self):
        lista_motoristas = ttk.Treeview(self.frame,show='headings',columns=('col1','col2','col3','col4','col5'))
        lista_motoristas.grid(row=0,column=0,sticky='we')

        # CABEÇALHO
        lista_motoristas.heading(column='col1',text='ID')
        lista_motoristas.heading(column='col2',text='Nome')
        lista_motoristas.heading(column='col3',text='Cpf')
        lista_motoristas.heading(column='col4',text='Telefone')
        lista_motoristas.heading(column='col5',text='Cnh')
        
        # TAMANHO COLUNAS
        lista_motoristas.column(column='col1',width=50)
        lista_motoristas.column(column='col2',width=50)
        lista_motoristas.column(column='col3',width=50)
        lista_motoristas.column(column='col4',width=50)
        lista_motoristas.column(column='col5',width=50)
        
