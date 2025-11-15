# from Controller.veiculo_controller import VeiculoController
# from Model.veiculo import Veiculo
# from Model.motorista import Motorista
# from Controller.motorista_controller import MotoristaController
# # # moto teste INSERIDO
# # moto_teste = Motorista('teste','3123213','23123213','3131232')
# # print(MotoristaController.inserir(moto_teste))

# # print(MotoristaController.inserir(moto_teste))

# # veiculo teste INSERIDO
# m = Motorista('TESTE333333','11234123412','123123123123','123asdzxcqweasd')
# a = MotoristaController.inserir(m)
# for c,v in a.keys:
#     print(c,v)
import customtkinter as ctk
from View.tela_main import TelaMain
if __name__ == '__main__':
    app = ctk.CTk()
    TelaMain(app)
    app.title('Tela Principal')
    app.configure(fg_color='orange')
    app.columnconfigure(0,weight=1)
    app.columnconfigure(1,weight=40)
    app.rowconfigure(0,weight=1)
    app.geometry('600x600')
    app.mainloop()