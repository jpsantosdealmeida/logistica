from tkinter import ttk
import customtkinter as ctk
from PIL import Image,ImageTk
from .telas.tela_motoristas import TelaMotoristas

class TelaMain:
    def __init__(self,master):
        self.master = master
        self.frame_menu()
        self.frame_conteudo()
    def frame_menu(self):

        frame_menu_lateral = ctk.CTkFrame(self.master,fg_color='lightgray',corner_radius=0)
        frame_menu_lateral.grid(row=0,column=0,sticky='wns')
        frame_menu_lateral.rowconfigure(5,weight=1)
        label_titulo = ctk.CTkLabel(frame_menu_lateral,text='Menu de Opções',font=(0,25),text_color='black')
        label_titulo.grid(row=0,column=0,pady=5,padx=5)

        dash = ImageTk.PhotoImage(Image.open('dashboard.png').resize((40,40)))
        motorista = ImageTk.PhotoImage(Image.open('driver.png').resize((40,40)))
        veiculo = ImageTk.PhotoImage(Image.open('truck.png').resize((40,40)))
        relatorio = ImageTk.PhotoImage(Image.open('file.png').resize((35,35)))
        config = ImageTk.PhotoImage(Image.open('setting.png').resize((30,30)))


        dash_b = ctk.CTkButton(frame_menu_lateral,text='Dashboard',image=dash,font=(0,21),fg_color='lightgray',text_color='black',hover_color='lightblue',width=150)
        motoristas_b = ctk.CTkButton(frame_menu_lateral,text='Motoristas',image=motorista,font=(0,21),fg_color='lightgray',text_color='black',hover_color='lightblue',width=150)
        veiculos_b = ctk.CTkButton(frame_menu_lateral,text='Veiculos',image=veiculo,font=(0,21),fg_color='lightgray',text_color='black',hover_color='lightblue',width=150)
        relatorio_b = ctk.CTkButton(frame_menu_lateral,text='Relatorio',image=relatorio,font=(0,21),fg_color='lightgray',text_color='black',hover_color='lightblue',width=50)
        config_b = ctk.CTkButton(frame_menu_lateral,text='',image=config,font=(0,21),fg_color='lightgray',text_color='black',hover_color='lightblue',width=50)



        dash_b.grid(row=1,column=0,pady=5,padx=5,)
        motoristas_b.grid(row=2,column=0,pady=5,padx=5)
        veiculos_b.grid(row=3,column=0,pady=5,padx=5)
        relatorio_b.grid(row=4,column=0,pady=5,padx=5)
        config_b.grid(row=5,column=0,pady=5,padx=5,sticky='ws')

    def frame_conteudo(self):
        frame_conteudo_principal = ctk.CTkFrame(self.master,fg_color='lightblue',corner_radius=0)
        frame_conteudo_principal.grid(row=0,column=1,sticky='nswe')

        TelaMotoristas(frame_conteudo_principal)